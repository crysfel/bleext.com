# bleext.com (static archive)

The Bleext blog (HTMLy, flat-file PHP) frozen as a static site on GitHub Pages: 17 posts, categories, tags,
author pages, `/music`, RSS (`/feed/rss.xml`, also `/feed/rss/`) and sitemaps. Comments (Disqus) still load client-side.

| Path | What |
|---|---|
| `site/` | What Pages serves (`.github/workflows/pages.yml` on push to `master`) |
| `tools/crawl.py` | Crawls a locally running copy of the old site into `raw/` (git-ignored) |
| `tools/build.py` | `raw/` → `site/`: strips PHP notices, adds `CNAME`, `404.html`, `feed/rss.xml` |

Source of the crawl: `/var/www/bleext.com/public` from the sites droplet (archived in
`~/Archives/sites-droplet/www-2026-11-11.tgz`), served with `php -S 127.0.0.1:8123 -t .` on PHP 8.4
after two one-line ternary fixes in `system/includes/functions.php` (lines 161 and 167).
Drafts are not published. Not carried over: the three old `.apk` files and `upload.php`/`record.html`.
