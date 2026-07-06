#!/usr/bin/env python3
"""Generate the 5 service subpages from a common scaffold.

Kept in-repo (scripts/) so the same generator can seed a NEW client site
by swapping the SERVICES dict and running again. This is the "reusable
component kit" applied to page generation, not just CSS.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SERVICES = {
    "auto-insurance.html": {
        "slug": "auto-insurance",
        "title": "Auto Insurance in Houston, TX | Marv Thorn Insurance",
        "meta":  "Independent auto insurance in Houston, TX. Marv Thorn shops top-rated carriers for liability, collision, comprehensive, uninsured motorist, and rideshare coverage.",
        "eyebrow": "Auto Coverage",
        "h1": "Auto insurance, priced from every carrier — not just the one on TV.",
        "lede": "Texas-minimum through full coverage, shopped across multiple top-rated carriers so you see the real spread — not just the first app quote.",
        "sections": [
            ("What's included in a real quote", [
                "Bodily injury + property damage liability (above Texas minimums when it matters)",
                "Collision + comprehensive with realistic deductibles",
                "Uninsured / underinsured motorist — critical in Houston traffic",
                "Medical payments (MedPay) or Personal Injury Protection (PIP)",
                "Rental reimbursement + roadside assistance",
                "Rideshare endorsement if you drive Uber, Lyft, DoorDash, or delivery",
                "Multi-vehicle + multi-line bundling with your home / flood / life",
            ]),
            ("How Marv shops it", [
                "Pulls quotes from multiple top-rated carriers at the same coverage level",
                "Flags where a slightly higher premium buys materially better protection",
                "Compares deductible options so you understand the trade-off before you sign",
                "Rechecks at every renewal — if the market has shifted, he tells you",
            ]),
        ],
    },
    "home-insurance.html": {
        "slug": "home-insurance",
        "title": "Home Insurance in Houston, TX | Marv Thorn Insurance",
        "meta":  "Homeowners insurance in Houston, TX. Independent agent Marv Thorn shops top-rated carriers for HO-3, HO-5, renters, and condo policies — with real hail, wind, and water-backup coverage.",
        "eyebrow": "Home Coverage",
        "h1": "Home insurance built for Houston's storm cycle — not a national average.",
        "lede": "Homeowners, renters, condo. Full replacement cost, hail &amp; wind endorsements, water backup, personal property. Tuned for the weather you actually live under.",
        "sections": [
            ("What's included", [
                "Dwelling (structure) at full replacement cost — not market value",
                "Personal property (contents) at replacement, not depreciated actual cash value",
                "Loss of use / additional living expenses if your home is uninhabitable",
                "Personal liability + medical payments for guest injuries",
                "Wind &amp; hail endorsement — critical along the Gulf Coast",
                "Water backup coverage (sewer / drain) — often excluded by default",
                "Ordinance or law coverage for older Houston homes",
            ]),
            ("What Marv double-checks in Houston", [
                "Whether wind &amp; hail is inside the policy or requires a separate TWIA endorsement",
                "Whether your dwelling limit will actually rebuild your home at 2026 material prices",
                "Whether flood is covered (it is NOT — see flood insurance)",
                "Whether your carrier is one that has been paying claims in your zip code",
            ]),
        ],
    },
    "flood-insurance.html": {
        "slug": "flood-insurance",
        "title": "Flood Insurance in Houston, TX | Marv Thorn Insurance",
        "meta":  "Flood insurance in Houston, TX — NFIP and private-market policies. Standard homeowners does NOT cover flood in Harris County. Independent agent Marv Thorn quotes both markets.",
        "eyebrow": "Flood Coverage · Houston-critical",
        "h1": "Standard homeowners does not cover flood. In Harris County, that gap is the whole game.",
        "lede": "Marv writes both NFIP (National Flood Insurance Program) and private-market flood policies. Inside a flood zone or outside one, the right flood policy is often the single most important line in a Houston coverage stack.",
        "sections": [
            ("Why this line matters more here", [
                "Standard HO-3 / HO-5 homeowners policies explicitly exclude flood damage",
                "Harris County flooding regularly affects homes OUTSIDE mapped flood zones",
                "FEMA maps lag reality — the last decade of storms proved it",
                "Once a storm is named, coverage cannot be bound retroactively (waiting period)",
                "Rebuilding out of pocket after a real flood is a household-ending event",
            ]),
            ("What Marv quotes", [
                "NFIP policy through a Write-Your-Own carrier (federally-backed)",
                "Private-market flood alternatives — often more coverage, sometimes lower premium",
                "Building + contents coverage set at realistic Houston rebuild values",
                "Excess flood coverage over NFIP limits if you have high-value contents",
                "Landlord / rental property flood",
            ]),
        ],
    },
    "life-insurance.html": {
        "slug": "life-insurance",
        "title": "Life Insurance in Houston, TX | Marv Thorn Insurance",
        "meta":  "Life insurance in Houston, TX. Term life, whole life, and final expense — sized for your family, not maximized for commission. Independent agent Marv Thorn.",
        "eyebrow": "Life Coverage",
        "h1": "Life insurance sized for your family — not for someone's commission.",
        "lede": "Term life for income replacement. Whole life where it earns its place. Final expense so a funeral is not the family's first bill. Explained, then quoted — in that order.",
        "sections": [
            ("What Marv writes", [
                "Term life (10, 15, 20, 30 year) — the most cost-efficient income replacement for most families",
                "Whole life &amp; universal life — for specific estate or cash-value needs, not defaulted to",
                "Final expense — small policies to cover funeral and closing costs",
                "Mortgage protection — if income loss should not put the house at risk",
                "Business key-person + buy-sell life — for small-business owners",
            ]),
            ("How Marv sizes the coverage", [
                "Household income × years of dependence (usually 10–20× income for young families)",
                "Plus mortgage balance + kids' expected education",
                "Minus existing employer group life (which is often not portable)",
                "Compared across multiple carriers — health underwriting differs meaningfully",
            ]),
        ],
    },
    "commercial-insurance.html": {
        "slug": "commercial-insurance",
        "title": "Commercial &amp; Business Insurance in Houston, TX | Marv Thorn Insurance",
        "meta":  "Commercial insurance in Houston, TX — general liability, workers' comp, commercial auto, BOP, professional liability, and cyber. Marv Thorn shops top-rated carriers for small businesses.",
        "eyebrow": "Commercial Coverage",
        "h1": "Small-business insurance for Houston contractors, shops, and service firms.",
        "lede": "General liability, workers' comp, commercial auto, BOP, professional liability, cyber. Built to bind fast without giving up coverage. Marv talks to underwriters directly.",
        "sections": [
            ("Lines Marv writes for Houston small businesses", [
                "General Liability (GL) — the foundation policy for any client-facing business",
                "Business Owner's Policy (BOP) — GL + property, priced as a bundle",
                "Workers' Compensation — required in Texas for most employers past a threshold",
                "Commercial Auto — trucks, fleets, hotshot / delivery vehicles",
                "Professional Liability (E&amp;O) — for advisors, consultants, agents, contractors",
                "Cyber liability + data breach — increasingly non-optional",
                "Contractor bonds + certificate-of-insurance issuance for jobsites",
            ]),
            ("How Marv works with owners", [
                "One 20-minute conversation to understand the risk footprint (not a 60-page form)",
                "Direct outreach to admitted-market carriers first, surplus-lines when needed",
                "Certificates of insurance issued same-day when a job requires proof",
                "Renewals reviewed proactively — not silently rolled at last year's rate",
            ]),
        ],
    },
}

def render(name, s):
    h1 = s["h1"]
    lede = s["lede"]
    sections_html = ""
    for heading, bullets in s["sections"]:
        li = "".join(f"      <li>{b}</li>\n" for b in bullets)
        sections_html += f"""
    <div class="reveal">
      <p class="eyebrow">Details</p>
      <h2>{heading}</h2>
      <ul style="padding-left:1.2rem;line-height:1.85;">
{li}      </ul>
    </div>
