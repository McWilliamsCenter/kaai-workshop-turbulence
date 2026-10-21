# KAAI Workshop Website

Static save-the-date site for the KAAI Workshop on AI Methods for Turbulence and
Early-Universe Signals (Carnegie Mellon University, November 2–6, 2026).

Plain HTML/CSS/JS. No build step, no dependencies.

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
| Schedule | `#schedule` section | Placeholder day blocks. When a schedule CSV exists, run `python3 scripts/build_schedule.py <file.csv>` to regenerate the content between the `SCHEDULE:START/END` markers |
| Speakers | `#speakers` section | Replace the "to be announced" note with `.speaker-grid` / `.speaker-card` markup (styles are in `css/style.css`) |
| Registration | `#registration` section | Add registration link/form |
| Committee | `#committee` section | Missing affiliation and homepage links are marked with TODO comments |

The current logo is a placeholder drawn as `img/logo.svg` (turbulent eddies, a CMB-like
speckle field, and a gravitational-wave chirp). To regenerate the PNG sizes from it, run
`rsvg-convert -w <px> -h <px> img/logo.svg -o img/<name>.png` (see sizes below). Don't use CMU's
official logo/wordmark (trademark restrictions).

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
