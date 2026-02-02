import sys
import os
from PIL import Image

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

files = sys.argv[1:]

images = [
    f for f in files
    if os.path.isfile(f) and f.lower().endswith((".jpg", ".jpeg", ".png"))
]

if not images:
    sys.exit(0)

images.sort()

out_dir = os.path.dirname(images[0])
first_name = os.path.splitext(os.path.basename(images[0]))[0]
output_pdf = os.path.join(out_dir, first_name + ".pdf")

pages = []

for img_path in images:
    img = Image.open(img_path)
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")
    pages.append(img)

pages[0].save(
    output_pdf,
    save_all=True,
    append_images=pages[1:]
)
