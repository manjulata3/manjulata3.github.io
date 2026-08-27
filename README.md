# manjulatasingh.com

Personal site for Manju Lata Singh — QA Lead, Business Analyst, and Test Automation Engineer.

Static HTML/CSS only. No build step, no JavaScript framework, no npm dependencies.

## Site structure

| File | Purpose |
|------|---------|
| `index.html` | Main portfolio page |
| `css/site.css` | All site styles (light/dark, responsive, accessible) |
| `resume.html` | HTML resume (crawlable, screen-reader friendly) |
| `resume.pdf` | Downloadable resume PDF |
| `img/logos/` | Employer logos used on the experience timeline |
| `img/photos/` | LinkedIn banner (`banner.jpeg`) and profile (`profile.jpeg`) |
| `resume.docx` | Source resume document |

## Local preview

From this directory:

```bash
python3 -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080).

## Editing content

- **Home page copy** — edit `index.html` directly. Sections: hero, about, skills, experience timeline, education, contact.
- **Resume (HTML)** — edit `resume.html`. Keep it in sync with the docx when the resume changes.
- **Styles** — edit `css/site.css`. Uses CSS custom properties and `prefers-color-scheme` for dark mode.
- **Logos** — add employer images to `img/logos/` and reference them in the experience timeline in `index.html`.

## Regenerating the PDF

Preferred (requires Google Chrome):

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=resume.pdf \
  "file://$(pwd)/resume.html"
```

Fallback (uses ReportLab, no browser needed):

```bash
python3 scripts/generate_resume_pdf.py
```

Keep the filename `resume.pdf` so site download links keep working.

## Verify links

Check that every local asset referenced in HTML resolves:

```bash
python3 scripts/verify_links.py
```

## Deploy

Upload the site root to any static host (GitHub Pages, S3, Netlify, etc.). No build or compile step required.
