# KAAI Workshop Website

Static save-the-date site for the KAAI Workshop on AI Methods for Turbulence and
Early-Universe Signals (Carnegie Mellon University, November 2–6, 2026).

Plain HTML/CSS/JS. No build step, no dependencies.

Live at https://mcwilliamscenter.github.io/kaai-workshop-turbulence/, served by GitHub Pages
from the root of `main` in `McWilliamsCenter/kaai-workshop-turbulence`. Pushing to `main`
updates the site within a minute or two.

## Local preview

Open `index.html` directly in a browser, or serve the directory:

```
python3 -m http.server 8000
```

then visit `http://localhost:8000`.

## Where to edit each TBD section

All content lives in `index.html`; styling in `css/style.css`; the nav toggle and countdown
script in `js/main.js`.

| Section | Look for | Notes |
|---|---|---|
| Overview / Topics | `#overview` section | Wording marked for review with the organizers |
| Schedule | `schedule.csv` | Edit the CSV, then run `python3 scripts/build_schedule.py schedule.csv` to regenerate the `#schedule` content between the `SCHEDULE:START/END` markers. Talk titles are TBA |
| Slides | `#slides` section, `slides/` folder | Put the PDF in `slides/` (e.g. `lastname-short-title.pdf`) and copy a `.slide-item` |
| Speakers | `#speakers` section, `.speaker-card` | Photos are 480×480 JPGs in `img/speakers/`. Cards without a photo use a `.speaker-initials` placeholder; swap it for an `<img>` when a photo arrives |
| Registration | `#registration` section | Registration closed; "Join on Zoom" button links to the Zoom meeting |
| Committee | `#committee` section | Homepage links are marked with a TODO comment |

The logo is cropped from a turbulence render (`ai_turbulence_logo.png`, 3840×2160, kept out
of the repo) into a round, red-ringed badge. To regenerate it from a new source image, run
`python3 scripts/make_logo.py <source.png> master.png <x0> <y0> <size>` (square crop in source
pixels; the current logo uses `960 0 2160`), then resize `master.png` to each size below, e.g.
`convert master.png -resize 160x160 -strip img/logo.png`.

The countdown target date is set in `js/main.js` (`workshopStart`).

## Images

`img/` holds pre-sized, web-optimized copies of the logo. Keep source art (large master
files) out of the repo and only commit the sizes actually referenced by the site:

| File | Size | Used for |
|---|---|---|
| `img/logo.png` | 160×160 | header + footer logo |
| `img/logo-hero.png` | 480×480 | hero logo, next to the title |
| `img/apple-touch-icon.png` | 180×180 | iOS home-screen icon |
| `img/favicon-32.png` | 32×32 | favicon |
| `img/favicon-16.png` | 16×16 | favicon |
