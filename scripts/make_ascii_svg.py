"""Convert the prepped portrait to a monochrome, self-typing ASCII SVG (writes avi-ascii.svg)."""
import html
from PIL import Image

COLS = 100
RAMP = " .`:-=+*cs#%@"   # bright (sparse) -> dark (dense)
CHAR_W, CHAR_H = 6.0, 11.0
FILL = "#c9d1d9"
ROW_DELAY = 0.04
ROW_DUR = 0.35

img = Image.open("source-prepped.png").convert("L")
w, h = img.size
rows = max(1, int(COLS * h / w * 0.5))
small = img.resize((COLS, rows), Image.LANCZOS)
px = small.load()

lines = []
for y in range(rows):
    chars = []
    for x in range(COLS):
        darkness = 1 - px[x, y] / 255
        chars.append(RAMP[min(len(RAMP) - 1, int(darkness * len(RAMP)))])
    lines.append("".join(chars).rstrip())

width = COLS * CHAR_W
height = rows * CHAR_H + 10
out = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" viewBox="0 0 {width:.0f} {height:.0f}">',
    f'<g font-family="Consolas, Menlo, monospace" font-size="10" fill="{FILL}" xml:space="preserve">',
]
for i, line in enumerate(lines):
    y = 10 + i * CHAR_H
    begin = i * ROW_DELAY
    out.append(
        f'<clipPath id="c{i}"><rect x="0" y="{y - 10:.1f}" height="{CHAR_H:.1f}" width="0">'
        f'<animate attributeName="width" from="0" to="{width:.1f}" begin="{begin:.2f}s" dur="{ROW_DUR}s" fill="freeze"/>'
        f'</rect></clipPath>'
    )
    out.append(f'<text x="0" y="{y:.1f}" clip-path="url(#c{i})">{html.escape(line)}</text>')
out += ["</g>", "</svg>"]
with open("avi-ascii.svg", "w") as f:
    f.write("\n".join(out))
print(f"wrote avi-ascii.svg ({COLS}x{rows} chars)")
