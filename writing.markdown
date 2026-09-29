---
layout: page
title: Writing
permalink: /writing/
---

I do not want this page to evoke the familiar sensation of "yet another dead aspirational blog, how sad." If it does, please message me directly and I will post something. Potentially on a subject of your choice.

{% assign writing = site.categories.writing %}
{% if writing and writing.size > 0 %}
{% for post in writing %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%B %-d, %Y" }}
{% endfor %}
{% else %}
Nothing published just yet. Check back soon, or take a look at my
[portfolio]({{ '/' | relative_url }}) in the meantime.
{% endif %}
