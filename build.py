#!/usr/bin/env python3
"""Build the Blind Sight Brand Partnerships Hub.

Reads Markdown pages from site/content/, renders them with a shared layout, and
writes a static site to docs/ (served by GitHub Pages from the /docs folder).

Usage:  pip install markdown   then   python3 build.py
"""
import html
import re
import shutil
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent
CONTENT = ROOT / "site" / "content"
OUT = ROOT / "docs"
SECTIONS = ["Start", "Program", "Term Sheets", "Agreements", "Sales", "Build & Operations"]


def parse(path):
    raw = path.read_text(encoding="utf-8")
    meta_block, body = raw.split("\n---\n", 1)
    meta = dict(line.split(":", 1) for line in meta_block.strip().splitlines())
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    return {
        "slug": path.stem,
        "title": meta["title"],
        "section": meta.get("section", "Start"),
        "order": int(meta.get("order", 99)),
        "body": body,
    }


def render_md(text):
    text = re.sub(r"~~(.+?)~~", r"<del>\1</del>", text)
    out = markdown.markdown(text, extensions=["tables", "fenced_code", "toc", "sane_lists"])
    out = out.replace("<li>[ ] ", '<li class="task"><input type="checkbox" disabled> ')
    out = out.replace("<li>[x] ", '<li class="task"><input type="checkbox" checked disabled> ')
    out = out.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    return out


def nav(pages, current):
    parts = []
    for section in SECTIONS:
        items = sorted((p for p in pages if p["section"] == section), key=lambda p: p["order"])
        if not items:
            continue
        parts.append(f'<p class="nav-section">{html.escape(section)}</p><ul>')
        for p in items:
            href = "index.html" if p["slug"] == "index" else f'{p["slug"]}.html'
            cls = ' class="active"' if p["slug"] == current else ""
            parts.append(f'<li><a href="{href}"{cls}>{html.escape(p["title"])}</a></li>')
        parts.append("</ul>")
    return "\n".join(parts)


TEMPLATE = (ROOT / "site" / "template.html").read_text(encoding="utf-8")


def main():
    pages = [parse(p) for p in sorted(CONTENT.glob("*.md"))]
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    for folder in ("assets", "downloads"):
        shutil.copytree(ROOT / "site" / folder, OUT / folder)
    (OUT / ".nojekyll").write_text("")
    for p in pages:
        page = (
            TEMPLATE.replace("{{title}}", html.escape(p["title"]))
            .replace("{{nav}}", nav(pages, p["slug"]))
            .replace("{{section}}", html.escape(p["section"]))
            .replace("{{content}}", render_md(p["body"]))
        )
        (OUT / f'{p["slug"]}.html').write_text(page, encoding="utf-8")
    print(f"Built {len(pages)} pages into {OUT}")


if __name__ == "__main__":
    main()
