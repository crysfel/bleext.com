#!/usr/bin/env python3
"""raw/ -> site/: strip PHP notices, add CNAME, 404.html, .nojekyll, feed/rss.xml."""
import re, shutil
from pathlib import Path

RAW, SITE = Path("raw"), Path("site")
NOTICE = re.compile(r"(?:<br />\s*)?<b>(?:Notice|Warning|Deprecated|Fatal error)</b>:.*?<br />\s*", re.S)
TEXT = {".html", ".xml", ".txt", ".css", ".js", ".json"}

shutil.rmtree(SITE, ignore_errors=True)
shutil.copytree(RAW, SITE)
fixed = 0
for p in SITE.rglob("*"):
    if p.is_file() and p.suffix in TEXT:
        t = p.read_text("utf-8", "replace")
        n = NOTICE.sub("", t)
        if n != t:
            fixed += 1
            p.write_text(n, "utf-8")
print(f"stripped PHP notices from {fixed} files")

# RSS: GitHub Pages serves .xml as XML, so publish /feed/rss.xml next to the old /feed/rss/ path.
rss = SITE / "feed/rss/index.html"
if rss.exists():
    (SITE / "feed/rss.xml").write_text(rss.read_text("utf-8").lstrip(), "utf-8")

(SITE / "CNAME").write_text("bleext.com\n")
(SITE / ".nojekyll").write_text("")
(SITE / "404.html").write_text("""<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Not found - Bleext</title>
<style>body{font:18px/1.6 system-ui,sans-serif;max-width:32rem;margin:20vh auto;padding:0 1rem;text-align:center}</style>
<h1>Page not found</h1><p>This page doesn't exist (anymore). <a href="/">Back to the Bleext blog</a>.</p>
""")
