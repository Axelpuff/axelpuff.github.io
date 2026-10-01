#!/usr/bin/env python3
"""Import a LessWrong post as a Jekyll post in _posts/.

Usage: python3 scripts/import_lesswrong.py <lesswrong-post-url> [--force]

Pulls the post from LessWrong's GraphQL API and writes
_posts/<date>-<slug>.markdown, dated by the original posting time
(US Eastern). The body comes from LessWrong's Markdown export; footnotes
are rebuilt from the HTML, because the Markdown export drops their links,
italics, and lists. Images are downloaded into assets/posts/<slug>/ so the
post doesn't depend on LessWrong's image host.

The excerpt is a placeholder and image alt text is copied as-is; both are
printed as TODOs at the end for a human to fill in.
"""

import html
import json
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent.parent
API = "https://www.lesswrong.com/graphql"
QUERY = """{ post(input: {selector: {_id: "%s"}}) { result {
  title slug postedAt pageUrl contents { markdown html } } } }"""
EXCERPT_PLACEHOLDER = "TODO: one-sentence excerpt"


def fetch_post(post_id):
    req = urllib.request.Request(
        API,
        data=json.dumps({"query": QUERY % post_id}).encode(),
        headers={"Content-Type": "application/json", "User-Agent": "axelsite-import"},
    )
    with urllib.request.urlopen(req) as resp:
        result = json.load(resp)["data"]["post"]["result"]
    if not result:
        sys.exit(f"No LessWrong post with id {post_id}")
    return result


def html_inline_to_markdown(s):
    s = re.sub(r'<a href="([^"]+)"[^>]*>(.*?)</a>',
               lambda m: f"[{m.group(2)}]({html.unescape(m.group(1))})", s, flags=re.S)
    s = re.sub(r"</?(b|strong)>", "", s)  # bold in footnotes is usually stray formatting
    s = re.sub(r"</?span[^>]*>", "", s)
    # Keep spaces outside the asterisks: "<i>Xunzi </i>Chapter" -> "*Xunzi* Chapter"
    s = re.sub(r"<(i|em)>(\s*)(.*?)(\s*)</\1>", r"\2*\3*\4", s, flags=re.S)
    s = re.sub(r"<[^>]+>", "", s)
    return html.unescape(s).replace("\xa0", " ").strip()


def footnotes_from_html(h):
    """Map LessWrong footnote id -> Markdown body (may span several paragraphs)."""
    notes = {}
    pattern = (r'<li class="footnote-item"[^>]*data-footnote-id="(\w+)"[^>]*>'
               r'.*?<div class="footnote-content"[^>]*>(.*?)</div></li>')
    for fid, content in re.findall(pattern, h, re.S):
        paras = [html_inline_to_markdown(p) for p in re.findall(r"<p>(.*?)</p>", content, re.S)]
        blocks = []
        for p in filter(None, paras):
            # LessWrong flattens footnote lists into "- item" paragraphs
            if p.startswith("- ") and blocks and blocks[-1].startswith("- "):
                blocks[-1] += "\n" + p
            else:
                blocks.append(p)
        notes[fid] = "\n\n".join(blocks)
    return notes


def convert_math(body, expected):
    # Pandoc's rule for inline $...$: no space just inside the delimiters and
    # no digit right after the closing $. Keeps "$180M ... $5B" as currency.
    pattern = r"(?<![\$\\])\$(?=\S)([^$\n]+?)(?<=\S)\$(?![\$\d])"
    found = len(re.findall(pattern, body))
    if found != expected:
        print(f"WARNING: found {found} inline math spans, LessWrong has {expected}. "
              "Check the $$...$$ conversions by hand.")
    return re.sub(pattern, r"$$\1$$", body)


