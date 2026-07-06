# Placeholder swap map

When Marv confirms his details, run search-and-replace across the repo for each entry below. Every value appears only in listed files.

## Placeholders in use

| Placeholder | Current value | Search token |
|---|---|---|
| Business name | `Marv Thorn Insurance` | grep-safe: `Marv Thorn Insurance` |
| Business name (short) | `Marv Thorn` | `Marv Thorn` (careful — appears inside longer strings too) |
| Phone (display) | `(713) 555-0142` | `(713) 555-0142` |
| Phone (tel:) | `+17135550142` | `+17135550142` |
| Email | `hello@marvthorn.example` | `hello@marvthorn.example` |
| Street | `1200 Main Street` | `1200 Main Street` |
| City / State / ZIP | `Houston, TX 77002` | `Houston, TX 77002` |
| Domain (canonical) | `l3escott.github.io/marv-thorn-preview` | `l3escott.github.io/marv-thorn-preview` |

## Files that reference placeholders

- Every `.html` file at repo root (10 files)
- `assets/img/logo-mark.svg` (initials "MT")
- `sitemap.xml`, `robots.txt`
- `docs/gbp-plan.md`

## Recommended sed one-liners (from repo root)

```bash
# Business name
find . -type f \( -name '*.html' -o -name '*.xml' -o -name '*.md' \) -not -path './.git/*' \
  -exec sed -i 's/Marv Thorn Insurance/CONFIRMED NAME LLC/g' {} +

# Display phone
find . -type f \( -name '*.html' -o -name '*.md' \) -not -path './.git/*' \
  -exec sed -i 's/(713) 555-0142/CONFIRMED PHONE DISPLAY/g' {} +

# tel: phone (E.164)
find . -type f -name '*.html' -not -path './.git/*' \
  -exec sed -i 's/+17135550142/+1CONFIRMEDPHONE/g' {} +

# Email
find . -type f \( -name '*.html' -o -name '*.md' \) -not -path './.git/*' \
  -exec sed -i 's/hello@marvthorn.example/hello@CONFIRMED-DOMAIN/g' {} +

# Address (street + city line)
find . -type f -name '*.html' -not -path './.git/*' \
  -exec sed -i 's/1200 Main Street/CONFIRMED STREET/g; s/Houston, TX 77002/Houston, TX CONFIRMED-ZIP/g' {} +
```

## What NOT to swap yet

- The domain in `<link rel="canonical">` — stays as GH Pages until Marv points a real domain at us.
- The Formspree endpoint in `contact.html` — remains `PLACEHOLDER` until Marv's form endpoint is set up.
- The map iframe center — update once we have Marv's actual office coordinates.
- The Marv biography block on `about.html` (currently a stub) — drop in the full bio and pro photo when Marv sends them.
