"""Plain info card. Writes info-card.svg. Edit the ROWS list to change content."""
import html

ROWS = [
    ("Name",        "Shavait Pandita"),
    ("Education",   "B.Tech Civil Engineering, IIT Indore (2029)"),
    ("Current",     "Marketing Associate, Code Rhythm 2027"),
    ("Previous",    "Web Development Associate, E-Summit 2026"),
    ("Research",    "AAAI-27 Undergraduate Consortium proposal"),
    ("Languages",   "Python, C++, JavaScript, TypeScript, SQL"),
    ("AI / ML",     "PyTorch, Scikit-learn, XGBoost, Transformers"),
    ("GenAI",       "LLMs, RAG, LangGraph, Vector Databases"),
    ("Web",         "React, Node.js, Express, MongoDB, PostgreSQL"),
    ("Tools",       "Docker, Kafka, Redis, Pathway, Git"),
    ("Projects",    "FlashGuard, GPT from Scratch, InterviewIQ"),
    ("Achievements","JEE Advanced AIR 9560, IAT 2025 AIR 1389"),
]

W = 560
ROW_H, TOP, PAD = 28, 40, 24
H = TOP + len(ROWS) * ROW_H + 16
LABEL_X, VALUE_X = PAD, 170
LABEL_COLOR, VALUE_COLOR, BG, BORDER = "#58a6ff", "#e6edf3", "#0d1117", "#30363d"
FONT = 'font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="14"'

parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
    f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="{BG}" stroke="{BORDER}"/>',
    f'<text x="{PAD}" y="26" {FONT} font-weight="600" fill="{VALUE_COLOR}">Profile</text>',
    f'<line x1="{PAD}" y1="34" x2="{W-PAD}" y2="34" stroke="{BORDER}"/>',
]
for i, (label, value) in enumerate(ROWS):
    y = TOP + i * ROW_H
    parts.append(f'<text x="{LABEL_X}" y="{y}" {FONT} fill="{LABEL_COLOR}">{html.escape(label)}</text>')
    parts.append(f'<text x="{VALUE_X}" y="{y}" {FONT} fill="{VALUE_COLOR}">{html.escape(value)}</text>')
parts.append("</svg>")
with open("info-card.svg", "w") as f:
    f.write("\n".join(parts))
print("wrote info-card.svg", W, "x", H)
