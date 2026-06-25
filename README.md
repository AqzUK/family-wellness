# 🌙 Peak Family Wellness App

Built for the Zahid family · St Albans · Bismillah

## What this app does

- **Three profiles** — Aquib, Yousaf, Mariam — each with personalised plans
- **Live prayer times** — pulled daily from Aladhan API for St Albans, accurate all year
- **Sleep intelligence** — tells you exactly when to sleep and wake based on today's Fajr and Isha
- **Daily check-in** — weight, sleep, prayers, food, energy, streak tracker
- **Gym plans** — prescriptive sessions for each person, changes by day of week
- **I'm Hungry** — tells you what to make right now based on time of day, halal and cheap
- **Weekly Aldi shopping list** — for the whole family, estimated under £60
- **Progress charts** — weight, sleep and energy over time
- **Islamic motivation** — authenticated quotes from Quran, Sahih al-Bukhari and Sahih Muslim only

---

## Setup (local)

```bash
git clone https://github.com/AqzUK/family-wellness.git
cd family-wellness
pip install -r requirements.txt
streamlit run app.py
```

---

## Deploy free on Streamlit Community Cloud

1. Push this repo to your GitHub (github.com/AqzUK)
2. Go to share.streamlit.io
3. Connect your GitHub account
4. Select this repo, set main file as `app.py`
5. Click Deploy — done. Free forever.

Your data (logs and profiles) will persist in the `data/` folder on the server.

---

## File structure

```
family-wellness/
├── app.py                  # Main app
├── requirements.txt
├── data/                   # Auto-created — stores profiles and logs
│   └── logs/
└── utils/
    ├── prayer_times.py     # Aladhan API integration
    ├── islamic_quotes.py   # Authenticated quotes only
    ├── data_store.py       # Profile and log persistence
    ├── gym_plans.py        # Personalised gym plans
    ├── meal_plans.py       # Meal suggestions by time of day
    └── shopping.py         # Weekly Aldi shopping list
```

---

## Prayer time source

All prayer times are fetched live from [Aladhan API](https://aladhan.com/prayer-times-api)
using St Albans coordinates (51.7526, -0.3364) and Method 2 (ISNA).
No hardcoded times. Accurate across summer and winter automatically.

---

## Islamic references used

All motivational content is drawn exclusively from:
- The Holy Quran
- Sahih al-Bukhari
- Sahih Muslim

No fabricated or unverified hadith are used anywhere in this app.

---

*"The most beloved of deeds to Allah are those that are most consistent, even if they are small."*
*— Sahih al-Bukhari 6464 · Sahih Muslim 783*