def download_images(body, slug):
    def save(m):
        alt, url = m.group(1), m.group(2)
        if not url.startswith("http"):
            return m.group(0)
        name = url.rsplit("/", 1)[-1].split("?")[0]
        dest = ROOT / "assets" / "posts" / slug / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(url, dest)
        print(f"Downloaded {url} -> {dest.relative_to(ROOT)}")
        return f"![{alt}]({{{{ '/assets/posts/{slug}/{name}' | relative_url }}}})"
    return re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", save, body)


def convert(post):
    md, h = post["contents"]["markdown"], post["contents"]["html"]

    # Split off the Markdown export's footnote definitions; we rebuild them from HTML.
    first_def = re.search(r"^\[\^\w+\]:", md, re.M)
    body = (md[:first_def.start()] if first_def else md).rstrip()
    notes = footnotes_from_html(h)
    refs = list(dict.fromkeys(re.findall(r"\[\^(\w+)\]", body)))
    missing = set(refs) ^ set(notes)
    if missing:
        sys.exit(f"Footnote mismatch between Markdown and HTML: {missing}")

    # Demote headings one level so they sit under the post title.
    body = re.sub(r"^(#{1,5}) ", r"#\1 ", body, flags=re.M)
    body = re.sub(r"^(.+)\n=+$", r"## \1", body, flags=re.M)
    body = re.sub(r"^(.+)\n-{3,}$", r"### \1", body, flags=re.M)

    has_math = 'class="math-tex"' in h
    if has_math:
        body = convert_math(body, h.count('class="math-tex"'))

    body = re.sub(r"^\*\s+", "- ", body, flags=re.M)      # "*   item" -> "- item"
    body = re.sub(r"^(\d+)\.\s+", r"\1. ", body, flags=re.M)
    body = re.sub(r"\n[ \t\xa0]+\n", "\n\n", body)          # whitespace-only spacer lines
    body = re.sub(r"\n{3,}", "\n\n", body)
    body = re.sub(r"\)  +\[", ") [", body)                  # double spaces between links
    body = download_images(body, post["slug"])

    # Number footnotes in order of first reference, for readable source.
    for n, fid in enumerate(refs, 1):
        body = body.replace(f"[^{fid}]", f"[^{n}]")
    defs = "\n\n".join(
        f"[^{n}]: " + notes[fid].replace("\n", "\n    ").replace("\n    \n", "\n\n")
        for n, fid in enumerate(refs, 1))

    posted = datetime.fromisoformat(post["postedAt"].replace("Z", "+00:00"))
    posted = posted.astimezone(ZoneInfo("America/New_York"))
    title = post["title"].replace('"', '\\"')
    front = [
        "---",
        "layout: post",
        f'title:  "{title}"',
        f"date:   {posted.strftime('%Y-%m-%d %H:%M:%S %z')}",
        "categories: writing",
        f'excerpt: "{EXCERPT_PLACEHOLDER}"',
    ]
    if has_math:
        front.append("math: true")
    front.append("---")

    crosspost = (f"*Originally posted on [LessWrong]({post['pageUrl']}).*\n"
                 "{: .post-crosspost}")
    text = "\n".join(front) + "\n\n" + body + "\n\n" + crosspost + "\n"
    if defs:
        text += "\n" + defs + "\n"
    return posted, text


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    m = re.search(r"/posts/(\w+)", args[0])
    if not m:
        sys.exit(f"Not a LessWrong post URL: {args[0]}")

    post = fetch_post(m.group(1))
    posted, text = convert(post)
    dest = ROOT / "_posts" / f"{posted:%Y-%m-%d}-{post['slug']}.markdown"
    if dest.exists() and "--force" not in sys.argv:
        sys.exit(f"{dest.relative_to(ROOT)} already exists; pass --force to overwrite")
    dest.write_text(text)

    print(f"Wrote {dest.relative_to(ROOT)}")
    print("TODO: replace the excerpt placeholder")
    for alt in re.findall(r"!\[([^\]]*)\]", text):
        print(f"TODO: write real alt text for image currently labelled {alt!r}")


if __name__ == "__main__":
    main()
