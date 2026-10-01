---
name: import-lesswrong
description: Import one of Axel's LessWrong posts into the site as a blog post under Writing, dated by its original posting date. Use when given a lesswrong.com/posts/... URL to add to the site.
---

# Import a LessWrong post

1. Run the importer from the repo root:

   ```sh
   python3 scripts/import_lesswrong.py <lesswrong-post-url>
   ```

   It writes `_posts/<date>-<slug>.markdown` and downloads any images to
   `assets/posts/<slug>/`. It handles footnotes (rebuilt from LessWrong's HTML,
   since the Markdown export drops their links and lists), heading levels, math
   (`$x$` → kramdown's `$$x$$`, plus `math: true` to load KaTeX), and the
   "Originally posted on LessWrong" line. Pass `--force` to re-import over an
   existing file.

2. Resolve the TODOs it prints:
   - **Excerpt**: one or two sentences for the home page and post listings. It
     shows on the home page under Recent, so make it a hook, not a summary
     of the first paragraph.
   - **Image alt text**: LessWrong usually labels uploads `image.png`. Look at
     each image and describe what it shows.

3. Downscale large images. Body text is about 750px wide, so 1600px covers
   retina screens: `sips -Z 1600 assets/posts/<slug>/*.png`.

4. Read the post through for anything the script didn't handle. Watch for a
   `WARNING` about the inline math count: it means a `$` was converted as math
   when it wasn't, or the other way round. Dollar amounts like `$180M ... $5B`
   are deliberately left alone.

5. Build (`bundle exec jekyll build`) and look at the post in a browser:
   images, footnotes, block quotes and any math.

Don't fix typos or edit the prose without asking. The post should match what
was published on LessWrong.
