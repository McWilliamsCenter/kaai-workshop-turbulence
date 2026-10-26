"""
Build the round, red-ringed site logo from a source render.

Usage:
    python3 scripts/make_logo.py <source.png> <out.png> <x0> <y0> <size>

Crops the square (x0, y0, size) from the source, masks it to a circle inside a CMU-red
ring, and writes a 1920x1920 transparent PNG. Resize that to the sizes listed in README.md.
"""
import sys
from PIL import Image, ImageDraw
src, out = sys.argv[1], sys.argv[2]
x0, y0, size = int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
N = 1920  # working canvas
im = Image.open(src).convert('RGB').crop((x0, y0, x0+size, y0+size)).resize((N, N), Image.LANCZOS)
canvas = Image.new('RGBA', (N, N), (0, 0, 0, 0))
ring = int(N * 0.021); pad = int(N * 0.04)
d = ImageDraw.Draw(canvas)
d.ellipse((pad, pad, N-pad, N-pad), fill=(255, 255, 255, 255), outline=(0xC4, 0x12, 0x30, 255), width=ring)
inner = pad + ring + int(N*0.012)
mask = Image.new('L', (N, N), 0)
ImageDraw.Draw(mask).ellipse((inner, inner, N-inner, N-inner), fill=255)
canvas.paste(im, (0, 0), mask)
canvas.save(out)
