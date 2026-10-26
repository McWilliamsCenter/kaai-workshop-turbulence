# KAAI Workshop Website — Project Spec

## What this is

A static website announcing the **KAAI Workshop on AI Methods for Turbulence and
Early-Universe Signals**, hosted at Carnegie Mellon University, November 2–6, 2026.
This repo was adapted from the site for the previous installment (Foundation Models &
Agentic Methods for Astrophysical Simulation, Aug 31–Sep 3). The workshop is part of the
sequence run under the Simons Foundation
**Keystone Astronomy & AI (KAAI) Fellows Program**
(https://www.cmu.edu/astro-cosmology/research/simons-kaai-fellows/index.html).

This is a **draft / save-the-date stage site**. Several sections are intentionally TBD and
will be filled in over the coming months. The site should look complete and professional
even with placeholder content — TBD sections should read as "more info coming soon," not
as broken or unfinished parts of the page.

Design reference (structure only, not content density): https://sbi-galev.github.io/2026/index.html
That site is a good model for section layout and typography but is more information-dense
than we need right now. Prefer a shorter, less cluttered page.

---

## Tech stack (decided)

- **Plain HTML + CSS + minimal vanilla JS.** No build step, no framework, no static site
  generator. This keeps it trivial to hand-edit later and trivial to deploy.
- Single page (`index.html`) with anchor-linked sections, following the reference site's
  pattern. Do not split into multiple pages yet — everything fits on one page at this stage.
- **Hosting: GitHub Pages.** Repo root (or `/docs`) serves directly, no CI/build pipeline
  needed. Structure the repo so `index.html` is deployable as-is via Pages settings.
- Fonts: use a system font stack or a single Google Font pairing (serif for headings, clean
  sans for body) loaded via `<link>` — avoid heavy font-loading JS.
- No JS framework, no npm dependencies unless there's a strong reason. Small vanilla JS is
  fine for: smooth-scroll nav, mobile nav toggle, maybe a simple countdown to the workshop
  dates.

## Design direction (decided)

**Clean, minimal academic style** — closer to the reference site than to a flashy conference
page. Lots of whitespace, restrained color use, clear typographic hierarchy, no stock photos,
no heavy gradients or animation.

Since there's no existing workshop-specific logo or visual identity yet, build the placeholder
identity around **CMU's institutional palette** rather than inventing an unrelated brand:

- Primary accent: **CMU Red** `#C41230`
- Secondary: near-black `#1A1A1A` / dark gray for body text
- Neutral backgrounds: white and a very light warm gray (`#FAFAFA` / `#F5F4F2`)
- Use red sparingly — section labels, links, hover states, key dates — not as large background
  blocks. Let whitespace and typography carry the design.
- No logo yet. Use a simple text wordmark for the workshop name in the header (e.g. small caps
  or letter-spaced sans). Leave a clearly marked spot/placeholder in the HTML (`<!-- TODO: logo -->`)
  where a real logo or KAAI program mark can be dropped in later.
- Typography: a serif or slab-serif for the H1/hero title (gives it academic conference gravitas,
  similar to the reference site's feel), clean sans-serif for nav, body, and cards.

## Tone / copy voice

Precise, understated, technically confident — written for a technically literate audience.
Avoid marketing language ("game-changing," "revolutionary"). Avoid unnecessary adjectives.
Short declarative sentences. This mirrors how the workshop itself is being framed: small,
informal, focused on substance.

---

## Site structure (single page, anchor nav)

Nav bar: `Overview` · `Registration` · `Location` · `Topics` · `Schedule` · `Speakers` · `Committee`

- **Hero:** title **AI Methods for Turbulence and Early-Universe Signals**, "A KAAI Workshop ·
  Carnegie Mellon University", **November 2–6**, countdown, Simons + McWilliams logos.
- **Overview + Topics:** two themes, AI methods for turbulence and early-universe signals.
- **Registration — TBD.** Contact: mgurgeni@andrew.cmu.edu.
- **Location:** unchanged from the previous installment (Wean Hall 8330, CMU).
- **Schedule — tentative.** Mon–Fri program generated from `schedule.csv` with
  `scripts/build_schedule.py`. Talk titles are TBA; don't invent them. Friday is a hackathon day.
- **Speakers:** Arthur Kosowsky, Isak Stomberg, Deyan Mihaylov, Matthew Ho, Muni Zhou (Stephon Alexander
  is on the schedule but not on the speaker list yet). Don't invent positions or affiliations.
- **Organizing Committee:** Tina Kahniashvili (CMU Physics), Barnabás Póczos (CMU MLD),
  Alberto Roper Pol (University of Geneva, Dept. of Theoretical Physics), Murman Gurgenidze (CMU Physics). Don't fabricate
  links that weren't supplied.
- **Footer:** name, dates, CMU, KAAI program link, contact email.
- Hackathon (Friday) appears only in the schedule for now; no separate section until details exist.

## Explicit non-goals for this draft

- No fabricated speaker names, schedule times, or hackathon rules — leave TBD sections
  honestly marked rather than inventing plausible-sounding placeholder content.
- No dependency on a CMS, database, or backend — must remain a fully static site deployable
  via GitHub Pages with zero server-side logic.
- No build tooling (webpack/vite/etc.) — keep it simple enough to edit by hand.
- Don't reuse CMU's official logo/wordmark images (trademark/branding restrictions) — the
  placeholder identity should be *inspired by* CMU red, not a reproduction of official CMU
  or McWilliams Center marks.

## Open items to fill in later (leave TODO comments in code)

- Speaker names + affiliations + photos
- Full schedule
- Registration link/form
- Venue/room details at CMU
- Individual committee member homepage links

## Deployment notes

- Repo should be structured so GitHub Pages can serve it directly from `main` (root or
  `/docs`) with no Actions/build step required.
- Keep all assets (CSS, images, JS) in relative paths so it works both locally
  (open `index.html` directly) and on GitHub Pages.
- Recommend a `README.md` with basic instructions for enabling GitHub Pages in repo settings
  and where to edit each TBD section.