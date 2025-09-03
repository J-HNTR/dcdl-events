# DC: Dark Legion – Auto-updating Calendar Feed

Public iCal feed (subscribe by URL):  
`https://J-HNTR.github.io/dcdl-events/dc-dark-legion.ics`

This repo scrapes public sources (official website news, official socials, and the official subreddit)
for announced event windows and publishes an `.ics` you can subscribe to in Apple, Google, or Samsung Calendar.

**Notes**
- Official posts are prioritized; community trackers are used only as hints because plans can change.
- If an event title lacks explicit dates, heuristics + keyword-based durations are applied.
- You can pin corrections in `data/manual_overrides.yaml`.

**Subscribe**
- **Apple Calendar (Mac/iOS)**: File → New Calendar Subscription → paste the URL.
- **Google Calendar**: Other calendars → `+` → From URL → paste the URL.
- **Samsung Calendar**: Hamburger menu → Manage calendars → Add calendar → Add by URL.
