import json, os

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(ROOT, "assets")
OUTPUT_HTML = os.path.join(ROOT, "tatami_moodboard.html")
LOGO_PATH = os.path.join(ROOT, "hawai_logo.svg")

hawai_logo_svg = ""
if os.path.exists(LOGO_PATH):
    with open(LOGO_PATH, "r", encoding="utf-8") as f:
        hawai_logo_svg = f.read().strip()

# EXACT TURPIN SHORTLIST (9 Tatamis/Dojos + 3 White Spaces + 1 Wildcard Boetticher)
venues_catalog = [
    # 01 / WARM WOOD & TRADITIONAL DOJOS (TURPIN SHORTLIST)
    {
        "category": "warm-wood",
        "cat_num": "01",
        "cat_title": "Traditional Dojos & Martial Arts (Shortlist)",
        "cat_desc": "Priority martial arts facilities selected by David Turpin for immediate availability check.",
        "id": "puerta-hierro",
        "folder": "Puerta de Hierro",
        "name": "Parque Deportivo Puerta de Hierro",
        "tag": "PRIORITY · BRUTALIST",
        "tag_class": "optioned",
        "location": "Ctra. de El Pardo, km 1 · Madrid",
        "distance": "~15.7 km from Valdebebas",
        "drive_time": "~25 min driving",
        "notes": "Standout brutalist exposed raw concrete sports pavilion with tatami mats. Turpin note: Municipal administrative permit lead time is lengthy; availability & feasibility must be confirmed immediately."
    },
    {
        "category": "warm-wood",
        "cat_num": "01",
        "cat_title": "Traditional Dojos & Martial Arts (Shortlist)",
        "cat_desc": "Priority martial arts facilities selected by David Turpin for immediate availability check.",
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
        "cat_title": "Traditional Dojos & Martial Arts (Shortlist)",
        "cat_desc": "Priority martial arts facilities selected by David Turpin for immediate availability check.",
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
        "cat_title": "Traditional Dojos & Martial Arts (Shortlist)",
        "cat_desc": "Priority martial arts facilities selected by David Turpin for immediate availability check.",
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
        "cat_title": "Traditional Dojos & Martial Arts (Shortlist)",
        "cat_desc": "Priority martial arts facilities selected by David Turpin for immediate availability check.",
        "id": "plato-who",
        "folder": "Who Espacio Creativo",
        "name": "Plató Who (Who Espacio Creativo)",
        "tag": "PRIORITY · MULTI-SPACE",
        "tag_class": "available",
        "location": "Madrid Centro",
        "distance": "~12.0 km from Valdebebas",
        "drive_time": "~20 min driving",
        "notes": "Contemporary architectural creative space. Warm timber accents, light floors, abundant natural soft daylight across open-plan spans."
    },
    {
        "category": "warm-wood",
        "cat_num": "01",
        "cat_title": "Traditional Dojos & Martial Arts (Shortlist)",
        "cat_desc": "Priority martial arts facilities selected by David Turpin for immediate availability check.",
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
        "cat_title": "Traditional Dojos & Martial Arts (Shortlist)",
        "cat_desc": "Priority martial arts facilities selected by David Turpin for immediate availability check.",
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
        "cat_title": "Traditional Dojos & Martial Arts (Shortlist)",
        "cat_desc": "Priority martial arts facilities selected by David Turpin for immediate availability check.",
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
        "cat_title": "Traditional Dojos & Martial Arts (Shortlist)",
        "cat_desc": "Priority martial arts facilities selected by David Turpin for immediate availability check.",
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

    # 02 / WHITE & POLYVALENT SPACES (TURPIN SHORTLIST)
    {
        "category": "white-polyvalent",
        "cat_num": "02",
        "cat_title": "White & Polyvalent Spaces (Shortlist)",
        "cat_desc": "Curated white and daylight architectural spaces requested by David Turpin for custom intervention.",
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
        "cat_title": "White & Polyvalent Spaces (Shortlist)",
        "cat_desc": "Curated white and daylight architectural spaces requested by David Turpin for custom intervention.",
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
        "cat_title": "White & Polyvalent Spaces (Shortlist)",
        "cat_desc": "Curated white and daylight architectural spaces requested by David Turpin for custom intervention.",
        "id": "espacio-abc",
        "folder": "Espacio ABC",
        "name": "Espacio ABC",
        "tag": "SELECTED · EVENT STAGE",
        "tag_class": "available",
        "location": "C/ Serrano, 61 (Salamanca) · Madrid",
        "distance": "~11.5 km from Valdebebas",
        "drive_time": "~18 min driving",
        "notes": "Premium venue in ABC Serrano with polished architectural finishes and daylight atriums."
    },

    # 03 / PRODUCTION WILDCARD (STATUS UPDATE)
    {
        "category": "production-wildcard",
        "cat_num": "03",
        "cat_title": "Production Wildcard (Status Update)",
        "cat_desc": "Alternative industrial and innovation center verified with Zafarrancho Locations.",
        "id": "nave-boetticher",
        "folder": "La Nave Boetticher",
        "name": "La Nave Boetticher",
        "tag": "NO DISPONIBLE · PUBLICIDAD",
        "tag_class": "optioned",
        "location": "C/ Cifuentes, 5 (Villaverde) · Madrid",
        "distance": "~22.3 km from Valdebebas",
        "drive_time": "~34 min driving",
        "notes": "Descartada por Zafarrancho (Cecilia Corrales): La Nave Boetticher no acepta rodajes publicitarios según normativa municipal. Se mantiene en archivo únicamente como referencia visual de escala catedralicia."
    }
]

total_images = 0
categories_grouped = {}

for v in venues_catalog:
    v_folder = os.path.join(ASSETS_DIR, v["folder"])
    images = []
    if os.path.exists(v_folder):
        files = sorted([f for f in os.listdir(v_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png')) and not f.startswith('._')])
        images = [f"assets/{v['folder']}/{f}" for f in files]
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

html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TMC × TATAMIS · ADIDAS RM125 · TURPIN SHORTLIST MOODBOARD</title>
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

  /* Page Wrapper */
  .editorial-wrapper {{
    max-width: 1680px;
    margin: 0 auto;
    padding: 0 56px;
  }}

  /* Hero Section */
  .hero-section {{
    padding: 72px 0 56px;
    border-bottom: 1px solid var(--line-hairline);
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

  /* Filter & View Control Bar */
  .filter-bar {{
    position: sticky;
    top: 57px;
    z-index: 90;
    background: rgba(249, 245, 233, 0.94);
    backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--line-hairline);
    padding: 12px 56px;
    margin: 0 -56px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
  }}

  .filter-group {{
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
  }}

  .filter-label {{
    font-family: var(--font-heading);
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--ink-faint);
    margin-right: 6px;
  }}

  .filter-btn {{
    background: transparent;
    border: none;
    font-family: var(--font-heading);
    font-size: 10.5px;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--ink-muted);
    padding: 5px 12px;
    border-radius: 999px;
    cursor: pointer;
    transition: all 0.15s ease;
  }}

  .filter-btn:hover {{
    color: var(--ink-black);
    background: var(--bg-surface-subtle);
  }}

  .filter-btn.active {{
    color: var(--ink-black);
    background: var(--ink-black);
    color: var(--bg-page);
    font-weight: 600;
  }}

  .search-wrapper {{
    position: relative;
    display: flex;
    align-items: center;
  }}

  input.search-input {{
    background: var(--bg-surface-subtle);
    border: none;
    font-family: var(--font-body);
    font-size: 12.5px;
    color: var(--ink-black);
    padding: 6px 14px 6px 30px;
    border-radius: 999px;
    width: 220px;
    outline: none;
    transition: width 0.2s ease, background 0.2s ease;
  }}

  input.search-input:focus {{
    width: 280px;
    background: #FFFFFF;
  }}

  .search-icon {{
    position: absolute;
    left: 12px;
    display: flex;
    align-items: center;
    color: var(--ink-muted);
    pointer-events: none;
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

  /* Floating Quick-Nav Pill */
  .quick-nav-pill {{
    position: fixed;
    bottom: 32px;
    right: 48px;
    z-index: 95;
    background: var(--ink-black);
    color: var(--bg-page);
    border-radius: 999px;
    box-shadow: 0 8px 32px rgba(15, 15, 15, 0.24);
    display: flex;
    align-items: center;
    padding: 6px;
    gap: 4px;
    transition: transform 0.2s ease, opacity 0.2s ease;
  }}

  .quick-nav-btn {{
    background: transparent;
    border: none;
    color: var(--bg-page);
    font-family: var(--font-heading);
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 8px 16px;
    border-radius: 999px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: background 0.15s ease;
  }}

  .quick-nav-btn:hover {{
    background: rgba(255, 255, 255, 0.16);
  }}

  /* Jump Menu Drawer */
  .jump-drawer {{
    display: none;
    position: fixed;
    bottom: 84px;
    right: 48px;
    z-index: 96;
    background: var(--bg-card);
    border: 1px solid var(--line-hairline);
    border-top: 2px solid var(--ink-black);
    box-shadow: 0 16px 48px rgba(15, 15, 15, 0.18);
    width: 340px;
    max-height: 460px;
    overflow-y: auto;
    padding: 16px 0;
  }}

  .jump-drawer.active {{
    display: block;
  }}

  .jump-header {{
    padding: 4px 20px 12px;
    font-family: var(--font-heading);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--ink-faint);
    border-bottom: 1px solid var(--line-light);
  }}

  .jump-group-title {{
    padding: 10px 20px 4px;
    font-family: var(--font-heading);
    font-size: 9.5px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: var(--ink-muted);
  }}

  .jump-item {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 8px 20px;
    text-decoration: none;
    color: var(--ink-charcoal);
    font-size: 13px;
    transition: background 0.15s ease;
  }}

  .jump-item:hover {{
    background: var(--bg-surface-subtle);
    color: var(--ink-black);
  }}

  .jump-item-name {{
    font-weight: 500;
  }}

  .jump-item-meta {{
    font-family: var(--font-heading);
    font-size: 10.5px;
    color: var(--ink-muted);
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

  @media (max-width: 768px) {{
    header.masthead {{ padding: 14px 24px; }}
    .editorial-wrapper {{ padding: 0 24px; }}
    .filter-bar {{ padding: 12px 24px; margin: 0 -24px 32px; }}
    article.venue-unit {{ padding: 24px 20px 36px; }}
    .venue-lead-row {{ flex-direction: column; gap: 18px; }}
    .venue-specs-column {{ width: 100%; justify-content: space-between; }}
    .mosaic-cell.hero-large, .mosaic-cell.hero-side, .mosaic-cell.half-cell, .mosaic-cell.quad-cell, .mosaic-cell.trio-cell {{
      grid-column: span 12;
      height: 260px;
    }}
    .masthead-right {{ display: none; }}
    .hero-meta-grid {{ flex-direction: column; gap: 14px; }}
    .quick-nav-pill {{ right: 20px; bottom: 20px; }}
    .jump-drawer {{ right: 20px; bottom: 72px; width: 280px; }}
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
      <nav class="index-nav">
        <a href="#warm-wood">01 Traditional Wood ({len(categories_grouped.get('warm-wood', {}).get('venues', []))})</a>
        <a href="#white-polyvalent">02 White Polyvalent ({len(categories_grouped.get('white-polyvalent', {}).get('venues', []))})</a>
        <a href="#production-wildcard">03 Wildcard ({len(categories_grouped.get('production-wildcard', {}).get('venues', []))})</a>
      </nav>
      <div class="curation-counter">Turpin Shortlist · {len(venues_catalog)} Venues · {total_images} Plates</div>
    </div>
  </header>

  <div class="editorial-wrapper">

    <!-- Hero Section -->
    <section class="hero-section">
      <div class="hero-top-row">
        <span class="editorial-badge">Turpin Selection · Shortlist Moodboard</span>
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
      <p class="hero-deck">Curated selection filtered directly by David Turpin for client review and immediate Zafarrancho availability checks. Includes 9 prioritized tatamis/dojos, 3 polyvalent white spaces, and the La Nave Boetticher industrial contingency.</p>
    </section>

    <!-- Interactive Navigation & Filter Bar -->
    <div class="filter-bar">
      <div class="filter-group">
        <span class="filter-label">Filter:</span>
        <button class="filter-btn active" onclick="filterCategory('all', this)">All Shortlist ({len(venues_catalog)})</button>
        <button class="filter-btn" onclick="filterCategory('warm-wood', this)">01 Traditional Wood (9)</button>
        <button class="filter-btn" onclick="filterCategory('white-polyvalent', this)">02 White Polyvalent (3)</button>
        <button class="filter-btn" onclick="filterCategory('production-wildcard', this)">03 Wildcard (1)</button>
      </div>
      <div class="search-wrapper">
        <span class="search-icon"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></span>
        <input type="text" class="search-input" id="venueSearch" placeholder="Search venue, district..." oninput="handleSearch(this.value)">
      </div>
    </div>

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

        for idx, img_path in enumerate(v['images']):
            span_cls = get_grid_span(idx, num_imgs)
            html_template += f"""
            <div class="mosaic-cell {span_cls}" onclick="openLightbox(this)">
              <img src="{img_path}" alt="{v['name']} plate {idx+1}" loading="lazy">
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

jump_html = ""
for cat_id, cat_data in categories_grouped.items():
    jump_html += f"<div class='jump-group-title'>{cat_data['title']}</div>"
    for v in cat_data['venues']:
        jump_html += f"""
        <a href="#venue-{v['id']}" class="jump-item" onclick="toggleJumpDrawer(false)">
          <span class="jump-item-name">{v['name']}</span>
          <span class="jump-item-meta">{v['drive_time']}</span>
        </a>
        """

html_template += f"""
    </main>

    <!-- Editorial Footer -->
    <footer class="editorial-footer">
      <div>HAWAI FILMS · PRODUCTION &amp; LOCATIONS</div>
      <div>ADIDAS × TMC · RM125 TATAMIS · CONFIDENTIAL PRODUCTION MATERIAL</div>
    </footer>

  </div>

  <!-- Quick Nav Floating Control -->
  <div class="quick-nav-pill">
    <button class="quick-nav-btn" onclick="toggleJumpDrawer()">Shortlist ({len(venues_catalog)})</button>
    <button class="quick-nav-btn" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">Top</button>
  </div>

  <!-- Jump Menu Drawer -->
  <div class="jump-drawer" id="jumpDrawer">
    <div class="jump-header">Turpin Shortlist Directory</div>
    {jump_html}
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
        document.getElementById('jumpDrawer').classList.remove('active');
      }}
    }});
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated {OUTPUT_HTML} with Turpin Shortlist!")