"""
    canonical = f"https://l3escott.github.io/marv-thorn-preview/{name}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{s["title"]}</title>
<meta name="description" content="{s["meta"]}">
<meta name="theme-color" content="#1F3A2E">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{s["title"]}">
<meta property="og:description" content="{s["meta"]}">
<meta property="og:url" content="{canonical}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/tokens.css">
<link rel="stylesheet" href="assets/css/components.css">
<link rel="icon" href="assets/img/logo-mark.svg" type="image/svg+xml">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","name":"{s["title"].split("|")[0].strip()}","provider":{{"@type":"InsuranceAgency","name":"Marv Thorn Insurance","telephone":"+1-713-555-0142","address":{{"@type":"PostalAddress","addressLocality":"Houston","addressRegion":"TX","addressCountry":"US"}}}},"areaServed":{{"@type":"City","name":"Houston"}},"url":"{canonical}"}}
</script>
</head>
<body>
<a href="#main" class="skip-link">Skip to main content</a>
<div style="background:#1F3A2E;color:#F7F1E5;text-align:center;padding:.5rem 1rem;font-size:.82rem;letter-spacing:.02em;"><strong style="color:#C55F3F">PREVIEW BUILD</strong> · placeholder business name, phone, email &amp; address — all details confirmed with Marv before launch.</div>

<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="Marv Thorn Insurance — Home"><span class="brand-mark">MT</span><span>Marv Thorn <em style="font-style:normal;color:var(--muted-strong);font-size:0.82em;">Insurance</em></span></a>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="primary-nav"><span></span></button>
    <nav class="nav" id="primary-nav" aria-label="Primary">
      <a href="index.html">Home</a>
      <a href="services.html" aria-current="page">Coverage</a>
      <a href="about.html">About</a>
      <a href="testimonials.html">Reviews</a>
      <a href="contact.html">Contact</a>
      <a class="btn btn-primary" href="contact.html#quote" style="min-height:44px;padding:.55rem 1.1rem;font-size:.9rem;">Get a Quote</a>
    </nav>
  </div>
</header>

<main id="main">
<section class="hero" style="padding-block:clamp(4rem,7vw,6rem);">
  <div class="container">
    <p class="eyebrow">{s["eyebrow"]}</p>
    <h1 style="font-size:var(--step-6);max-width:22ch;">{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="hero-actions" style="margin-top:var(--sp-5);">
      <a class="btn btn-primary" href="contact.html#quote">Get a quote for this line</a>
      <a class="btn btn-secondary" href="tel:+17135550142">Call (713) 555-0142</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container-narrow stack-lg">
{sections_html}  </div>
</section>

<section class="section-tight">
  <div class="container">
    <div class="cta-banner reveal">
      <div><h2>Ready to see what Marv can find?</h2><p>Tell him what you have — plain-English comparison within one business day.</p></div>
      <div class="cta-actions"><a class="btn btn-primary" href="contact.html#quote">Start my quote</a><a class="btn btn-ghost" href="tel:+17135550142">Or call (713) 555-0142</a></div>
    </div>
  </div>
</section>

</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div><div class="footer-brand"><span class="brand-mark">MT</span><span>Marv Thorn Insurance</span></div><p>Independent insurance agent serving Houston, TX and surrounding Harris County communities.</p></div>
      <div><h4>Coverage</h4><ul><li><a href="auto-insurance.html">Auto</a></li><li><a href="home-insurance.html">Home</a></li><li><a href="flood-insurance.html">Flood</a></li><li><a href="life-insurance.html">Life</a></li><li><a href="commercial-insurance.html">Commercial</a></li></ul></div>
      <div><h4>Agency</h4><ul><li><a href="about.html">About Marv</a></li><li><a href="testimonials.html">Reviews</a></li><li><a href="contact.html">Contact</a></li></ul></div>
      <div><h4>Direct</h4><ul><li><a href="tel:+17135550142">(713) 555-0142</a></li><li><a href="mailto:hello@marvthorn.example">hello@marvthorn.example</a></li><li>1200 Main Street<br>Houston, TX 77002</li></ul></div>
    </div>
    <div class="footer-bottom"><span>© <span id="yr">2026</span> Marv Thorn Insurance · placeholder branding · Independent agency.</span><span>Built by <a href="https://digitalopsystems.com">Digital Ops Systems</a></span></div>
  </div>
</footer>
<script>document.getElementById('yr').textContent=new Date().getFullYear();</script>
<script defer src="assets/js/site.js"></script>
</body>
</html>
"""

if __name__ == "__main__":
    for name, spec in SERVICES.items():
        out = ROOT / name
        out.write_text(render(name, spec))
        print(f"wrote {out}")
