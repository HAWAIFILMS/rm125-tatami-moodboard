import json, os, base64

ROOT = os.path.dirname(os.path.abspath(__file__))
SPEC_PATH = os.path.join(ROOT, "moodboard_spec.json")
OUTPUT_HTML = os.path.join(ROOT, "tatami_moodboard.html")
LOGO_PATH = os.path.join(ROOT, "hawai_logo.svg")

with open(SPEC_PATH, "r", encoding="utf-8") as f:
    spec = json.load(f)

hawai_logo_svg = ""
if os.path.exists(LOGO_PATH):
    with open(LOGO_PATH, "r", encoding="utf-8") as f:
        hawai_logo_svg = f.read().strip()

def get_base64_image(rel_path):
    full_path = os.path.join(ROOT, rel_path)
    if not os.path.exists(full_path):
        return ""
    mime = "image/jpeg"
    if rel_path.lower().endswith(".png"):
        mime = "image/png"
    with open(full_path, "rb") as img_file:
        b64 = base64.b64encode(img_file.read()).decode("utf-8")
        return f"data:{mime};base64,{b64}"

categories_data = []
total_images = 0

for cat in spec.get("categories", []):
    venues_data = []
    for v in cat.get("venues", []):
        imgs = []
        for p in v.get("images", []):
            b64_src = get_base64_image(p)
            if b64_src:
                imgs.append({
                    "src": b64_src,
                    "rel": p
                })
                total_images += 1
        venues_data.append({
            "id": v.get("id"),
            "name": v.get("name"),
            "tag": v.get("tag"),
            "tag_class": v.get("tag_class", "available"),
            "location": v.get("location"),
            "distance": v.get("distance"),
            "drive_time": v.get("drive_time"),
            "notes": v.get("notes"),
            "images": imgs
        })
    categories_data.append({
        "id": cat.get("id"),
        "label": cat.get("label"),
        "desc": cat.get("desc"),
        "venues": venues_data
    })

