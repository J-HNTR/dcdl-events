import re
from dateutil import parser as dtp
from datetime import timedelta

# Common date patterns like "July 8–22" or "Jul 8 - Jul 22, 2025"
DATE_PAT = re.compile(
    r'(?P<start_month>[A-Za-z]{3,9})\.?\s*(?P<start_day>\d{1,2})(?:,\s*(?P<start_year>\d{4}))?'
    r'\s*(?:–|-|to)\s*'
    r'(?:(?P<end_month>[A-Za-z]{3,9})\.?\s*)?(?P<end_day>\d{1,2})(?:,\s*(?P<end_year>\d{4}))?',
    re.IGNORECASE
)

SINGLE_DAY_PAT = re.compile(
    r'(?P<month>[A-Za-z]{3,9})\.?\s*(?P<day>\d{1,2})(?:,\s*(?P<year>\d{4}))?',
    re.IGNORECASE
)

KEYWORDS_TO_DURATION = {
    "supreme commander": 7,   # community: weekly cadence (varies; adjust if needed)
    "bleed": 7,
    "hypertime": 7,
    "event": 3,               # fallback if no range detected
}

def infer_dates_from_text(text: str, default_year: int):
    text = text.strip()
    m = DATE_PAT.search(text)
    if m:
        sm, sd = m.group("start_month"), m.group("start_day")
        sy = m.group("start_year") or str(default_year)
        em = m.group("end_month") or sm
        ed = m.group("end_day")
        ey = m.group("end_year") or sy
        start = dtp.parse(f"{sm} {sd} {sy}")
        end   = dtp.parse(f"{em} {ed} {ey}") + timedelta(days=1)  # ICE end is exclusive
        return start, end

    # Try single date + keyword duration
    kmatch = None
    for k in KEYWORDS_TO_DURATION:
        if k in text.lower():
            kmatch = k
            break

    m2 = SINGLE_DAY_PAT.search(text)
    if m2 and kmatch:
        mo, d = m2.group("month"), m2.group("day")
        y = m2.group("year") or str(default_year)
        start = dtp.parse(f"{mo} {d} {y}")
        end = start + timedelta(days=KEYWORDS_TO_DURATION[kmatch])
        return start, end

    return None, None

def summarize_title(title: str):
    # Clean noisy prefixes
    title = re.sub(r'\s*\|\s*.*$', '', title).strip()
    return title
