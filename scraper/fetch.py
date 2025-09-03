import requests, feedparser, time
from bs4 import BeautifulSoup


def get_rss_items(url: str):
    feed = feedparser.parse(url)
    for e in feed.entries:
        yield {
            "title": e.get("title", ""),
            "link": e.get("link", ""),
            "summary": e.get("summary", ""),
            "published": e.get("published", "") or e.get("updated", "")
        }


def get_html_items(url: str):
    # Basic HTML fetch for the official site news list
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    # Heuristic: find news cards/links with dates; adjust selectors if site changes.
    items = []
    for a in soup.find_all("a"):
        t = (a.get_text() or "").strip()
        if not t:
            continue
        if any(k in t.lower() for k in ["event", "schedule", "roadmap", "newsletter"]):
            items.append({"title": t, "link": a.get("href", ""), "summary": "", "published": ""})
    return items
