# marv-thorn-preview

Preview build of the Marv Thorn Insurance website — Digital Ops Systems, Website Design Standard v2 (2026-06-30).

**This is a preview.** Business name, phone, email, and address are placeholders. Every real detail gets confirmed with Marv before launch.

## Live preview

- URL: <https://l3escott.github.io/marv-thorn-preview/>
- Local: `python3 -m http.server 8090` from repo root, then <http://127.0.0.1:8090/>

## Pages

- `/` — Home
- `/about.html` — About Marv
- `/services.html` — Coverage overview
- `/auto-insurance.html`, `/home-insurance.html`, `/flood-insurance.html`, `/life-insurance.html`, `/commercial-insurance.html` — Service subpages
- `/testimonials.html` — Reviews (honest placeholder)
- `/contact.html` — Contact + quote form
- `/404.html`, `/sitemap.xml`, `/robots.txt`

## Design system

- `assets/css/tokens.css` — **client skin** (swap this per client)
- `assets/css/components.css` — **shared kit** (never changes per client)
- `assets/js/site.js` — mobile nav + scroll reveals
- `assets/img/houston-skyline.svg` — original illustration (not stock)
- `assets/img/logo-mark.svg` — placeholder mark

## Docs

- [Design decisions](docs/design-decisions.md) — palette, type, doctrine v2 checklist
- [Placeholder swap map](docs/config.md) — sed commands to convert preview → real
- [Google Business Profile plan](docs/gbp-plan.md) — drafted, not published

## Reskin for a new client

1. Duplicate this repo.
2. Rewrite `assets/css/tokens.css` (palette, fonts, spacing scale) for the new client's brand.
3. Update the `SERVICES` dict in `scripts/gen_service_pages.py` for their offerings.
4. Search-replace placeholder strings per `docs/config.md`.
5. Every page automatically re-skins.
