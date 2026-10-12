"""Neofetch-style info card. Writes info-card.svg. STATIC=1 gives a frozen frame."""
import os, html

STATIC = os.environ.get("STATIC") == "1"

ROWS = [
    ("Now",        "B.Tech Civil Engineering, IIT Indore (2029)"),
    ("",           "Marketing Associate, Code Rhythm 2027 (CSESA)"),
    ("Prev",       "Web Development Associate, E-Summit 2026, IIT Indore"),
    ("Research",   "AAAI-27 Undergraduate Consortium proposal (eVTOL traffic)"),
    ("Languages",  "Python, C++, JavaScript, TypeScript, SQL"),
    ("AI / ML",    "PyTorch, Scikit-learn, XGBoost, Pandas, NumPy, Transformers, NLP"),
    ("GenAI",      "LLMs, RAG, Embeddings, Vector DBs, LangGraph"),
    ("Streaming",  "Pathway, Kafka, Redis"),
    ("Web",        "React, Node.js, Express, MongoDB, PostgreSQL, Firebase, Tailwind"),
    ("DevOps",     "Docker, Git, GitHub"),
    ("Highlights", "FlashGuard (Pathway fraud detection), GPT from scratch, InterviewIQ"),
    ("",           "AIR 1389 (IAT 2025), JEE Advanced AIR 9560, NSEP Top 1%"),
]

W, H = 490, 340
ROW_H, TOP = 20, 52
KEY_COLOR, VAL_COLOR, MUTED = "#7ee787", "#c9d1d9", "#8b949e"
MONO = 'font-family="Consolas, Menlo, monospace" font-size="12"'

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="#0d1117" stroke="#30363d"/>',
    '<circle cx="18" cy="18" r="5" fill="#ff5f56"/><circle cx="36" cy="18" r="5" fill="#ffbd2e"/><circle cx="54" cy="18" r="5" fill="#27c93f"/>',
    f'<text x="{W/2}" y="22" text-anchor="middle" {MONO} fill="{MUTED}">ershavait@iit-indore ~ neofetch</text>',
    f'<line x1="0" y1="34" x2="{W}" y2="34" stroke="#30363d"/>',
]
for i, (k, v) in enumerate(ROWS):
    y = TOP + i * ROW_H
    if STATIC:
        parts.append(f'<g opacity="1">')
    else:
        d = 0.15 + i * 0.12
        parts.append(f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" begin="{d:.2f}s" dur="0.4s" fill="freeze"/>')
    parts.append(f'<text x="18" y="{y}" {MONO} fill="{KEY_COLOR}">{html.escape(k)}</text>')
    parts.append(f'<text x="110" y="{y}" {MONO} fill="{VAL_COLOR}">{html.escape(v)}</text></g>')
parts.append("</svg>")
with open("info-card.svg", "w") as f:
    f.write("\n".join(parts))
print("wrote info-card.svg", "(static)" if STATIC else "(animated)")
