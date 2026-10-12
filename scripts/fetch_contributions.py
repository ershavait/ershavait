"""Scrape public contribution data (no token) into data/contributions.json."""
import json, re, datetime as dt
import requests
from bs4 import BeautifulSoup

USER = "ershavait"
resp = requests.get(f"https://github.com/users/{USER}/contributions", timeout=30,
                    headers={"User-Agent": "profile-art-bot"})
resp.raise_for_status()
soup = BeautifulSoup(resp.text, "html.parser")

days = []
for cell in soup.select("td.ContributionCalendar-day[data-date]"):
    level = int(cell.get("data-level", 0))
    tip = soup.select_one(f"tool-tip[for='{cell.get('id')}']")
    text = tip.get_text(strip=True) if tip else ""
    m = re.match(r"(\d+)", text.replace(",", ""))
    count = int(m.group(1)) if m and not text.startswith("No") else 0
    days.append({"date": cell.get("data-date"), "count": count, "level": level})

days.sort(key=lambda d: d["date"])
total = sum(d["count"] for d in days)

best = cur = 0
for d in days:
    cur = cur + 1 if d["count"] > 0 else 0
    best = max(best, cur)
current = 0
for d in reversed(days):
    if d["count"] > 0:
        current += 1
    else:
        break

with open("data/contributions.json", "w") as f:
    json.dump({"user": USER, "updated": dt.datetime.now(dt.timezone.utc).isoformat(),
               "total": total, "longest_streak": best, "current_streak": current,
               "days": days}, f, indent=1)
print(f"{len(days)} days, {total} contributions, streak {current} (best {best})")
