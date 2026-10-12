"""Render data/contributions.json as an animated 53x7 contribution heatmap (writes contrib-heatmap.svg)."""
import json, datetime as dt

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
CELL, GAP, LEFT, TOP = 12, 3, 20, 40
MONO = 'font-family="Consolas, Menlo, monospace"'

with open("data/contributions.json") as f:
    data = json.load(f)
days = data["days"]

offset = (dt.date.fromisoformat(days[0]["date"]).weekday() + 1) % 7   # Sunday = row 0
cells = [None] * offset + days
cols = (len(cells) + 6) // 7
W = LEFT * 2 + cols * (CELL + GAP)
H = TOP + 7 * (CELL + GAP) + 50

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    '<style>@keyframes in{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}'
    '.c{animation:in .5s ease both}</style>',
    f'<text x="{LEFT}" y="22" {MONO} font-size="13" fill="#c9d1d9">{data["total"]:,} contributions in the last year</text>',
]
for i, d in enumerate(cells):
    if d is None:
        continue
    col, row = divmod(i, 7)
    x, y = LEFT + col * (CELL + GAP), TOP + row * (CELL + GAP)
    parts.append(f'<rect class="c" x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" '
                 f'fill="{PALETTE[d["level"]]}" style="animation-delay:{(col + row) * 0.02:.2f}s"/>')

ly, lx = H - 22, W - LEFT - 150
parts.append(f'<text x="{lx}" y="{ly+10}" {MONO} font-size="11" fill="#8b949e">Less</text>')
for k, c in enumerate(PALETTE):
    parts.append(f'<rect x="{lx + 34 + k*14}" y="{ly}" width="11" height="11" rx="2" fill="{c}"/>')
parts.append(f'<text x="{lx + 34 + 6*14 + 4}" y="{ly+10}" {MONO} font-size="11" fill="#8b949e">More</text>')
parts.append(f'<text x="{LEFT}" y="{H-8}" {MONO} font-size="11" fill="#8b949e">'
             f'current streak {data["current_streak"]} · longest {data["longest_streak"]}</text>')
parts.append("</svg>")
with open("contrib-heatmap.svg", "w") as f:
    f.write("\n".join(parts))
print("wrote contrib-heatmap.svg")
