---
layout: page
title: Writing
permalink: /writing/
---

Crystallized thoughts.

{% assign writing = site.categories.writing %}
{% if writing and writing.size > 0 %}
{% for post in writing %}
- [{{ post.title }}]({{ post.url | relative_url }}) — {{ post.date | date: "%B %-d, %Y" }}
{% endfor %}
{% else %}
Nothing published just yet. Check back soon, or take a look at my
[portfolio]({{ '/' | relative_url }}) in the meantime.
{% endif %}
