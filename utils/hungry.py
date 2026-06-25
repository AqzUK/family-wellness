# I'm Hungry — emergency craving fixes BETWEEN meals
# All from the weekly shopping list. Under 5 minutes. Keeps you on plan.

from datetime import datetime

# Meal times — used to calculate how far away next meal is
MEAL_TIMES = {
    "breakfast": 7.5,   # 7:30am
    "lunch":     13.0,  # 1:00pm
    "dinner":    18.5,  # 6:30pm
}

def get_next_meal(hour: float) -> tuple:
    """Return (next_meal_name, hours_until) based on current time."""
    if hour < 7.5:
        return "breakfast", round(7.5 - hour, 1)
    elif hour < 13.0:
        return "lunch", round(13.0 - hour, 1)
    elif hour < 18.5:
        return "dinner", round(18.5 - hour, 1)
    else:
        return "tomorrow's breakfast", round((24 - hour) + 7.5, 1)

# ─────────────────────────────────────────────────────────────────────────────
# AT HOME FIXES — all from Aldi shopping list, under 5 min
# ─────────────────────────────────────────────────────────────────────────────
AT_HOME_FIXES = [
    {
        "name": "Greek yogurt with 2 dates",
        "time": "1 min",
        "calories": 180,
        "protein": 12,
        "method": "Spoon 150g Greek yogurt into a bowl. Add 2 dates. Eat slowly. High protein, naturally sweet — kills sugar cravings fast.",
        "why": "Protein and natural sugar stop the craving without spiking your blood sugar."
    },
    {
        "name": "Apple with a tablespoon of peanut butter",
        "time": "1 min",
        "calories": 200,
        "protein": 6,
        "method": "Slice an apple. Dip in peanut butter. Eat it slowly. That is it.",
        "why": "Fibre from the apple plus fat and protein from peanut butter — this holds you for 90 minutes minimum."
    },
    {
        "name": "Handful of mixed nuts and almonds",
        "time": "0 min",
        "calories": 170,
        "protein": 5,
        "method": "A small handful — roughly 20–25 nuts total. Eat slowly. Drink a full glass of water with it.",
        "why": "Most cravings are actually thirst. Nuts plus water is the fastest craving killer."
    },
    {
        "name": "2 boiled eggs (pre-boiled from the fridge)",
        "time": "0 min if pre-boiled · 8 min if not",
        "calories": 140,
        "protein": 12,
        "method": "Grab 2 boiled eggs from the fridge. Sprinkle paprika. Done. If you have not pre-boiled — boil 6 right now for the rest of the week.",
        "why": "Highest protein per calorie of anything on your shopping list. Zero sugar spike."
    },
    {
        "name": "Banana with a handful of walnuts",
        "time": "0 min",
        "calories": 200,
        "protein": 4,
        "method": "Eat the banana first, then the walnuts. The combination of fast and slow energy stops the crash.",
        "why": "Good option if you are about to train or need energy. Not ideal late evening."
    },
    {
        "name": "500ml water and green tea",
        "time": "2 min",
        "calories": 0,
        "protein": 0,
        "method": "Drink 500ml water first. Make a green tea. Wait 10 minutes. Most cravings disappear entirely.",
        "why": "Your brain confuses thirst for hunger 60% of the time. Always try water first."
    },
    {
        "name": "Small bowl of porridge oats with honey",
        "time": "5 min",
        "calories": 220,
        "protein": 6,
        "method": "50g oats, 150ml milk or water, microwave 2 min or cook 3 min. Drizzle honey. Eat slowly.",
        "why": "Slow release carbs — fills you up without spiking blood sugar. Best option if dinner is still 3+ hours away."
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# OUT OF HOUSE FIXES — specific places and what to buy
# ─────────────────────────────────────────────────────────────────────────────
OUT_FIXES = [
    {
        "name": "Supermarket protein pot",
        "time": "2 min to grab",
        "calories": 150,
        "protein": 12,
        "method": "M&S, Sainsbury's or Tesco: grab a boiled egg protein pot or Greek yogurt pot. Avoid anything with pastry, crisps or chocolate.",
        "why": "High protein, low calorie, available everywhere."
    },
    {
        "name": "Banana from any shop",
        "time": "1 min",
        "calories": 100,
        "protein": 1,
        "method": "Buy a banana. Eat it slowly. Drink water with it.",
        "why": "Cheapest craving fix available anywhere. Under 30p."
    },
    {
        "name": "Small bag of unsalted nuts",
        "time": "1 min",
        "calories": 170,
        "protein": 5,
        "method": "Most supermarkets and petrol stations sell small mixed nut bags. Unsalted only. Avoid the ones coated in honey or chocolate.",
        "why": "Portable, filling, no sugar spike."
    },
    {
        "name": "Greek yogurt pot — any supermarket",
        "time": "1 min",
        "calories": 130,
        "protein": 10,
        "method": "Fage 0% or Total Greek yogurt from any supermarket. Avoid flavoured ones — they are full of sugar. Plain only.",
        "why": "Best protein to calorie ratio of anything you can buy ready-made."
    },
    {
        "name": "Water and wait",
        "time": "0 min",
        "calories": 0,
        "protein": 0,
        "method": "Buy a large still water. Drink the whole bottle over 10 minutes. Walk if you can. Most cravings gone by then.",
        "why": "Free. Works. Always try this first before spending money on a snack."
    },
    {
        "name": "Pret a Manger — boiled egg pot or fruit pot",
        "time": "3 min",
        "calories": 120,
        "protein": 8,
        "method": "Pret: boiled egg pot, or a fruit pot (berries only, not the tropical mix which is high sugar). Avoid the pastries and sandwiches.",
        "why": "Clean options that keep you on plan without a full meal."
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# AFTER 9PM — no food, no exceptions
# ─────────────────────────────────────────────────────────────────────────────
LATE_NIGHT_RESPONSE = {
    "name": "Kitchen is closed — drink water",
    "time": "0 min",
    "calories": 0,
    "protein": 0,
    "method": "Drink 500ml water. Make camomile tea. Go to bed. You are not hungry — you are either bored, tired, or your body is adjusting to the new routine. Night eating is your single biggest blocker. Hold the line.",
    "why": "Every time you close the kitchen after 8:30pm and sleep instead, you are winning. This is where the weight comes off."
}

# ─────────────────────────────────────────────────────────────────────────────
# CLOSE TO MEAL — tell them to wait
# ─────────────────────────────────────────────────────────────────────────────
WAIT_RESPONSE = {
    "name": "Wait — your meal is coming soon",
    "time": "0 min",
    "calories": 0,
    "protein": 0,
    "method": "Drink 500ml water right now. Your next meal is less than 45 minutes away. A craving that close to a meal is almost always thirst or habit, not hunger. Hold on.",
    "why": "Eating between meals when your next meal is under 45 minutes away adds unnecessary calories and blunts your appetite for the proper meal."
}


def get_hungry_fix(location: str, profile: dict) -> dict:
    """
    Return the right craving fix based on:
    - Current time
    - Whether at home or out
    - How far away the next meal is
    - Profile (for personalisation)
    """
    now = datetime.now()
    hour = now.hour + now.minute / 60
    name = profile.get("name", "Aquib")

    # After 9pm — always close the kitchen
    if hour >= 21.0:
        return {"type": "closed", "fix": LATE_NIGHT_RESPONSE, "next_meal": "tomorrow's breakfast", "hours_until": round((24 - hour) + 7.5, 1)}

    next_meal, hours_until = get_next_meal(hour)

    # If next meal is under 45 min away — tell them to wait
    if hours_until <= 0.75:
        return {"type": "wait", "fix": WAIT_RESPONSE, "next_meal": next_meal, "hours_until": hours_until}

    # Pick the right fix based on location
    import random
    # Use time-based seed so it's consistent within the same hour
    seed = now.hour + now.day * 24
    random.seed(seed)

    if location == "home":
        # Pick best fit for time of day
        if hour < 10:
            # Morning — lighter options
            options = [AT_HOME_FIXES[0], AT_HOME_FIXES[1], AT_HOME_FIXES[5]]
        elif hour < 15:
            # Midday — more sustaining
            options = [AT_HOME_FIXES[1], AT_HOME_FIXES[2], AT_HOME_FIXES[3], AT_HOME_FIXES[6]]
        elif hour < 18:
            # Afternoon — snack to bridge to dinner
            options = [AT_HOME_FIXES[0], AT_HOME_FIXES[2], AT_HOME_FIXES[4]]
        else:
            # Evening before dinner
            options = [AT_HOME_FIXES[5], AT_HOME_FIXES[0], AT_HOME_FIXES[2]]

        fix = random.choice(options)

        # Yousaf can have slightly more — note it
        if name == "Yousaf":
            fix = dict(fix)
            fix["method"] += " — Yousaf: you can have a slightly larger portion given your calorie target."

    else:  # out
        if hour < 10:
            options = [OUT_FIXES[0], OUT_FIXES[1], OUT_FIXES[4]]
        elif hour < 15:
            options = [OUT_FIXES[0], OUT_FIXES[2], OUT_FIXES[3], OUT_FIXES[5]]
        elif hour < 18:
            options = [OUT_FIXES[1], OUT_FIXES[2], OUT_FIXES[3]]
        else:
            options = [OUT_FIXES[4], OUT_FIXES[0], OUT_FIXES[3]]

        fix = random.choice(options)

    return {
        "type": "fix",
        "fix": fix,
        "next_meal": next_meal,
        "hours_until": hours_until
    }
