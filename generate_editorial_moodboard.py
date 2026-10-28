import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(ROOT, "assets")
OUTPUT_HTML = os.path.join(ROOT, "tatami_moodboard.html")
LOGO_PATH = os.path.join(ROOT, "hawai_logo.svg")

hawai_logo_svg = ""
if os.path.exists(LOGO_PATH):
    with open(LOGO_PATH, "r", encoding="utf-8") as f:
        hawai_logo_svg = f.read().strip()

# LOCATION SHORTLIST (9 Tatamis/Dojos + 3 White Spaces)
venues_catalog = [
    # 01 / WARM WOOD & TRADITIONAL DOJOS (TURPIN PREFERRED ORDER)
    {
        "category": "warm-wood",
        "cat_num": "01",
        "cat_title": "Traditional Dojos & Martial Arts",
        "cat_desc": "Curated martial arts facilities and authentic timber tatami dojos in Madrid.",
        "id": "las-encinas",
        "folder": "Encinas",
        "name": "Las Encinas de Boadilla",
        "tag": "PRIORITY · MULTI-SPACE",
        "tag_class": "available",
        "location": "Boadilla del Monte · Madrid",
        "distance": "~32.2 km from Valdebebas",
        "drive_time": "~45–50 min driving",
        "notes": "Private sports club complex with dedicated martial arts tatami rooms and specialized fencing pistes."
    },
    {
        "category": "warm-wood",
        "cat_num": "01",
        "cat_title": "Traditional Dojos & Martial Arts",
        "cat_desc": "Curated martial arts facilities and authentic timber tatami dojos in Madrid.",
        "id": "csd-car",
        "folder": "CSD",
        "name": "CSD (CAR Madrid)",
        "tag": "PRIORITY · MULTI-SPACE",
        "tag_class": "available",
        "location": "C/ Pintor el Greco, 1 (Moncloa) · Madrid",
        "distance": "~14.7 km from Valdebebas",
        "drive_time": "~24 min driving",
        "notes": "National elite training center (Consejo Superior de Deportes). Multi-space: Specifically prioritized for Gimnasia Rítmica and adjacent training hall."
    },
    {
        "category": "warm-wood",
        "cat_num": "01",
        "cat_title": "Traditional Dojos & Martial Arts",
        "cat_desc": "Curated martial arts facilities and authentic timber tatami dojos in Madrid.",
        "id": "principe-asturias",
        "folder": "Principe de Asturias",
        "name": "Polideportivo Príncipe de Asturias",
        "tag": "PRIORITY · MULTI-SPACE",
        "tag_class": "available",
        "location": "Madrid",
        "distance": "~16.0 km from Valdebebas",
        "drive_time": "~25 min driving",
        "notes": "Monumental indoor sports pavilion with extensive polished wood sports parquet, perimeter bleachers, and high ceiling clearance."
    },
    {
        "category": "warm-wood",
        "cat_num": "01",
        "cat_title": "Traditional Dojos & Martial Arts",
        "cat_desc": "Curated martial arts facilities and authentic timber tatami dojos in Madrid.",
        "id": "santiago-apostol",
        "folder": "Complejo Deportivo Santiago Apostol",
        "name": "Complejo Deportivo Santiago Apóstol",
        "tag": "PRIORITY · MULTI-SPACE",
        "tag_class": "available",
        "location": "Villanueva de la Cañada · Madrid",
        "distance": "~44.2 km from Valdebebas",
        "drive_time": "~60–65 min driving",
        "notes": "Multi-space sports complex featuring dedicated tatami and fencing rooms."
    },
    {
        "category": "warm-wood",
        "cat_num": "01",
        "cat_title": "Traditional Dojos & Martial Arts",
        "cat_desc": "Curated martial arts facilities and authentic timber tatami dojos in Madrid.",
        "id": "puerta-hierro",
        "folder": "Puerta de Hierro",
        "name": "Parque Deportivo Puerta de Hierro",
        "tag": "PRIORITY · BRUTALIST",
        "tag_class": "optioned",
        "location": "Ctra. de El Pardo, km 1 · Madrid",
        "distance": "~15.7 km from Valdebebas",
        "drive_time": "~25 min driving",
        "notes": "Standout brutalist exposed raw concrete sports pavilion with tatami mats. Note: Municipal administrative permit lead time is lengthy; subject to immediate feasibility confirmation."
    },
    {
        "category": "warm-wood",
        "cat_num": "01",
        "cat_title": "Traditional Dojos & Martial Arts",
        "cat_desc": "Curated martial arts facilities and authentic timber tatami dojos in Madrid.",
        "id": "shotokan",
        "folder": "Shotokan Honbu Dojo",
        "name": "Shotokan Honbu Dojo",
        "tag": "PRIORITY · MULTI-SPACE",
        "tag_class": "confirmed",
        "location": "Chamartín / Prosperidad · Madrid",
        "distance": "~8.0 km from Valdebebas",
        "drive_time": "~15 min driving",
        "notes": "Authentic Japanese karate dojo. Multi-space configuration with warm timber perimeter lattice, clean tatami flooring, and warm directional ambient light."
    },
    {
        "category": "warm-wood",
        "cat_num": "01",
        "cat_title": "Traditional Dojos & Martial Arts",
        "cat_desc": "Curated martial arts facilities and authentic timber tatami dojos in Madrid.",
        "id": "cc-ejercitos",
        "folder": "CC Ejércitos",
        "name": "CC Ejércitos (Club de Esgrima)",
        "tag": "PRIORITY · MULTI-SPACE",
        "tag_class": "confirmed",
        "location": "Gran Vía, 13 (Centro) · Madrid",
        "distance": "~13.5 km from Valdebebas",
        "drive_time": "~22 min driving",
        "notes": "Stately historic palace. Stained wood herringbone parquets, classical moldings, monumental ceiling heights. Multi-space: Sala de Esgrima, Gimnasio, and Sala de Baile."
    },
    {
        "category": "warm-wood",
        "cat_num": "01",
        "cat_title": "Traditional Dojos & Martial Arts",
        "cat_desc": "Curated martial arts facilities and authentic timber tatami dojos in Madrid.",
        "id": "zanshin",
        "folder": "Zanshin Madrid",
        "name": "Zanshin Madrid",
        "tag": "PRIORITY · 1 SPACE",
        "tag_class": "confirmed",
        "location": "C/ Clara del Rey, Chamartín · Madrid",
        "distance": "~8.9 km from Valdebebas",
        "drive_time": "~16 min driving",
        "notes": "Minimalist Japanese martial arts studio. Warm wood wall paneling, clean tatami configuration, high ceiling clearance."
    },
    {
        "category": "warm-wood",
        "cat_num": "01",
        "cat_title": "Traditional Dojos & Martial Arts",
        "cat_desc": "Curated martial arts facilities and authentic timber tatami dojos in Madrid.",
        "id": "dojo-shubukan",
        "folder": "Dojo Shubukan",
        "name": "Dojo Shubukan",
        "tag": "NEW · TRADITIONAL TATAMI",
        "tag_class": "confirmed",
        "location": "C/ de los Yébenes, 98 (Aluche) · Madrid",
        "distance": "~18.2 km from Valdebebas",
        "drive_time": "~26 min driving",
        "notes": "Dedicated Japanese martial arts dojo with authentic tatami flooring, traditional shoji wooden partitions, and atmospheric lighting."
    },

    # 02 / WHITE & POLYVALENT SPACES
    {
        "category": "white-polyvalent",
        "cat_num": "02",
        "cat_title": "White & Polyvalent Spaces",
        "cat_desc": "Curated white and daylight architectural spaces for custom set design and spatial intervention.",
        "id": "invernadero-penotes",
        "folder": "Invernadero los Peñotes",
        "name": "Invernadero Los Peñotes",
        "tag": "SELECTED · GLASSHOUSE",
        "tag_class": "confirmed",
        "location": "Alcobendas · Madrid",
        "distance": "~9.5 km from Valdebebas",
        "drive_time": "~14 min driving",
        "notes": "Botanical glasshouse venue with natural overhead light and architectural steel frames. Closest polyvalent space to Valdebebas."
    },
    {
        "category": "white-polyvalent",
        "cat_num": "02",
        "cat_title": "White & Polyvalent Spaces",
        "cat_desc": "Curated white and daylight architectural spaces for custom set design and spatial intervention.",
        "id": "plato-who",
        "folder": "Who Espacio Creativo",
        "name": "Plató Who (Who Espacio Creativo)",
        "tag": "SELECTED · ARCHITECTURAL",
        "tag_class": "available",
        "location": "Madrid Centro",
        "distance": "~12.0 km from Valdebebas",
        "drive_time": "~20 min driving",
        "notes": "Contemporary architectural creative space. Warm timber accents, light floors, abundant natural soft daylight across open-plan spans."
    },
    {
        "category": "white-polyvalent",
        "cat_num": "02",
        "cat_title": "White & Polyvalent Spaces",
        "cat_desc": "Curated white and daylight architectural spaces for custom set design and spatial intervention.",
        "id": "espacio-larra",
        "folder": "Espacio Larra",
        "name": "Espacio Larra (Larra 14)",
        "tag": "SELECTED · PLATÓ",
        "tag_class": "confirmed",
        "location": "C/ de Larra, 14 (Chamberí) · Madrid",
        "distance": "~12.7 km from Valdebebas",
        "drive_time": "~21 min driving",
        "notes": "Historic editorial building. Pristine white cyclorama Plató, grand skylit central atrium, raw gallery spaces, and auditorium."
    },
    {
        "category": "white-polyvalent",
        "cat_num": "02",
        "cat_title": "White & Polyvalent Spaces",
        "cat_desc": "Curated white and daylight architectural spaces for custom set design and spatial intervention.",
        "id": "espacio-abc",
        "folder": "Espacio ABC",
        "name": "Espacio ABC",
        "tag": "SELECTED · EVENT STAGE",
        "tag_class": "available",
        "location": "C/ Serrano, 61 (Salamanca) · Madrid",
        "distance": "~11.5 km from Valdebebas",
        "drive_time": "~18 min driving",
        "notes": "Premium venue in ABC Serrano with polished architectural finishes and daylight atriums."
    }
]

