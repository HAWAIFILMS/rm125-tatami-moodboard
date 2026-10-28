import os, time
from PIL import Image
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(ROOT, "assets")
THUMBS_DIR = os.path.join(ROOT, "assets_thumbs")
os.makedirs(THUMBS_DIR, exist_ok=True)

from generate_editorial_moodboard import venues_catalog

tasks = []
for v in venues_catalog:
    src_folder = os.path.join(ASSETS_DIR, v["folder"])
    dst_folder = os.path.join(THUMBS_DIR, v["folder"])
    os.makedirs(dst_folder, exist_ok=True)
    if os.path.exists(src_folder):
        for f in os.listdir(src_folder):
            if f.lower().endswith(('.jpg', '.jpeg', '.png')) and not f.startswith('.'):
                src = os.path.join(src_folder, f)
                base = os.path.splitext(f)[0]
                dst = os.path.join(dst_folder, f"{base}.webp")
                tasks.append((src, dst))

def convert(item):
    src, dst = item
    if os.path.exists(dst) and os.path.getmtime(dst) >= os.path.getmtime(src):
        return True
    try:
        with Image.open(src) as img:
            img = img.convert("RGB")
            img.thumbnail((1200, 1200), Image.Resampling.LANCZOS)
            img.save(dst, "WEBP", quality=78, method=4)
        return True
    except Exception as e:
        print(f"Error {src}: {e}")
        return False

print(f"Checking/generating WebP thumbnails for {len(tasks)} images...")
t0 = time.time()
with ThreadPoolExecutor(max_workers=8) as ex:
    results = list(ex.map(convert, tasks))
print(f"Completed in {time.time()-t0:.2f}s")