print(f"Building editorial moodboard: {len(categories_data)} categories, {sum(len(c['venues']) for c in categories_data)} venues, {total_images} photos.")

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{spec.get('project', 'HAWAI FILMS')} · LOCATION MOODBOARD</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    /* Pure Hawai Brand Surfaces */
    --bg-page: #F9F5E9;
    --bg-surface-subtle: #F2EDE0;
    
    /* Typography & Ink */
    --ink-black: #0F0F0F;
    --ink-charcoal: #2A2A2A;
    --ink-muted: #737373;
    --ink-faint: #A3A3A3;

    /* Hairline Dividers - Single Edge Only */
    --line-hairline: rgba(15, 15, 15, 0.12);
    --line-light: rgba(15, 15, 15, 0.06);

    /* Clean Pill Accents (No Borders, Hugs Text) */
    --pill-green-bg: #E6F4EA;
    --pill-green-text: #1A6B3C;
    --pill-amber-bg: #F2EDE0;
    --pill-amber-text: #78350F;
    --pill-neutral-bg: #EFEAE0;
    --pill-neutral-text: #404040;

    --font-heading: 'Space Grotesk', -apple-system, sans-serif;
    --font-body: 'Barlow', -apple-system, sans-serif;
  }}

  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}

  html {{
    scroll-behavior: smooth;
  }}

  body {{
    background-color: var(--bg-page);
    color: var(--ink-charcoal);
    font-family: var(--font-body);
    -webkit-font-smoothing: antialiased;
    line-height: 1.5;
    padding-bottom: 140px;
  }}

  /* Masthead — Editorial Header with Single Bottom Divider */
  header.masthead {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(249, 245, 233, 0.95);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--line-hairline);
    padding: 20px 64px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .masthead-left {{
    display: flex;
    align-items: center;
    gap: 24px;
  }}

  .hawai-logo {{
    height: 19px;
    width: auto;
    display: flex;
    align-items: center;
  }}
  .hawai-logo svg {{
    height: 100%;
    width: auto;
  }}

  .masthead-sep {{
    width: 1px;
    height: 18px;
    background: var(--line-hairline);
  }}

  .masthead-project {{
    font-family: var(--font-heading);
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--ink-black);
  }}

  .masthead-right {{
    display: flex;
    align-items: center;
    gap: 36px;
  }}

  nav.index-nav {{
    display: flex;
    gap: 6px;
  }}

  nav.index-nav a {{
    text-decoration: none;
    font-family: var(--font-heading);
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--ink-muted);
    padding: 6px 14px;
    border-radius: 999px;
    transition: color 0.15s ease, background 0.15s ease;
  }}

  nav.index-nav a:hover {{
    color: var(--ink-black);
    background: var(--bg-surface-subtle);
  }}

  .curation-counter {{
    font-family: var(--font-heading);
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--ink-muted);
  }}

  /* Page Wrapper */
  .editorial-wrapper {{
    max-width: 1680px;
    margin: 0 auto;
    padding: 0 64px;
  }}

  /* Hero Section */
  .hero-section {{
    padding: 80px 0 64px;
    border-bottom: 1px solid var(--line-hairline);
  }}

  .hero-top-row {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 28px;
    flex-wrap: wrap;
    gap: 16px;
  }}

  .editorial-badge {{
    font-family: var(--font-heading);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--ink-black);
    background: var(--bg-surface-subtle);
    padding: 5px 14px;
    border-radius: 999px;
  }}

  .hero-meta-grid {{
    display: flex;
    gap: 40px;
    font-size: 13px;
    color: var(--ink-muted);
  }}

  .hero-meta-col {{
    display: flex;
    flex-direction: column;
    gap: 2px;
  }}

  .meta-col-label {{
    font-family: var(--font-heading);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--ink-faint);
  }}

  .meta-col-val {{
    font-family: var(--font-body);
    font-size: 13px;
    font-weight: 500;
    color: var(--ink-charcoal);
  }}

  h1.hero-headline {{
    font-family: var(--font-heading);
    font-size: clamp(40px, 5vw, 76px);
    font-weight: 500;
    letter-spacing: -0.025em;
    line-height: 1.02;
    color: var(--ink-black);
    margin-bottom: 16px;
  }}

  p.hero-deck {{
    font-size: clamp(16px, 1.3vw, 21px);
    font-weight: 400;
    color: var(--ink-muted);
    max-width: 980px;
    line-height: 1.45;
  }}

  /* Chapter Section */
  section.chapter {{
    padding-top: 80px;
  }}

  .chapter-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding-bottom: 24px;
    border-bottom: 1px solid var(--ink-black);
    margin-bottom: 56px;
    flex-wrap: wrap;
    gap: 16px;
  }}

  .chapter-number-title {{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}

  .chapter-number {{
    font-family: var(--font-heading);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--ink-faint);
  }}

  h2.chapter-title {{
    font-family: var(--font-heading);
    font-size: 26px;
    font-weight: 500;
    letter-spacing: -0.01em;
    color: var(--ink-black);
  }}

  .chapter-scope {{
    font-size: 14px;
    color: var(--ink-muted);
    max-width: 580px;
  }}

  /* Venue Editorial Unit — Completely Borderless, Flowing on Canvas */
  article.venue-unit {{
    margin-bottom: 96px;
    padding-bottom: 48px;
    border-bottom: 1px solid var(--line-light);
  }}

  article.venue-unit:last-child {{
    margin-bottom: 40px;
    border-bottom: none;
  }}

  .venue-headline-bar {{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--line-hairline);
    margin-bottom: 18px;
    flex-wrap: wrap;
    gap: 16px;
  }}

  .venue-identification {{
    display: flex;
    align-items: baseline;
    gap: 16px;
    flex-wrap: wrap;
  }}

  h3.venue-title {{
    font-family: var(--font-heading);
    font-size: 22px;
    font-weight: 600;
    letter-spacing: -0.01em;
    color: var(--ink-black);
  }}

  .venue-district {{
    font-size: 13px;
    color: var(--ink-muted);
    letter-spacing: 0.02em;
  }}

  .status-pill {{
    display: inline-flex;
    align-items: center;
    padding: 3px 10px;
    border-radius: 999px;
    font-family: var(--font-heading);
    font-size: 9.5px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }}

  .status-pill.confirmed {{
    background: var(--pill-green-bg);
    color: var(--pill-green-text);
  }}
  .status-pill.optioned {{
    background: var(--pill-amber-bg);
    color: var(--pill-amber-text);
  }}
  .status-pill.available {{
    background: var(--pill-neutral-bg);
    color: var(--pill-neutral-text);
  }}

  .venue-transit-metrics {{
    display: flex;
    align-items: baseline;
    gap: 16px;
  }}

  .transit-time {{
    font-family: var(--font-heading);
    font-size: 14px;
    font-weight: 600;
    color: var(--ink-black);
    letter-spacing: 0.02em;
  }}

  .transit-dist {{
    font-size: 13px;
    color: var(--ink-muted);
  }}

  p.venue-curation-text {{
    font-size: 14px;
    color: var(--ink-charcoal);
    max-width: 1040px;
    line-height: 1.5;
    margin-bottom: 22px;
  }}

  /* Pixieset Gallery — Organic Masonry & Asymmetric Rhythm */
  .pixieset-mosaic {{
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: 12px;
  }}

  .mosaic-cell {{
    position: relative;
    overflow: hidden;
    background: var(--bg-surface-subtle);
    cursor: zoom-in;
  }}

  .mosaic-cell img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
  }}

  .mosaic-cell:hover img {{
    transform: scale(1.02);
    opacity: 0.95;
  }}

  .cell-caption {{
    position: absolute;
    bottom: 12px;
    left: 14px;
    font-family: var(--font-heading);
    font-size: 10px;
    font-weight: 500;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #FFFFFF;
    background: rgba(15, 15, 15, 0.65);
    backdrop-filter: blur(8px);
    padding: 3px 8px;
    border-radius: 2px;
    pointer-events: none;
    opacity: 0;
    transform: translateY(4px);
    transition: all 0.25s ease;
  }}

  .mosaic-cell:hover .cell-caption {{
    opacity: 1;
    transform: translateY(0);
  }}

  /* Asymmetric Cell Spans */
  .mosaic-cell.span-7 {{
    grid-column: span 7;
    height: 480px;
  }}
  .mosaic-cell.span-5 {{
    grid-column: span 5;
    height: 480px;
  }}
  .mosaic-cell.span-4 {{
    grid-column: span 4;
    height: 330px;
  }}
  .mosaic-cell.span-8 {{
    grid-column: span 8;
    height: 330px;
  }}
  .mosaic-cell.span-6 {{
    grid-column: span 6;
    height: 380px;
  }}

  /* Lightbox Modal */
  .lightbox-modal {{
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(15, 15, 15, 0.96);
    backdrop-filter: blur(16px);
    z-index: 1000;
    justify-content: center;
    align-items: center;
    padding: 48px;
  }}

  .lightbox-modal.active {{
    display: flex;
  }}

  .lightbox-content {{
    max-width: 90vw;
    max-height: 88vh;
    object-fit: contain;
    box-shadow: 0 24px 64px rgba(0, 0, 0, 0.8);
  }}

  .lightbox-close {{
    position: absolute;
    top: 28px;
    right: 36px;
    color: #FFFFFF;
    font-size: 30px;
    cursor: pointer;
    background: none;
    border: none;
    opacity: 0.7;
    transition: opacity 0.2s;
    font-family: var(--font-heading);
    font-weight: 300;
  }}
  .lightbox-close:hover {{
    opacity: 1;
  }}

  /* Editorial Footer */
  footer.editorial-footer {{
    margin-top: 100px;
    padding-top: 32px;
    border-top: 1px solid var(--line-hairline);
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 11px;
    color: var(--ink-muted);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-family: var(--font-heading);
  }}

  @media (max-width: 1024px) {{
    header.masthead {{ padding: 16px 32px; }}
    .editorial-wrapper {{ padding: 0 32px; }}
    .mosaic-cell.span-7, .mosaic-cell.span-5, .mosaic-cell.span-6, .mosaic-cell.span-8, .mosaic-cell.span-4 {{
      grid-column: span 6;
      height: 300px;
    }}
  }}

  @media (max-width: 768px) {{
    header.masthead {{ padding: 14px 20px; }}
    .editorial-wrapper {{ padding: 0 20px; }}
    .mosaic-cell.span-7, .mosaic-cell.span-5, .mosaic-cell.span-6, .mosaic-cell.span-8, .mosaic-cell.span-4 {{
      grid-column: span 12;
      height: 250px;
    }}
    .masthead-right {{ display: none; }}
    .hero-meta-grid {{ flex-direction: column; gap: 14px; }}
  }}
