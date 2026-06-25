import streamlit as st
import json
import os
from datetime import date
from utils.prayer_times import get_prayer_times, get_sleep_instruction
from utils.data_store import load_profiles, save_profiles, load_logs, save_log
from utils.islamic_quotes import get_daily_quote

st.set_page_config(
    page_title="Family Wellness — Peak Health",
    page_icon="🌙",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  .main-title { font-size: 26px; font-weight: 600; margin-bottom: 4px; }
  .sub-title  { font-size: 14px; color: #888; margin-bottom: 1.5rem; }
  .quran-card {
    background: linear-gradient(135deg, #1a472a 0%, #2d6a4f 100%);
    border-radius: 12px; padding: 1.2rem 1.4rem; margin-bottom: 1.5rem; color: white;
  }
  .quran-text  { font-size: 15px; font-style: italic; margin-bottom: 6px; }
  .quran-ref   { font-size: 12px; opacity: 0.75; }
  .prayer-row  {
    display: flex; justify-content: space-between; align-items: center;
    padding: 6px 0; border-bottom: 1px solid #f0f0f0; font-size: 14px;
  }
  .prayer-name { font-weight: 500; }
  .prayer-time { color: #2d6a4f; font-weight: 600; }
  .sleep-box {
    background: #eaf3f8; border-left: 4px solid #1a6fa0;
    border-radius: 6px; padding: 0.8rem 1rem; margin-top: 1rem;
    font-size: 14px; color: #1a4f6e;
  }
  .metric-card {
    background: #f8f8f8; border-radius: 10px;
    padding: 0.9rem 1rem; text-align: center;
  }
  .metric-val  { font-size: 24px; font-weight: 600; color: #1a472a; }
  .metric-lab  { font-size: 12px; color: #888; margin-top: 2px; }
  .streak-fire { font-size: 32px; }
  .gym-card {
    background: #fff8f0; border-left: 4px solid #e07b39;
    border-radius: 6px; padding: 1rem 1.2rem; margin-bottom: 1rem;
  }
  .gym-title   { font-weight: 600; font-size: 15px; color: #b85c1a; margin-bottom: 8px; }
  .gym-item    { font-size: 13px; padding: 3px 0; color: #333; }
  .hungry-card {
    background: #f0f7f0; border-left: 4px solid #2d6a4f;
    border-radius: 6px; padding: 1rem 1.2rem; margin-bottom: 0.8rem;
  }
  .hungry-title { font-weight: 600; font-size: 15px; color: #1a472a; margin-bottom: 6px; }
  .hungry-item  { font-size: 13px; color: #333; padding: 2px 0; }
  .aldi-section { margin-bottom: 0.5rem; }
  .aldi-header  { font-weight: 600; font-size: 14px; color: #e07b39; margin: 0.8rem 0 4px; }
</style>
""", unsafe_allow_html=True)

# ── SESSION STATE ──────────────────────────────────────────────────────────────
if "active_profile" not in st.session_state:
    st.session_state.active_profile = None
if "profiles" not in st.session_state:
    st.session_state.profiles = load_profiles()

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🌙 Peak Family Wellness")
    st.markdown("---")

    profiles = st.session_state.profiles
    if profiles:
        names = [p["name"] for p in profiles]
        choice = st.radio("Who are you?", names)
        st.session_state.active_profile = next(p for p in profiles if p["name"] == choice)
        st.markdown("---")

    st.markdown("**Navigation**")
    page = st.radio(
        "Go to",
        ["🏠 Daily Dashboard", "⚖️ Log Weight", "🏋️ Gym Plan",
         "🍽️ Weekly Meal Plan", "🥗 I'm Hungry", "🛒 Shopping List",
         "📈 My Progress", "👤 Profiles"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.caption("Built for the Zahid family · St Albans")

# ── PROFILE SETUP ─────────────────────────────────────────────────────────────
if page == "👤 Profiles":
    st.markdown('<div class="main-title">👤 Family Profiles</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Set up or update each person\'s details</div>', unsafe_allow_html=True)

    profiles = st.session_state.profiles
    existing_names = [p["name"] for p in profiles]

    with st.expander("➕ Add or update a profile", expanded=len(profiles) == 0):
        pname  = st.selectbox("Name", ["Aquib", "Yousaf", "Mariam", "Anwar"])
        height = st.text_input("Height (e.g. 5ft 11)")
        weight = st.number_input("Current weight (stone)", min_value=6.0, max_value=30.0, step=0.1)
        target = st.number_input("Target weight (stone)", min_value=6.0, max_value=30.0, step=0.1)
        age    = st.number_input("Age", min_value=10, max_value=80, step=1)
        goal   = st.selectbox("Primary goal", ["Weight loss + strength", "Gradual weight loss (teen)", "Tone + general health"])

        if st.button("Save profile"):
            new_p = {"name": pname, "height": height, "weight": weight,
                     "target": target, "age": int(age), "goal": goal,
                     "start_weight": weight}
            profiles = [p for p in profiles if p["name"] != pname]
            profiles.append(new_p)
            st.session_state.profiles = profiles
            save_profiles(profiles)
            st.success(f"Profile saved for {pname}!")
            st.rerun()

    if profiles:
        st.markdown("### Current profiles")
        for p in profiles:
            lost = round(p["start_weight"] - p["weight"], 1)
            to_go = round(p["weight"] - p["target"], 1)
            cols = st.columns(4)
            cols[0].metric("Name", p["name"])
            cols[1].metric("Current", f"{p['weight']} st")
            cols[2].metric("Lost so far", f"{lost} st")
            cols[3].metric("To go", f"{to_go} st")
            st.markdown("---")

# ── DAILY DASHBOARD ───────────────────────────────────────────────────────────
elif page == "🏠 Daily Dashboard":
    profile = st.session_state.active_profile
    if not profile:
        st.warning("Please set up your profile first using the Profiles page.")
        st.stop()

    name = profile["name"]
    today = date.today()

    st.markdown(f'<div class="main-title">Assalamu Alaikum, {name} 🌙</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-title">{today.strftime("%A, %d %B %Y")}</div>', unsafe_allow_html=True)

    # Islamic quote
    quote = get_daily_quote()
    st.markdown(f"""
    <div class="quran-card">
      <div class="quran-text">"{quote['text']}"</div>
      <div class="quran-ref">— {quote['reference']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Prayer times
    st.markdown("### 🕌 Today's Prayer Times")
    prayers = get_prayer_times()
    if prayers:
        prayer_names = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
        cols = st.columns(5)
        for i, pname_p in enumerate(prayer_names):
            cols[i].metric(pname_p, prayers.get(pname_p, "—"))

        sleep_info = get_sleep_instruction(prayers)
        st.markdown(f'<div class="sleep-box">🛏️ <strong>Tonight:</strong> {sleep_info}</div>', unsafe_allow_html=True)
    else:
        st.warning("Could not load prayer times. Check your internet connection.")

    st.markdown("---")

    # Daily check-in
    st.markdown("### ✅ Daily Check-In")
    logs = load_logs(name)
    today_str = today.isoformat()
    already_logged = any(l["date"] == today_str for l in logs)

    if already_logged:
        st.success("You've completed today's check-in. Barakallahu feek! 🌿")
    else:
        with st.form("checkin_form"):
            w       = st.number_input("Weight this morning (stone)", min_value=6.0, max_value=30.0, step=0.1, value=float(profile["weight"]))
            sleep_h = st.slider("Hours of sleep last night", 0, 12, 7)
            prayers_done = st.multiselect("Prayers completed today", ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"])
            ate_late = st.radio("Did you eat after 8:30pm last night?", ["No ✅", "Yes ❌"])
            trained  = st.radio("Did you train / exercise today?", ["Yes 💪", "No", "Rest day"])
            sugar    = st.select_slider("Sugar intake today", options=["None ✅", "1–2 items", "Too much ❌"])
            energy   = st.slider("Energy level today (1–10)", 1, 10, 7)

            submitted = st.form_submit_button("Submit check-in")
            if submitted:
                log_entry = {
                    "date": today_str, "weight": w, "sleep": sleep_h,
                    "prayers": prayers_done, "ate_late": ate_late,
                    "trained": trained, "sugar": sugar, "energy": energy
                }
                save_log(name, log_entry)
                # Update profile weight
                profile["weight"] = w
                profiles = st.session_state.profiles
                profiles = [p if p["name"] != name else profile for p in profiles]
                st.session_state.profiles = profiles
                save_profiles(profiles)
                st.success("Check-in saved! May Allah bless your efforts. 🌿")
                st.rerun()

    # Streak
    st.markdown("---")
    streak = 0
    for l in sorted(logs, key=lambda x: x["date"], reverse=True):
        if l.get("ate_late") == "No ✅" and l.get("sleep", 0) >= 6:
            streak += 1
        else:
            break
    cols = st.columns(3)
    cols[0].markdown(f'<div class="metric-card"><div class="metric-val">{streak}</div><div class="metric-lab">Day streak 🔥</div></div>', unsafe_allow_html=True)
    lost = round(profile["start_weight"] - profile["weight"], 1)
    cols[1].markdown(f'<div class="metric-card"><div class="metric-val">{lost} st</div><div class="metric-lab">Lost so far</div></div>', unsafe_allow_html=True)
    to_go = round(profile["weight"] - profile["target"], 1)
    cols[2].markdown(f'<div class="metric-card"><div class="metric-val">{to_go} st</div><div class="metric-lab">To go</div></div>', unsafe_allow_html=True)

# ── GYM PLAN ──────────────────────────────────────────────────────────────────
elif page == "🏋️ Gym Plan":
    from utils.gym_plans import get_todays_gym_plan
    profile = st.session_state.active_profile
    if not profile:
        st.warning("Please set up your profile first.")
        st.stop()

    st.markdown('<div class="main-title">🏋️ Today\'s Gym Plan</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Your personalised session for today</div>', unsafe_allow_html=True)

    quote = get_daily_quote("gym")
    st.markdown(f"""
    <div class="quran-card">
      <div class="quran-text">"{quote['text']}"</div>
      <div class="quran-ref">— {quote['reference']}</div>
    </div>
    """, unsafe_allow_html=True)

    plan = get_todays_gym_plan(profile)
    st.markdown(f"### {plan['day_name']}")
    st.caption(plan["focus"])

    for block in plan["blocks"]:
        st.markdown(f'<div class="gym-card"><div class="gym-title">{block["name"]}</div>', unsafe_allow_html=True)
        for ex in block["exercises"]:
            st.markdown(f'<div class="gym-item">• {ex}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if plan.get("cardio"):
        st.info(f"🚶 Cardio: {plan['cardio']}")
    if plan.get("rest_note"):
        st.success(plan["rest_note"])

    st.markdown("---")
    st.markdown("**⚠️ Always warm up 5 minutes before lifting. Form over weight every time.**")

# ── HUNGRY ────────────────────────────────────────────────────────────────────
elif page == "🥗 I'm Hungry":
    from utils.hungry import get_hungry_fix
    from datetime import datetime

    profile = st.session_state.active_profile
    if not profile:
        st.warning("Please set up your profile first.")
        st.stop()

    name = profile["name"]
    now = datetime.now()
    hour = now.hour + now.minute / 60

    st.markdown("<div class='main-title'>🥗 I'm Hungry</div>", unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Quick fix between meals · Keeps you on plan</div>', unsafe_allow_html=True)

    # Show current time and next meal
    from utils.hungry import get_next_meal
    next_meal, hours_until = get_next_meal(hour)
    h = int(hours_until)
    m = int((hours_until - h) * 60)
    time_str = f"{h}h {m}m" if h > 0 else f"{m} minutes"

    col1, col2 = st.columns(2)
    col1.metric("Time now", now.strftime("%H:%M"))
    col2.metric("Next meal", f"{next_meal.title()} in {time_str}")

    st.markdown("---")

    # Ask home or out
    st.markdown("### Where are you right now?")
    location_choice = st.radio(
        "Location",
        ["🏠 At home", "🏢 Out and about"],
        label_visibility="collapsed",
        horizontal=True
    )
    location = "home" if "home" in location_choice else "out"

    if st.button("Tell me what to eat →", type="primary"):
        result = get_hungry_fix(location, profile)
        fix = result["fix"]

        st.markdown("---")

        if result["type"] == "closed":
            st.error(f"⛔ **{fix['name']}**")
            st.markdown(f"> {fix['method']}")
            st.caption(fix['why'])

        elif result["type"] == "wait":
            st.warning(f"⏱ **{fix['name']}**")
            st.markdown(f"Your next meal ({result['next_meal']}) is only **{time_str}** away.")
            st.markdown(f"> {fix['method']}")
            st.caption(fix['why'])

        else:
            icon = "🏠" if location == "home" else "🏢"
            st.markdown(f"""
            <div class="hungry-card">
              <div class="hungry-title">{icon} {fix['name']}</div>
              <div class="hungry-item">⏱ {fix['time']} · ~{fix['calories']} kcal · {fix['protein']}g protein</div>
              <div class="hungry-item" style="margin-top:8px">{fix['method']}</div>
              <div class="hungry-item" style="margin-top:6px; color:#888"><em>Why this works: {fix['why']}</em></div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("---")
            st.caption(f"Next meal: {result['next_meal'].title()} in {time_str}. Hold on until then.")

# ── SHOPPING LIST ─────────────────────────────────────────────────────────────
elif page == "🛒 Shopping List":
    from utils.shopping import get_weekly_shopping_list
    from datetime import date as date_cls
    week_number = date_cls.today().isocalendar()[1] % 4
    week_labels = ["Week A", "Week B", "Week C", "Week D"]
    week_label = week_labels[week_number]

    st.markdown('<div class="main-title">🛒 Weekly Aldi Shopping List</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-title">{week_label} · For the whole family · Est. under £60 · Halal</div>', unsafe_allow_html=True)
    st.info(f"This is **{week_label}** of your 4-week rotation. The list updates automatically each week to match your meal plan.")

    shopping = get_weekly_shopping_list(week_number)
    total_est = 0
    for category, items in shopping.items():
        st.markdown(f'<div class="aldi-header">{category}</div>', unsafe_allow_html=True)
        for item in items:
            col1, col2, col3 = st.columns([0.5, 3, 1])
            col1.checkbox("", key=f"shop_{category}_{item['name']}")
            col2.markdown(f"<span style='font-size:13px'>{item['name']}</span>", unsafe_allow_html=True)
            col3.markdown(f"<span style='font-size:12px; color:#888'>{item['qty']}</span>", unsafe_allow_html=True)
            total_est += item.get("price", 0)

    st.markdown("---")
    st.metric("Estimated total", f"£{total_est:.2f}")
    st.caption("Prices based on Aldi UK typical costs. Halal meat from halal butcher or Aldi halal range.")

# ── PROGRESS ──────────────────────────────────────────────────────────────────
elif page == "📈 My Progress":
    import pandas as pd
    profile = st.session_state.active_profile
    if not profile:
        st.warning("Please set up your profile first.")
        st.stop()

    name = profile["name"]
    logs = load_logs(name)

    st.markdown(f'<div class="main-title">📈 {name}\'s Progress</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Your journey so far</div>', unsafe_allow_html=True)

    if not logs:
        st.info("No data yet. Complete your first daily check-in on the Dashboard.")
        st.stop()

    df = pd.DataFrame(logs)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    col1, col2, col3 = st.columns(3)
    start_w = profile["start_weight"]
    current_w = df["weight"].iloc[-1]
    lost = round(start_w - current_w, 1)
    to_go = round(current_w - profile["target"], 1)
    col1.metric("Started at", f"{start_w} st")
    col2.metric("Lost", f"{lost} st", delta=f"-{lost} st")
    col3.metric("Still to go", f"{to_go} st")

    st.markdown("### Weight over time")
    chart_df = df[["date", "weight"]].set_index("date")
    st.line_chart(chart_df)

    st.markdown("### Sleep over time")
    if "sleep" in df.columns:
        sleep_df = df[["date", "sleep"]].set_index("date")
        st.line_chart(sleep_df)

    st.markdown("### Energy over time")
    if "energy" in df.columns:
        energy_df = df[["date", "energy"]].set_index("date")
        st.line_chart(energy_df)

    st.markdown("---")
    st.markdown("### Check-in history")
    display_cols = ["date", "weight", "sleep", "energy", "trained", "sugar"]
    available = [c for c in display_cols if c in df.columns]
    st.dataframe(df[available].sort_values("date", ascending=False), use_container_width=True)

# ── WEEKLY MEAL PLAN ──────────────────────────────────────────────────────────
elif page == "🍽️ Weekly Meal Plan":
    from utils.meal_plans import (
        BREAKFASTS, LUNCHES, DINNERS, SNACKS, get_calorie_target
    )
    from datetime import date as date_cls

    # Rotate meals each week so content changes — 4 week cycle
    week_number = date_cls.today().isocalendar()[1] % 4
    def rotated(lst, n):
        n = n % len(lst)
        return lst[n:] + lst[:n]
    B = rotated(BREAKFASTS, week_number)
    L = rotated(LUNCHES, week_number)
    D = rotated(DINNERS, week_number)
    S = rotated(SNACKS, week_number)

    profile = st.session_state.active_profile
    if not profile:
        st.warning("Please set up your profile first.")
        st.stop()

    name = profile["name"]
    target = get_calorie_target(profile)

    st.markdown(f'<div class="main-title">🍽️ {name}\'s Weekly Meal Plan</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub-title">Every meal from your Aldi weekly shop · {target["target"]} kcal daily target</div>', unsafe_allow_html=True)

    st.info(f"📊 **Your daily target:** {target['target']} kcal · {target['note']}")

    # Lunch note for those eating out
    if name in ["Aquib", "Mariam"]:
        st.warning("🏢 You are out for lunch — each lunch day shows both a meal prep option and an out option.")

    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    for i, day in enumerate(DAYS):
        breakfast = B[i % 7]
        lunch     = L[i % 7]
        dinner    = D[i % 7]
        snack     = S[i % len(S)]

        with st.expander(f"📅 {day}", expanded=(i == 0)):

            # ── BREAKFAST ──
            st.markdown("#### 🌅 Breakfast")
            st.markdown(f"""
            <div class="hungry-card">
              <div class="hungry-title">{breakfast['name']}</div>
              <div class="hungry-item">⏱ {breakfast['time']} · 💰 {breakfast['cost']} · ~{breakfast['calories']} kcal · {breakfast['protein']}g protein</div>
              <div class="hungry-item" style="margin-top:6px"><strong>Ingredients:</strong> {breakfast['ingredients']}</div>
              <div class="hungry-item" style="margin-top:4px"><strong>Method:</strong> {breakfast['method']}</div>
            </div>
            """, unsafe_allow_html=True)

            # ── LUNCH ──
            st.markdown("#### ☀️ Lunch")

            # At home option
            st.markdown(f"""
            <div class="hungry-card">
              <div class="hungry-title">🏠 At home / meal prep — {lunch['name']}</div>
              <div class="hungry-item">⏱ {lunch['at_home']['prep']} · 💰 {lunch['at_home']['cost']} · ~{lunch['at_home']['calories']} kcal · {lunch['at_home']['protein']}g protein</div>
              <div class="hungry-item" style="margin-top:6px">{lunch['at_home']['instructions']}</div>
            </div>
            """, unsafe_allow_html=True)

            # Out option
            st.markdown(f"""
            <div class="gym-card">
              <div class="gym-title">🏢 If you are out — {lunch['name']}</div>
              <div class="gym-item">💰 {lunch['out']['cost']} · ~{lunch['out']['calories']} kcal · {lunch['out']['protein']}g protein</div>
              <div class="gym-item" style="margin-top:6px">{lunch['out']['instructions']}</div>
              <div class="gym-item" style="margin-top:4px; color:#888"><strong>Alternative:</strong> {lunch['out']['alternatives']}</div>
            </div>
            """, unsafe_allow_html=True)

            # ── SNACK ──
            st.markdown("#### 🍎 Afternoon Snack")
            st.markdown(f"""
            <div class="hungry-card">
              <div class="hungry-title">{snack['name']}</div>
              <div class="hungry-item">⏱ {snack['time']} · 💰 {snack['cost']} · ~{snack['calories']} kcal · {snack['protein']}g protein</div>
              <div class="hungry-item" style="margin-top:4px">{snack['method']}</div>
              <div class="hungry-item" style="margin-top:4px; color:#888"><strong>If out:</strong> {snack.get('out', 'Bring from home in a small container.')}</div>
            </div>
            """, unsafe_allow_html=True)

            # ── DINNER ──
            st.markdown("#### 🌙 Dinner")

            dinner_method = dinner['method']
            if name == "Mariam":
                dinner_method += " — Reduce portion by roughly a quarter."
            if name == "Yousaf":
                dinner_method += " — Add an extra egg or portion of rice to hit your calorie target."

            st.markdown(f"""
            <div class="hungry-card">
              <div class="hungry-title">{dinner['name']}</div>
              <div class="hungry-item">⏱ {dinner['time']} · 💰 {dinner['cost']} · ~{dinner['calories']} kcal · {dinner['protein']}g protein</div>
              <div class="hungry-item" style="margin-top:6px"><strong>Ingredients:</strong> {dinner['ingredients']}</div>
              <div class="hungry-item" style="margin-top:4px"><strong>Method:</strong> {dinner_method}</div>
            </div>
            """, unsafe_allow_html=True)

            # ── DAILY TOTAL ──
            daily_cals = breakfast['calories'] + lunch['at_home']['calories'] + snack['calories'] + dinner['calories']
            daily_protein = breakfast['protein'] + lunch['at_home']['protein'] + snack['protein'] + dinner['protein']
            def parse_cost(cost_str):
                # Handle ranges like £4-6, text like 'per portion', etc.
                import re
                nums = re.findall(r'[0-9]+\.?[0-9]*', cost_str)
                if not nums:
                    return 0.0
                return float(nums[0])

            daily_cost = (
                parse_cost(breakfast['cost']) +
                parse_cost(lunch['at_home']['cost']) +
                parse_cost(snack['cost']) +
                parse_cost(dinner['cost'])
            )

            st.markdown("---")
            col1, col2, col3 = st.columns(3)
            col1.metric("Day total", f"~{daily_cals} kcal",
                        delta=f"{daily_cals - target['target']:+} vs target")
            col2.metric("Protein", f"~{daily_protein}g")
            col3.metric("Food cost", f"~£{daily_cost:.2f}")

    st.markdown("---")
    st.markdown("### 📋 Meal prep tips")
    st.markdown("""
    **Sunday evening (30 min) — prep these for the whole week:**
    - Boil 6 eggs — grab 2 any time as a snack or breakfast
    - Cook a big pot of lentil soup — 4 lunch portions ready
    - Roast a tray of chicken thighs — use through the week cold in wraps or hot for dinner
    - Cook a batch of brown rice — base for 3 dinners
    - Portion Greek yogurt into small containers for grab-and-go breakfasts

    **This one Sunday session saves you cooking every single day.**
    """)
