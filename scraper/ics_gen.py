from ics import Calendar, Event
from datetime import datetime, timezone


def build_calendar(events):
    cal = Calendar()
    for ev in events:
        e = Event()
        e.name = ev["title"]
        e.begin = ev["start"].astimezone(timezone.utc)
        e.end = ev["end"].astimezone(timezone.utc)
        e.description = (ev.get("summary") or "") + (f"\nLink: {ev.get('link','')}" if ev.get("link") else "")
        e.url = ev.get("link")
        e.uid = ev["uid"]  # stable id
        cal.events.add(e)
    return cal


def write_calendar(cal, path="docs/dc-dark-legion.ics"):
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(cal)
