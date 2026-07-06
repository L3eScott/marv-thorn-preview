# Design decisions — Marv Thorn Insurance preview

**Applied doctrine:** Website Design Standard v2 (2026-06-30).

## Visual identity — Marv's skin

Chosen so this site does NOT look like any other DOPS-built site (leescott-website, St. James, SJ Youth Ministry).

| Token | Value | Rationale |
|---|---|---|
| Primary | Deep forest green `#1F3A2E` | Grounded, Southern, trustworthy — **not** the corporate Progressive/Geico/State-Farm blue every big carrier uses. Distinct from prior DOPS sites (which lean blue-ish). |
| Accent | Terracotta `#C55F3F` | Houston brick warmth. One accent color = one CTA color, per Design Standard v2 hero rules. |
| Cream | `#F7F1E5` | Warm ivory background — never stark white. Reads editorial, human. |
| Ink | `#1A1A1A` | Body text. |
| Muted | `#6B6558` | Warm gray, not cool gray — keeps everything on the warm side. |

## Typography

- **Headings — Fraunces (variable serif).** Humanist warmth, editorial feel. Distinct from the ubiquitous Inter/Poppins sans-only insurance sites that all look identical. Fraunces at heavy sizes reads like a good local newspaper or a bookstore brand, not a corporate carrier.
- **Body — Inter.** Clean, legible, contemporary. Pairs cleanly with Fraunces.
- Size scale via `clamp()` — mobile-first, scales up smoothly. Hero H1 hits ~66px desktop, ~44px mobile (per Design Standard v2 §Hero).

## Layout & imagery

- Typography-forward hero — no big generic stock photo. Design Standard v2 forbids generic stock. Since Marv hasn't sent his real photos yet, we lead with big warm type on cream instead. High-craft indie brands do this and it reads more premium in 2026, not less.
- Original SVG illustration of the Houston skyline for the "Local & Independent" trust block. Real Houston reference, zero licensing risk, custom to this site (won't appear on any other DOPS site).
- Testimonials: honest "coming soon" placeholders labeled clearly. NO fabricated quotes.
- Reveal animations are subtle, respect `prefers-reduced-motion`, never applied to body text or nav.

## Reusability

- `assets/css/tokens.css` is the ONLY file that changes per client. Swap it, reskin the whole kit.
- `assets/css/components.css` uses `var(--brand-*)` for every color and font — it does not know or care which client it renders.
- `scripts/gen_service_pages.py` generates service subpages from a dict — new client = swap the `SERVICES` dict, run again.

## Not built (deferred by scope)

- Blog / news layout — deferred until Marv has content or a case study to publish.
- Live chat widget — deferred until Marv confirms whether he wants to answer chat.
- Real form endpoint — Formspree link is a placeholder until Marv's form endpoint (or n8n leads-intake webhook) is bound to a real inbox.
- Real Marv photography — About and hero sections have clearly-marked stubs for when Marv sends photos.
- Google Business Profile — planned in `docs/gbp-plan.md`, publication blocked pending Marv's confirmed details.

## Doctrine v2 checklist — self-assessment

1. ☑ Hero: one headline, one subheadline, one primary CTA (plus a secondary phone button — treat call as the same CTA, different modality).
2. ☑ Headline states customer benefit ("Real insurance, from a real neighbor.") in plain words.
3. ☑ Mobile-first layout — nav collapses to hamburger < 820px, single-column below 640px, tap targets ≥ 44px.
4. ☐ Sub-2.5s LCP — measured post-deploy, see next section of README.
5. ☑ Trust elements: "Independent · Houston-based · Plain-English · Same-day quotes" strip + local strip; **no fake testimonials.**
6. ☑ Accessibility: contrast passes AA on cream/ink and primary/cream; keyboard nav works; alt text on all images; `prefers-reduced-motion` respected; skip-link present.
7. ☑ Visually distinct: warm forest+terracotta+cream + Fraunces/Inter is a new palette+type pair vs. any prior DOPS site.
8. ☐ Lee review + approval — pending your walkthrough of the live URL.
