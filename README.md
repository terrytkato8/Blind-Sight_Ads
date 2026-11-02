# Blind Sight — Brand Partnerships Hub

A static site holding the in-game advertising and product placement program for **Blind Sight** (Kato.8 Studios LLC): rate card, pitch deck, readiness plan, term sheets, agreements, SLA, RFP, creative guidelines, creator LOI, the Unreal sponsor-slot spec, finance operations, a browser-based sales CRM and downloadable spreadsheets.

> Confidential working drafts. Legal documents need review by a licensed California attorney before use; finance guidance needs a CPA.

## Layout

```
site/content/    Markdown source, one file per page (edit these)
site/template.html  Shared page layout and styles
site/assets/     Kato.8 Studios logos
site/downloads/  Spreadsheets and other downloadable files
build.py         Renders site/ into docs/
docs/            Generated site (GitHub Pages serves this folder)
```

Each Markdown file starts with a small header that sets its title and where it appears in the sidebar:

```
title: Rate Card
section: Program
order: 1
---
```

Sections, in sidebar order: Start, Program, Term Sheets, Agreements, Sales, Build & Operations.

The Sales CRM stores client records in the browser's local storage. Use its Export backup button to create a portable JSON backup before changing devices or clearing browser data. It does not provide shared team access or server-side storage.

## Editing

```bash
pip install markdown
python3 build.py
```

Commit both `site/` and the regenerated `docs/`.

## Publishing with Vercel

The static output can be deployed to Vercel from `docs/`:

```bash
npx vercel docs --prod
```

## Publishing with GitHub Pages

Repository **Settings → Pages → Build and deployment → Deploy from a branch → `main` / `/docs`**.

**Visibility:** if this repository is public, the Pages site is public too, including pricing and draft contracts. Keep the repository private (GitHub Pages on private repositories needs a paid plan), or host the site somewhere access-controlled.
