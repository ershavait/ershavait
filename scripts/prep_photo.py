"""Grayscale, contrast-boost and flatten a portrait. Usage: python scripts/prep_photo.py source-photo.png"""
import sys
from PIL import Image, ImageOps, ImageEnhance

src = sys.argv[1] if len(sys.argv) > 1 else "source-photo.png"
img = Image.open(src).convert("L")
img = ImageOps.autocontrast(img, cutoff=1)
img = ImageEnhance.Contrast(img).enhance(1.6)
img.save("source-prepped.png")
print("wrote source-prepped.png", img.size)
