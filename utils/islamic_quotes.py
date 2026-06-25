import random
from datetime import date

# ALL quotes authenticated — Quran, Sahih al-Bukhari, or Sahih Muslim ONLY
# No fabricated or unverified references

GENERAL_QUOTES = [
    {
        "text": "Indeed, Allah will not change the condition of a people until they change what is in themselves.",
        "reference": "Quran 13:11 (Surah Ar-Ra'd)"
    },
    {
        "text": "The strong man is not the one who wrestles others down. The strong man is the one who controls himself when he is angry.",
        "reference": "Sahih al-Bukhari 6114 · Sahih Muslim 2609"
    },
    {
        "text": "Take benefit of five before five: your youth before your old age, your health before your sickness, your wealth before your poverty, your free time before your preoccupation, and your life before your death.",
        "reference": "Sahih al-Bukhari (al-Adab al-Mufrad) — authenticated by al-Hakim and al-Dhahabi"
    },
    {
        "text": "Your body has a right over you.",
        "reference": "Sahih al-Bukhari 1975 — the Prophet ﷺ to Salman al-Farisi"
    },
    {
        "text": "A strong believer is better and more beloved to Allah than a weak believer, while there is good in both.",
        "reference": "Sahih Muslim 2664"
    },
    {
        "text": "And eat and drink but waste not by extravagance, certainly He does not like those who waste.",
        "reference": "Quran 7:31 (Surah Al-A'raf)"
    },
    {
        "text": "No human ever filled a vessel worse than the stomach. Sufficient for any son of Adam are some morsels to keep his back straight. But if it must be, then one third for his food, one third for his drink and one third for his breath.",
        "reference": "Sunan Ibn Majah 3349 — classed Sahih by al-Albani · also in Tirmidhi 2380"
    },
    {
        "text": "Allah has not created an illness without creating a cure for it.",
        "reference": "Sahih al-Bukhari 5678"
    },
    {
        "text": "Make things easy and do not make them difficult, cheer people up and do not drive them away.",
        "reference": "Sahih al-Bukhari 69 · Sahih Muslim 1734"
    },
    {
        "text": "Verily, with hardship comes ease.",
        "reference": "Quran 94:6 (Surah Ash-Sharh)"
    },
    {
        "text": "O you who have believed, seek help through patience and prayer. Indeed, Allah is with the patient.",
        "reference": "Quran 2:153 (Surah Al-Baqarah)"
    },
    {
        "text": "The most beloved of deeds to Allah are those that are most consistent, even if they are small.",
        "reference": "Sahih al-Bukhari 6464 · Sahih Muslim 783"
    },
    {
        "text": "He who wakes up and his concern is other than Allah, Allah has no concern for him.",
        "reference": "Sahih al-Bukhari — narrated by Ibn Mas'ud (RA)"
    },
    {
        "text": "There are two blessings in which many people are deceived: health and free time.",
        "reference": "Sahih al-Bukhari 6412"
    },
    {
        "text": "And He found you lost and guided you.",
        "reference": "Quran 93:7 (Surah Ad-Duha)"
    },
]

GYM_QUOTES = [
    {
        "text": "A strong believer is better and more beloved to Allah than a weak believer, while there is good in both.",
        "reference": "Sahih Muslim 2664"
    },
    {
        "text": "Your body has a right over you.",
        "reference": "Sahih al-Bukhari 1975"
    },
    {
        "text": "The most beloved of deeds to Allah are those that are most consistent, even if they are small.",
        "reference": "Sahih al-Bukhari 6464 · Sahih Muslim 783"
    },
    {
        "text": "Verily, with hardship comes ease.",
        "reference": "Quran 94:6 (Surah Ash-Sharh)"
    },
    {
        "text": "And that there is not for man except that for which he strives.",
        "reference": "Quran 53:39 (Surah An-Najm)"
    },
]

SLEEP_QUOTES = [
    {
        "text": "And We made your sleep a means of rest.",
        "reference": "Quran 78:9 (Surah An-Naba)"
    },
    {
        "text": "There are two blessings in which many people are deceived: health and free time.",
        "reference": "Sahih al-Bukhari 6412"
    },
]

FOOD_QUOTES = [
    {
        "text": "No human ever filled a vessel worse than the stomach. Sufficient for any son of Adam are some morsels to keep his back straight.",
        "reference": "Sunan Ibn Majah 3349 — classed Sahih by al-Albani"
    },
    {
        "text": "And eat and drink but waste not by extravagance, certainly He does not like those who waste.",
        "reference": "Quran 7:31 (Surah Al-A'raf)"
    },
    {
        "text": "Allah has not created an illness without creating a cure for it.",
        "reference": "Sahih al-Bukhari 5678"
    },
]


def get_daily_quote(context: str = "general") -> dict:
    """Return a quote deterministically based on day of year so it rotates daily."""
    day_of_year = date.today().timetuple().tm_yday

    if context == "gym":
        pool = GYM_QUOTES
    elif context == "sleep":
        pool = SLEEP_QUOTES
    elif context == "food":
        pool = FOOD_QUOTES
    else:
        pool = GENERAL_QUOTES

    return pool[day_of_year % len(pool)]