</style>
</head>
<body>

  <!-- Masthead Bar -->
  <header class="masthead">
    <div class="masthead-left">
      <div class="hawai-logo">{hawai_logo_svg}</div>
      <div class="masthead-sep"></div>
      <div class="masthead-project">{spec.get('project')}</div>
    </div>
    <div class="masthead-right">
      <nav class="index-nav">
        <a href="#warm-wood">01 Traditional Wood</a>
        <a href="#architectural-olympic">02 Brutalist &amp; Olympic</a>
        <a href="#polyvalent-white">03 White Polyvalent</a>
      </nav>
      <div class="curation-counter">16 Venues · 64 Plates</div>
    </div>
  </header>

  <div class="editorial-wrapper">

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-top-row">
        <span class="editorial-badge">Location Moodboard · Madrid 2026</span>
        <div class="hero-meta-grid">
          <div class="hero-meta-col">
            <span class="meta-col-label">Client</span>
            <span class="meta-col-val">{spec.get('client')}</span>
          </div>
          <div class="hero-meta-col">
            <span class="meta-col-label">Shoot Dates</span>
            <span class="meta-col-val">{spec.get('shoot_dates')}</span>
          </div>
          <div class="hero-meta-col">
            <span class="meta-col-label">Transit Origin</span>
            <span class="meta-col-val">{spec.get('origin')}</span>
          </div>
        </div>
      </div>
      <h1 class="hero-headline">{spec.get('title')}</h1>
      <p class="hero-deck">{spec.get('subtitle')}</p>
    </section>

    <!-- Content Sections -->
    <main>