total_images = 0
categories_grouped = {}
THUMBS_DIR = os.path.join(ROOT, "assets_thumbs")

for v in venues_catalog:
    v_folder = os.path.join(ASSETS_DIR, v["folder"])
    thumb_v_folder = os.path.join(THUMBS_DIR, v["folder"])
    images = []
    if os.path.exists(v_folder):
        files = sorted([f for f in os.listdir(v_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png')) and not f.startswith('._')])
        for f in files:
            orig_rel = f"assets/{v['folder']}/{f}"
            base_name = os.path.splitext(f)[0]
            thumb_file = f"{base_name}.webp"
            thumb_abs = os.path.join(thumb_v_folder, thumb_file)
            if os.path.exists(thumb_abs):
                thumb_rel = f"assets_thumbs/{v['folder']}/{thumb_file}"
            else:
                thumb_rel = orig_rel
            images.append({
                "orig": orig_rel,
                "thumb": thumb_rel
            })
    v["images"] = images
    total_images += len(images)
    
    cat_id = v["category"]
    if cat_id not in categories_grouped:
        categories_grouped[cat_id] = {
            "num": v["cat_num"],
            "title": v["cat_title"],
            "desc": v["cat_desc"],
            "venues": []
        }
    categories_grouped[cat_id]["venues"].append(v)

print(f"Shortlist catalog ready: {len(venues_catalog)} venues, {total_images} total images linked.")

sidebar_nav_html = ""
for cat_id, cat_data in categories_grouped.items():
    cat_venues = cat_data['venues']
    sidebar_nav_html += f"""
    <div class="sidebar-section">
      <div class="sidebar-section-header">
        <div class="sidebar-section-label">
          <span class="section-badge-num">{cat_data['num']}</span>
          <span class="section-badge-title">{cat_data['title']}</span>
        </div>
        <span class="section-badge-count">{len(cat_venues)}</span>
      </div>
      <div class="sidebar-items-list">
    """
    for idx_v, v in enumerate(cat_venues):
        primary_tag = v['tag'].split('·')[0].strip()
        is_priority = 'PRIORITY' in v['tag'].upper()
        p_dot = '<span class="priority-dot" title="Priority Check"></span>' if is_priority else ''
        sidebar_nav_html += f"""
        <a href="#venue-{v['id']}" class="sidebar-item" data-venue-target="venue-{v['id']}">
          <div class="sidebar-item-main">
            <span class="sidebar-item-num">{idx_v+1:02d}</span>
            <div class="sidebar-item-text-group">
              <div class="sidebar-item-title-row">
                <span class="sidebar-item-name">{v['name']}</span>
                {p_dot}
              </div>
              <div class="sidebar-item-meta">
                <span class="sidebar-item-tag">{primary_tag}</span>
                <span class="sidebar-item-time">{v['drive_time'].replace('driving', '').strip()}</span>
              </div>
            </div>
          </div>
        </a>
        """
    sidebar_nav_html += """
      </div>
    </div>
    """

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TMC × TATAMIS · ADIDAS RM125 · LOCATION MOODBOARD</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg-page: #F9F5E9;
    --bg-surface-subtle: #F2EDE0;
    --bg-card: #FAF6EC;
    
    --ink-black: #0F0F0F;
    --ink-charcoal: #2A2A2A;
    --ink-muted: #737373;
    --ink-faint: #999999;

    --line-hairline: rgba(15, 15, 15, 0.12);
    --line-light: rgba(15, 15, 15, 0.06);

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

  /* Masthead — Editorial Top Bar */
  header.masthead {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(249, 245, 233, 0.96);
    backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--line-hairline);
    padding: 16px 56px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .masthead-left {{
    display: flex;
    align-items: center;
    gap: 20px;
  }}

  .hawai-logo {{
    height: 18px;
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
    height: 16px;
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
    gap: 28px;
  }}

  nav.index-nav {{
    display: flex;
    gap: 6px;
  }}

  nav.index-nav a {{
    text-decoration: none;
    font-family: var(--font-heading);
    font-size: 10.5px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--ink-muted);
    padding: 6px 12px;
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

  /* App Layout: Left Sidebar + Main Content */
  .app-layout {{
    display: flex;
    min-height: calc(100vh - 57px);
  }}

  /* Left Side Navigation Panel */
  aside.location-sidebar {{
    width: 320px;
    flex-shrink: 0;
    position: sticky;
    top: 57px;
    height: calc(100vh - 57px);
    overflow-y: auto;
    border-right: 1px solid var(--line-hairline);
    background: var(--bg-surface-subtle);
    display: flex;
    flex-direction: column;
    z-index: 80;
    scrollbar-width: thin;
    scrollbar-color: rgba(15, 15, 15, 0.15) transparent;
  }}

  .sidebar-header {{
    padding: 24px 26px 18px;
    border-bottom: 1px solid var(--line-hairline);
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: var(--bg-card);
  }}

  .sidebar-title {{
    font-family: var(--font-heading);
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--ink-black);
  }}

  .sidebar-count {{
    font-family: var(--font-heading);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.06em;
    color: var(--ink-muted);
  }}

  .sidebar-nav {{
    padding: 8px 0 40px;
    flex: 1;
  }}

  .sidebar-section {{
    margin-bottom: 16px;
  }}

  .sidebar-section-header {{
    padding: 18px 26px 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  .sidebar-section-label {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .section-badge-num {{
    font-family: var(--font-heading);
    font-size: 9px;
    font-weight: 700;
    color: var(--ink-faint);
    letter-spacing: 0.05em;
  }}

  .section-badge-title {{
    font-family: var(--font-heading);
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--ink-charcoal);
  }}

  .section-badge-count {{
    font-family: var(--font-heading);
    font-size: 10px;
    font-weight: 600;
    color: var(--ink-faint);
    background: rgba(15, 15, 15, 0.04);
    padding: 1px 7px;
    border-radius: 999px;
  }}

  .sidebar-items-list {{
    display: flex;
    flex-direction: column;
    gap: 1px;
  }}

  .sidebar-item {{
    display: block;
    padding: 10px 26px;
    text-decoration: none;
    color: var(--ink-charcoal);
    transition: all 0.15s ease;
    border-left: 2px solid transparent;
  }}

  .sidebar-item:hover {{
    background: rgba(15, 15, 15, 0.035);
    color: var(--ink-black);
  }}

  .sidebar-item.active {{
    background: var(--bg-card);
    border-left-color: var(--ink-black);
    box-shadow: 0 2px 8px rgba(15, 15, 15, 0.04);
  }}

  .sidebar-item.active .sidebar-item-name {{
    color: var(--ink-black);
    font-weight: 600;
  }}

  .sidebar-item.active .sidebar-item-num {{
    color: var(--ink-black);
  }}

  .sidebar-item-main {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }}

  .sidebar-item-num {{
    font-family: var(--font-heading);
    font-size: 10px;
    font-weight: 500;
    color: var(--ink-faint);
    letter-spacing: 0.04em;
    padding-top: 2px;
    min-width: 16px;
  }}

  .sidebar-item-text-group {{
    flex: 1;
    min-width: 0;
  }}

  .sidebar-item-title-row {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6px;
    margin-bottom: 3px;
  }}

  .sidebar-item-name {{
    font-size: 13.5px;
    font-weight: 500;
    line-height: 1.3;
    color: var(--ink-charcoal);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }}

  .priority-dot {{
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #1A6B3C;
    flex-shrink: 0;
  }}

  .sidebar-item-meta {{
    font-family: var(--font-heading);
    font-size: 10px;
    color: var(--ink-muted);
    display: flex;
    justify-content: space-between;
    align-items: center;
    letter-spacing: 0.04em;
  }}

  .sidebar-item-tag {{
    text-transform: uppercase;
    font-size: 9px;
    letter-spacing: 0.06em;
    color: var(--ink-faint);
  }}

  .sidebar-item-time {{
    color: var(--ink-muted);
    font-weight: 500;
  }}

  .masthead-origin-badge {{
    font-family: var(--font-heading);
    font-size: 10.5px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--ink-muted);
    background: var(--bg-surface-subtle);
    padding: 4px 10px;
    border-radius: 999px;
  }}

  /* Page Wrapper */
  .editorial-wrapper {{
    flex: 1;
    min-width: 0;
    max-width: 1540px;
    margin: 0 auto;
    padding: 0 48px;
  }}

  /* Hero Section */
  .hero-section {{
    padding: 72px 0 64px;
    border-bottom: 1px solid var(--line-hairline);
    margin-bottom: 32px;
  }}

  .hero-top-row {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 24px;
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
    gap: 36px;
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
    font-size: clamp(38px, 4.5vw, 70px);
    font-weight: 500;
    letter-spacing: -0.025em;
    line-height: 1.02;
    color: var(--ink-black);
    margin-bottom: 14px;
  }}

  p.hero-deck {{
    font-size: clamp(15px, 1.2vw, 19px);
    font-weight: 400;
    color: var(--ink-muted);
    max-width: 960px;
    line-height: 1.45;
  }}



  /* Chapter Section */
  section.chapter {{
    padding-top: 64px;
  }}

  .chapter-header {{
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding-bottom: 20px;
    border-bottom: 1px solid var(--ink-black);
    margin-bottom: 64px;
    flex-wrap: wrap;
    gap: 16px;
  }}

  .chapter-number-title {{
    display: flex;
    flex-direction: column;
    gap: 4px;
  }}

  .chapter-number {{
    font-family: var(--font-heading);
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--ink-faint);
  }}

  h2.chapter-title {{
    font-family: var(--font-heading);
    font-size: 24px;
    font-weight: 500;
    letter-spacing: -0.01em;
    color: var(--ink-black);
  }}

  .chapter-scope {{
    font-size: 13.5px;
    color: var(--ink-muted);
    max-width: 580px;
  }}

  /* Venue Card Unit — Separate Warm Surface, Tight Integrated Details */
  article.venue-unit {{
    background: var(--bg-card);
    border-top: 2px solid var(--ink-black);
    padding: 36px 40px 48px;
    margin-bottom: 96px;
    scroll-margin-top: 76px;
  }}

  .venue-lead-row {{
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding-bottom: 22px;
    border-bottom: 1px solid var(--line-hairline);
    margin-bottom: 28px;
    flex-wrap: wrap;
    gap: 24px;
  }}

  .venue-left-block {{
    display: flex;
    flex-direction: column;
    gap: 6px;
    max-width: 620px;
  }}

  .venue-title-meta {{
    display: flex;
    align-items: baseline;
    gap: 14px;
    flex-wrap: wrap;
  }}

  h3.venue-title {{
    font-family: var(--font-heading);
    font-size: 26px;
    font-weight: 600;
    letter-spacing: -0.015em;
    color: var(--ink-black);
    line-height: 1.15;
  }}

  .venue-district {{
    font-size: 13px;
    color: var(--ink-muted);
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

  p.venue-curation-text {{
    font-size: 14px;
    color: var(--ink-charcoal);
    line-height: 1.45;
    margin-top: 4px;
  }}

  /* Compact Transit Specs Column (No Wasted Space) */
  .venue-specs-column {{
    display: flex;
    gap: 28px;
    background: rgba(242, 237, 224, 0.6);
    padding: 14px 22px;
    border-radius: 4px;
    align-self: flex-start;
  }}

  .spec-item {{
    display: flex;
    flex-direction: column;
    gap: 1px;
  }}

  .spec-label {{
    font-family: var(--font-heading);
    font-size: 9.5px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--ink-faint);
  }}

  .spec-val-primary {{
    font-family: var(--font-heading);
    font-size: 15px;
    font-weight: 600;
    color: var(--ink-black);
    letter-spacing: 0.02em;
  }}

  .spec-val-secondary {{
    font-size: 12px;
    color: var(--ink-muted);
  }}

  /* Dynamic Pixieset Grid with Masonry Pacing */
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
    transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s ease;
  }}

  .mosaic-cell:hover img {{
    transform: scale(1.02);
    opacity: 0.95;
  }}

  .cell-caption {{
    position: absolute;
    bottom: 10px;
    left: 12px;
    font-family: var(--font-heading);
    font-size: 9.5px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #FFFFFF;
    background: rgba(15, 15, 15, 0.7);
    backdrop-filter: blur(8px);
    padding: 3px 8px;
    border-radius: 2px;
    pointer-events: none;
    opacity: 0;
    transform: translateY(4px);
    transition: all 0.2s ease;
  }}

  .mosaic-cell:hover .cell-caption {{
    opacity: 1;
    transform: translateY(0);
  }}

  /* Asymmetric Layout Classes */
  .mosaic-cell.hero-large {{
    grid-column: span 8;
    height: 480px;
  }}
  .mosaic-cell.hero-side {{
    grid-column: span 4;
    height: 480px;
  }}
  .mosaic-cell.quad-cell {{
    grid-column: span 4;
    height: 330px;
  }}
  .mosaic-cell.half-cell {{
    grid-column: span 6;
    height: 380px;
  }}
  .mosaic-cell.trio-cell {{
    grid-column: span 3;
    height: 260px;
  }}

  /* Lightbox Modal */
  .lightbox-modal {{
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(15, 15, 15, 0.97);
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
    max-width: 92vw;
    max-height: 90vh;
    object-fit: contain;
    box-shadow: 0 24px 64px rgba(0, 0, 0, 0.85);
  }}

  .lightbox-close {{
    position: absolute;
    top: 28px;
    right: 36px;
    color: #FFFFFF;
    font-size: 32px;
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



  /* Footer */
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

  @media (max-width: 1200px) {{
    .mosaic-cell.hero-large, .mosaic-cell.hero-side, .mosaic-cell.half-cell, .mosaic-cell.quad-cell {{
      grid-column: span 6;
      height: 320px;
    }}
    .mosaic-cell.trio-cell {{
      grid-column: span 4;
      height: 240px;
    }}
  }}

  @media (max-width: 1024px) {{
    aside.location-sidebar {{
      display: none;
    }}
    .editorial-wrapper {{
      padding: 0 32px;
    }}
  }}

  @media (max-width: 768px) {{
    header.masthead {{ padding: 14px 24px; }}
    .editorial-wrapper {{ padding: 0 20px; }}
    
    article.venue-unit {{ padding: 24px 18px 36px; }}
    .venue-lead-row {{ flex-direction: column; gap: 18px; }}
    .venue-specs-column {{ width: 100%; justify-content: space-between; }}
    .mosaic-cell.hero-large, .mosaic-cell.hero-side, .mosaic-cell.half-cell, .mosaic-cell.quad-cell, .mosaic-cell.trio-cell {{
      grid-column: span 12;
      height: 260px;
    }}
    .masthead-right {{ display: none; }}
    .hero-meta-grid {{ flex-direction: column; gap: 14px; }}
  }}

  /* Curation Mode Floating Tool Bar */
  .curate-toolbar {{
    position: fixed;
    top: 14px;
    right: 48px;
    z-index: 120;
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .curate-btn {{
    font-family: var(--font-heading);
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 7px 14px;
    border-radius: 999px;
    cursor: pointer;
    border: 1px solid var(--line-hairline);
    background: var(--bg-card);
    color: var(--ink-charcoal);
    box-shadow: 0 4px 16px rgba(15, 15, 15, 0.08);
    transition: all 0.15s ease;
  }}

  .curate-btn:hover {{
    background: var(--bg-surface-subtle);
    color: var(--ink-black);
  }}

  .curate-btn.active {{
    background: #E53935;
    color: #FFFFFF;
    border-color: #D32F2F;
  }}

  .delete-badge {{
    position: absolute;
    top: 8px;
    right: 8px;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: rgba(15, 15, 15, 0.55);
    backdrop-filter: blur(8px);
    border: 1.5px solid rgba(255, 255, 255, 0.7);
    color: #FFFFFF;
    display: none;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    cursor: pointer;
    z-index: 10;
    transition: all 0.15s ease;
  }}

  body.curate-active .delete-badge {{
    display: flex;
  }}

  .mosaic-cell.marked-for-removal {{
    opacity: 0.25;
    filter: grayscale(1);
  }}

  .mosaic-cell.marked-for-removal .delete-badge {{
    background: #E53935;
    border-color: #FFFFFF;
    color: #FFFFFF;
  }}

  .curate-status-pill {{
    display: none;
    font-family: var(--font-heading);
    font-size: 11px;
    font-weight: 600;
    color: #FFFFFF;
    background: #111111;
    padding: 6px 14px;
    border-radius: 999px;
  }}

  body.curate-active .curate-status-pill {{
    display: inline-block;
  }}

</style>
</head>
<body>



  <!-- Masthead Bar -->
  <header class="masthead">
    <div class="masthead-left">
      <div class="hawai-logo">{hawai_logo_svg}</div>
      <div class="masthead-sep"></div>
      <div class="masthead-project">TMC × TATAMIS — ADIDAS RM125</div>
    </div>
    <div class="masthead-right">
      <div class="curation-counter">{len(venues_catalog)} Locations · {total_images} Curated Plates</div>
      <div class="masthead-sep"></div>
      <div class="masthead-origin-badge">Origin: Valdebebas</div>
    </div>
  </header>

  <!-- Main App Layout: Sidebar + Editorial Stream -->
  <div class="app-layout">
    
    <!-- Left Side Navigation Panel -->
    <aside class="location-sidebar">
      <div class="sidebar-header">
        <span class="sidebar-title">Locations Directory</span>
        <span class="sidebar-count">{len(venues_catalog)} Venues</span>
      </div>
      <nav class="sidebar-nav">
        {sidebar_nav_html}
      </nav>
    </aside>

    <div class="editorial-wrapper">

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-top-row">
        <span class="editorial-badge">Production Dossier · Location Moodboard</span>
        <div class="hero-meta-grid">
          <div class="hero-meta-col">
            <span class="meta-col-label">Client</span>
            <span class="meta-col-val">TMC / adidas</span>
          </div>
          <div class="hero-meta-col">
            <span class="meta-col-label">Shoot Dates</span>
            <span class="meta-col-val">18–19 November 2026</span>
          </div>
          <div class="hero-meta-col">
            <span class="meta-col-label">Transit Origin</span>
            <span class="meta-col-val">Ciudad Real Madrid (Valdebebas)</span>
          </div>
        </div>
      </div>
      <h1 class="hero-headline">Location Moodboard</h1>
      <p class="hero-deck">Curated location options for client review and feasibility assessment. Features 9 authentic tatamis and martial arts dojos alongside 4 polyvalent white architectural spaces in Madrid.</p>
    </section>



    <!-- Main Categories -->
    <main>
"""

def get_grid_span(idx, total):
    if total <= 4:
        pattern = ["hero-large", "hero-side", "quad-cell", "hero-large"]
        return pattern[idx % len(pattern)]
    elif idx == 0:
        return "hero-large"
    elif idx == 1:
        return "hero-side"
    elif idx in [2, 3, 4]:
        return "quad-cell"
    elif idx in [5, 6]:
        return "half-cell"
    elif idx in [7, 8, 9, 10]:
        return "trio-cell"
    else:
        sub_idx = (idx - 11) % 5
        if sub_idx in [0, 1, 2]:
            return "quad-cell"
        else:
            return "half-cell"

for cat_id, cat_data in categories_grouped.items():
    html_template += f"""
    <section class="chapter" id="{cat_id}" data-category="{cat_id}">
      <div class="chapter-header">
        <div class="chapter-number-title">
          <span class="chapter-number">{cat_data['num']}</span>
          <h2 class="chapter-title">{cat_data['title']}</h2>
        </div>
        <p class="chapter-scope">{cat_data['desc']}</p>
      </div>
    """

    for v in cat_data['venues']:
        num_imgs = len(v['images'])
        search_terms = f"{v['name']} {v['location']} {v['tag']} {v['notes']}".lower()

        html_template += f"""
        <article class="venue-unit" id="venue-{v['id']}" data-category="{v['category']}" data-search="{search_terms}">
          <div class="venue-lead-row">
            <div class="venue-left-block">
              <div class="venue-title-meta">
                <h3 class="venue-title">{v['name']}</h3>
                <span class="status-pill {v['tag_class']}">{v['tag']}</span>
              </div>
              <div class="venue-district">{v['location']}</div>
              <p class="venue-curation-text">{v['notes']}</p>
            </div>
            
            <div class="venue-specs-column">
              <div class="spec-item">
                <span class="spec-label">Drive Time</span>
                <span class="spec-val-primary">{v['drive_time']}</span>
                <span class="spec-val-secondary">from Valdebebas</span>
              </div>
              <div class="spec-item">
                <span class="spec-label">Distance</span>
                <span class="spec-val-primary">{v['distance'].split('from')[0].strip()}</span>
                <span class="spec-val-secondary">orbital route</span>
              </div>
              <div class="spec-item">
                <span class="spec-label">Archive Plates</span>
                <span class="spec-val-primary">{num_imgs}</span>
                <span class="spec-val-secondary">Zafarrancho</span>
              </div>
            </div>
          </div>

          <div class="pixieset-mosaic">
        """

        for idx, img_info in enumerate(v['images']):
            span_cls = get_grid_span(idx, num_imgs)
            html_template += f"""
            <div class="mosaic-cell {span_cls}" onclick="openLightbox(this)">
              <img src="{img_info['thumb']}" data-full="{img_info['orig']}" alt="{v['name']} plate {idx+1}" loading="lazy">
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
      <div>HAWAI FILMS · PRODUCTION &amp; LOCATIONS</div>
      <div>ADIDAS × TMC · RM125 TATAMIS · CONFIDENTIAL PRODUCTION MATERIAL</div>
    </footer>

    </div><!-- /.editorial-wrapper -->
  </div><!-- /.app-layout -->

  <!-- Fullscreen Modal Lightbox -->
  <div class="lightbox-modal" id="lightboxModal" onclick="closeLightbox(event)">
    <button class="lightbox-close" onclick="closeLightbox(event)">&times;</button>
    <img class="lightbox-content" id="lightboxImg" src="" alt="Enlarged Plate">
  </div>

  <script>

    let curationMode = false;
    const selectedForTrash = new Set();

    function toggleCurationMode() {{
      curationMode = !curationMode;
      document.body.classList.toggle('curate-active', curationMode);
      const btn = document.getElementById('toggleCurateBtn');
      btn.classList.toggle('active', curationMode);
      btn.innerText = curationMode ? '✕ Exit Curate' : '✂️ Curate Mode';
      updateCurateUI();
    }}

    function toggleMarkCell(e, badge) {{
      e.stopPropagation();
      const cell = badge.closest('.mosaic-cell');
      const src = cell.getAttribute('data-src');
      if (selectedForTrash.has(src)) {{
        selectedForTrash.delete(src);
        cell.classList.remove('marked-for-removal');
      }} else {{
        selectedForTrash.add(src);
        cell.classList.add('marked-for-removal');
      }}
      updateCurateUI();
    }}

    function handleCellClick(e, cell) {{
      if (curationMode) {{
        const src = cell.getAttribute('data-src');
        if (selectedForTrash.has(src)) {{
          selectedForTrash.delete(src);
          cell.classList.remove('marked-for-removal');
        }} else {{
          selectedForTrash.add(src);
          cell.classList.add('marked-for-removal');
        }}
        updateCurateUI();
      }} else {{
        openLightbox(cell);
      }}
    }}

    function updateCurateUI() {{
      const applyBtn = document.getElementById('applyDeleteBtn');
      const countPill = document.getElementById('curateCount');
      const deleteNum = document.getElementById('deleteNum');
      countPill.innerText = `${{selectedForTrash.size}} marked`;
      deleteNum.innerText = selectedForTrash.size;
      applyBtn.style.display = (curationMode && selectedForTrash.size > 0) ? 'inline-block' : 'none';
    }}

    async function applyBatchRemove() {{
      if (selectedForTrash.size === 0) return;
      const count = selectedForTrash.size;
      if (!confirm(`Are you sure you want to remove and trash ${{count}} images? They will be moved to .trashed_plates safely.`)) {{
        return;
      }}
      try {{
        const res = await fetch('/api/remove-images', {{
          method: 'POST',
          headers: {{'Content-Type': 'application/json'}},
          body: JSON.stringify({{images: Array.from(selectedForTrash)}})
        }});
        const data = await res.json();
        if (data.ok) {{
          alert(`Successfully removed ${{data.removed_count}} images! The moodboard has been automatically regenerated.`);
          location.reload();
        }} else {{
          alert('Error removing images: ' + data.error);
        }}
      }} catch (err) {{
        alert('Could not connect to curation server: ' + err.message);
      }}
    }}

    function openLightbox(el) {{
      const img = el.querySelector('img');
      if (!img) return;
      const modal = document.getElementById('lightboxModal');
      const modalImg = document.getElementById('lightboxImg');
      modalImg.src = img.getAttribute('data-full') || img.src;
      modal.classList.add('active');
    }}

    function closeLightbox(e) {{
      if (e.target.id === 'lightboxModal' || e.target.classList.contains('lightbox-close')) {{
        document.getElementById('lightboxModal').classList.remove('active');
      }}
    }}

    function toggleJumpDrawer(force) {{
      const drawer = document.getElementById('jumpDrawer');
      if (typeof force === 'boolean') {{
        drawer.classList.toggle('active', force);
      }} else {{
        drawer.classList.toggle('active');
      }}
    }}

    document.addEventListener('click', (e) => {{
      const drawer = document.getElementById('jumpDrawer');
      const pill = document.querySelector('.quick-nav-pill');
      if (drawer.classList.contains('active') && !drawer.contains(e.target) && !pill.contains(e.target)) {{
        drawer.classList.remove('active');
      }}
    }});

    function filterCategory(catId, btn) {{
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const chapters = document.querySelectorAll('section.chapter');
      const venues = document.querySelectorAll('article.venue-unit');

      if (catId === 'all') {{
        chapters.forEach(c => c.style.display = 'block');
        venues.forEach(v => v.style.display = 'block');
      }} else {{
        chapters.forEach(c => {{
          if (c.getAttribute('data-category') === catId) {{
            c.style.display = 'block';
          }} else {{
            c.style.display = 'none';
          }}
        }});
        venues.forEach(v => {{
          if (v.getAttribute('data-category') === catId) {{
            v.style.display = 'block';
          }} else {{
            v.style.display = 'none';
          }}
        }});
      }}
    }}

    function handleSearch(term) {{
      term = term.trim().toLowerCase();
      const venues = document.querySelectorAll('article.venue-unit');
      const chapters = document.querySelectorAll('section.chapter');

      if (!term) {{
        const activeFilter = document.querySelector('.filter-btn.active');
        if (activeFilter) {{
          activeFilter.click();
        }}
        return;
      }}

      chapters.forEach(c => c.style.display = 'block');
      venues.forEach(v => {{
        const haystack = v.getAttribute('data-search') || '';
        if (haystack.includes(term)) {{
          v.style.display = 'block';
        }} else {{
          v.style.display = 'none';
        }}
      }});
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        document.getElementById('lightboxModal').classList.remove('active');
      }}
    }});

    // Active state highlighting on scroll
    const venueElements = document.querySelectorAll('article.venue-unit');
    const sidebarLinks = document.querySelectorAll('.sidebar-item');

    const observer = new IntersectionObserver((entries) => {{
      entries.forEach(entry => {{
        if (entry.isIntersecting) {{
          const id = entry.target.id;
          sidebarLinks.forEach(link => {{
            if (link.getAttribute('data-venue-target') === id) {{
              link.classList.add('active');
            }} else {{
              link.classList.remove('active');
            }}
          }});
        }}
      }});
    }}, {{
      rootMargin: '-20% 0px -70% 0px'
    }});

    venueElements.forEach(el => observer.observe(el));
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated {OUTPUT_HTML} successfully!")