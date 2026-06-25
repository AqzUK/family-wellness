import requests
from datetime import date, datetime

ST_ALBANS_LAT  = 51.7526
ST_ALBANS_LNG  = -0.3364
METHOD         = 2  # ISNA — commonly used in UK

def get_prayer_times() -> dict:
    """Fetch today's prayer times from Aladhan API for St Albans."""
    today = date.today()
    url = (
        f"https://api.aladhan.com/v1/timings/{today.day}-{today.month}-{today.year}"
        f"?latitude={ST_ALBANS_LAT}&longitude={ST_ALBANS_LNG}&method={METHOD}"
    )
    try:
        resp = requests.get(url, timeout=8)
        resp.raise_for_status()
        data = resp.json()
        timings = data["data"]["timings"]
        return {
            "Fajr":    timings["Fajr"],
            "Sunrise": timings["Sunrise"],
            "Dhuhr":   timings["Dhuhr"],
            "Asr":     timings["Asr"],
            "Maghrib": timings["Maghrib"],
            "Isha":    timings["Isha"],
            "Midnight": timings.get("Midnight", ""),
        }
    except Exception:
        return {}


def _parse_time(t_str: str) -> datetime | None:
    """Parse HH:MM string into today's datetime."""
    try:
        h, m = map(int, t_str.split(":"))
        return datetime.now().replace(hour=h, minute=m, second=0, microsecond=0)
    except Exception:
        return None


def get_sleep_instruction(prayers: dict) -> str:
    """
    Generate a prescriptive sleep instruction based on today's Fajr and Isha times.
    Accounts for summer (late Isha / early Fajr) and winter (early Isha / late Fajr).
    """
    fajr_str = prayers.get("Fajr", "")
    isha_str  = prayers.get("Isha", "")

    fajr = _parse_time(fajr_str)
    isha = _parse_time(isha_str)

    if not fajr or not isha:
        return "Set an alarm for Fajr and aim for 7 hours sleep."

    fajr_hour = fajr.hour + fajr.minute / 60
    isha_hour  = isha.hour + isha.minute / 60

    # Gap between Isha and Fajr
    if fajr_hour < isha_hour:
        gap_hours = (24 - isha_hour) + fajr_hour
    else:
        gap_hours = fajr_hour - isha_hour

    # Summer: Isha after 10pm AND Fajr before 4am
    if isha_hour >= 22 and fajr_hour <= 4:
        bedtime_after_isha = "Sleep immediately after Isha prayer"
        return (
            f"SUMMER PROTOCOL — Isha is {isha_str}, Fajr is {fajr_str} "
            f"(only {gap_hours:.1f} hours between them). "
            f"{bedtime_after_isha}. Wake for Fajr, pray, then sleep again until 7:00am. "
            "This split sleep is Sunnah-aligned and essential. No screens after 9:30pm."
        )

    # Winter: Isha before 8pm, Fajr after 6am — plenty of night
    if isha_hour <= 20 and fajr_hour >= 6:
        sleep_target = f"{int(fajr_hour - 7):02d}:00"
        return (
            f"WINTER PROTOCOL — Isha is {isha_str}, Fajr is {fajr_str}. "
            f"You have {gap_hours:.1f} hours. Sleep by {sleep_target} to get 7 full hours before Fajr. "
            "No food after 8:30pm. No screens 30 minutes before bed."
        )

    # Standard
    target_hour = int(fajr_hour - 7)
    if target_hour < 0:
        target_hour += 24
    return (
        f"Fajr is at {fajr_str}. Sleep by {target_hour:02d}:00 to get 7 hours. "
        "Pray Isha then rest immediately. No food or screens after 9:00pm."
    )