"""

# Dynamic rhythm styles for 4 images
rhythms = [
    ["span-7", "span-5", "span-4", "span-8"],
    ["span-5", "span-7", "span-8", "span-4"],
    ["span-6", "span-6", "span-7", "span-5"]
]

for cat in categories_data:
    html_template += f"""
    <section class="chapter" id="{cat['id']}">
      <div class="chapter-header">
        <div class="chapter-number-title">
          <span class="chapter-number">{cat['label'].split('/')[0].strip()}</span>
          <h2 class="chapter-title">{cat['label'].split('/')[-1].strip()}</h2>
        </div>
        <p class="chapter-scope">{cat['desc']}</p>
      </div>
    """

    v_counter = 0
    for v in cat['venues']:
        rhythm = rhythms[v_counter % len(rhythms)]
        v_counter += 1

        html_template += f"""
        <article class="venue-unit" id="venue-{v['id']}">
          <div class="venue-headline-bar">
            <div class="venue-identification">
              <h3 class="venue-title">{v['name']}</h3>
              <span class="venue-district">{v['location']}</span>
              <span class="status-pill {v['tag_class']}">{v['tag']}</span>
            </div>
            <div class="venue-transit-metrics">
              <span class="transit-time">{v['drive_time']}</span>
              <span class="transit-dist">{v['distance']}</span>
            </div>
          </div>
          <p class="venue-curation-text">{v['notes']}</p>
          <div class="pixieset-mosaic">
        """

        for idx, img in enumerate(v['images']):
            span_cls = rhythm[idx % len(rhythm)]
            html_template += f"""
            <div class="mosaic-cell {span_cls}" onclick="openLightbox(this)">
              <img src="{img['src']}" alt="{v['name']} plate {idx+1}" loading="lazy">
              <span class="cell-caption">Plate {idx+1:02d}</span>
            </div>
            """

        html_template += """
          </div>
        </article>
        """

    html_template += """
    </section>
    """

html_template += f"""
    </main>

    <!-- Editorial Footer -->
    <footer class="editorial-footer">
      <div>HAWAI FILMS · {spec.get('curated_by')}</div>
      <div>ADIDAS × TMC · RM125 TATAMIS · CONFIDENTIAL PRODUCTION MATERIAL</div>
    </footer>

  </div>

  <!-- Fullscreen Modal Lightbox -->
  <div class="lightbox-modal" id="lightboxModal" onclick="closeLightbox(event)">
    <button class="lightbox-close" onclick="closeLightbox(event)">&times;</button>
    <img class="lightbox-content" id="lightboxImg" src="" alt="Enlarged Plate">
  </div>

  <script>
    function openLightbox(el) {{
      const img = el.querySelector('img');
      if (!img) return;
      const modal = document.getElementById('lightboxModal');
      const modalImg = document.getElementById('lightboxImg');
      modalImg.src = img.src;
      modal.classList.add('active');
    }}

    function closeLightbox(e) {{
      if (e.target.id === 'lightboxModal' || e.target.classList.contains('lightbox-close')) {{
        document.getElementById('lightboxModal').classList.remove('active');
      }}
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        document.getElementById('lightboxModal').classList.remove('active');
      }}
    }});
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated {OUTPUT_HTML} ({os.path.getsize(OUTPUT_HTML) / (1024*1024):.2f} MB)")
