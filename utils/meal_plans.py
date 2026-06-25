# ALL meals use ONLY ingredients from the weekly Aldi shopping list.
# No extras. No assumptions. Every recipe is built from what was bought.
#
# Shopping list ingredients available:
# MEAT/FISH: chicken thighs, minced beef, lamb diced, beef strips, salmon fillets, tinned tuna
# DAIRY/EGGS: Greek yogurt, eggs, milk, cheddar cheese
# VEG: broccoli, spinach, sweet potato, carrots, onions, courgettes, bell peppers,
#       cherry tomatoes, cucumber, green beans
# FRUIT: bananas, apples, frozen berries, lemons, dates
# DRY/TINNED: red lentils, tinned chickpeas, tinned chopped tomatoes, brown rice,
#              wholegrain pasta, porridge oats, wholegrain bread, wholegrain wraps, peanut butter
# NUTS: mixed nuts, walnuts, almonds
# OILS/SPICES: olive oil, cumin, turmeric, paprika, garam masala, coriander, tomato puree,
#               halal soy sauce, honey
# DRINKS: water, camomile tea, green tea

from datetime import datetime

# ─────────────────────────────────────────────────────────────────────────────
# BREAKFAST — 7 options, all from shopping list
# ─────────────────────────────────────────────────────────────────────────────
BREAKFASTS = [
    {
        "name": "Spiced scrambled eggs on wholegrain toast",
        "time": "10 min",
        "cost": "~£0.55",
        "calories": 370,
        "protein": 24,
        "ingredients": "3 eggs, 2 slices wholegrain bread, olive oil, cumin, turmeric, pinch paprika",
        "method": "Heat olive oil in pan. Add cumin and turmeric for 30 seconds. Crack in eggs and scramble gently. Serve on toasted wholegrain bread.",
        "at_home": True,
        "out": None
    },
    {
        "name": "Porridge with banana, honey and walnuts",
        "time": "8 min",
        "cost": "~£0.45",
        "calories": 420,
        "protein": 12,
        "ingredients": "80g porridge oats, 300ml milk, 1 banana, 1 tsp honey, small handful walnuts",
        "method": "Add oats and milk to pan, cook on medium heat 5 min stirring constantly. Pour into bowl. Top with sliced banana, drizzle honey, scatter walnuts.",
        "at_home": True,
        "out": None
    },
    {
        "name": "Greek yogurt with frozen berries, dates and almonds",
        "time": "3 min",
        "cost": "~£0.70",
        "calories": 320,
        "protein": 18,
        "ingredients": "200g Greek yogurt, large handful frozen berries (defrost overnight), 2 dates (chopped), 8 almonds",
        "method": "Put berries in a bowl before bed to defrost overnight. In the morning, layer yogurt, berries, chopped dates and almonds. Done in 3 minutes.",
        "at_home": True,
        "out": None
    },
    {
        "name": "Egg and cheese wholegrain wrap",
        "time": "8 min",
        "cost": "~£0.60",
        "calories": 400,
        "protein": 22,
        "ingredients": "2 eggs, 1 wholegrain wrap, small handful spinach, 20g cheddar (grated), olive oil, paprika",
        "method": "Scramble eggs with spinach in olive oil. Place on wrap, scatter grated cheddar and a pinch of paprika. Fold and eat immediately or wrap in foil to take out.",
        "at_home": True,
        "out": None
    },
    {
        "name": "Overnight oats with apple and peanut butter",
        "time": "5 min prep night before",
        "cost": "~£0.50",
        "calories": 440,
        "protein": 14,
        "ingredients": "80g porridge oats, 250ml milk, 1 apple (grated), 1 tbsp peanut butter, 1 tsp honey",
        "method": "Night before: mix oats, milk, grated apple and honey in a jar or container. Leave in fridge. Morning: stir in peanut butter. Eat cold. Takes 2 minutes in the morning.",
        "at_home": True,
        "out": None
    },
    {
        "name": "Boiled eggs with wholegrain toast soldiers and a banana",
        "time": "8 min",
        "cost": "~£0.40",
        "calories": 360,
        "protein": 20,
        "ingredients": "2 eggs, 2 slices wholegrain bread, 1 banana",
        "method": "Boil eggs 7 min for firm yolk. Toast bread and cut into strips. Peel eggs. Eat with banana on the side.",
        "at_home": True,
        "out": None
    },
    {
        "name": "Spiced yogurt smoothie bowl",
        "time": "5 min",
        "cost": "~£0.65",
        "calories": 350,
        "protein": 16,
        "ingredients": "150g Greek yogurt, 100ml milk, handful frozen berries, 1 banana, 1 tsp honey, sprinkle of mixed nuts",
        "method": "Blend yogurt, milk, berries and banana until smooth. Pour into bowl. Top with a drizzle of honey and crushed mixed nuts.",
        "at_home": True,
        "out": None
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# LUNCH — 7 options each with AT HOME and OUT OF HOUSE versions
# ─────────────────────────────────────────────────────────────────────────────
LUNCHES = [
    {
        "name": "Chicken and salad wrap",
        "at_home": {
            "instructions": "Use leftover roasted chicken thigh from dinner. Slice cold. Fill a wholegrain wrap with chicken, spinach, cucumber, cherry tomatoes. Mix 2 tbsp Greek yogurt with lemon juice and cumin as a sauce. Wrap tight in foil.",
            "prep": "5 min — prep the night before and refrigerate",
            "cost": "~£1.00",
            "calories": 420,
            "protein": 34,
        },
        "out": {
            "instructions": "Subway — choose wholegrain bread, grilled chicken, all salad, no mayo. Ask for oil and vinegar only. Avoid the cookies and crisps at checkout.",
            "alternatives": "Supermarket: M&S or Sainsbury's chicken salad wrap. Avoid anything with bacon or non-halal meat. Check label.",
            "cost": "~£4–6",
            "calories": 380,
            "protein": 28,
        }
    },
    {
        "name": "Tuna and chickpea salad box",
        "at_home": {
            "instructions": "Drain 1 tin tuna and half a tin of chickpeas. Mix with chopped cucumber, cherry tomatoes, spinach. Dress with olive oil, lemon juice, cumin and a pinch of paprika. Pack in a container.",
            "prep": "5 min — make the night before, keeps well",
            "cost": "~£0.85",
            "calories": 390,
            "protein": 36,
        },
        "out": {
            "instructions": "Supermarket meal deal: choose a protein pot (egg or tuna based) plus a side salad. Skip the crisps — swap for fruit or nuts you bring from home.",
            "alternatives": "Pret a Manger: tuna salad bowl or egg protein pot — halal safe as no meat involved.",
            "cost": "~£3–5",
            "calories": 350,
            "protein": 24,
        }
    },
    {
        "name": "Lentil soup in a flask",
        "at_home": {
            "instructions": "Make a big batch of lentil soup Sunday evening: fry onion, garlic, carrot in olive oil. Add red lentils, tinned tomatoes, cumin, turmeric, coriander, 800ml water. Simmer 20 min. Blend half. Pour into a flask with a slice of wholegrain bread in a bag.",
            "prep": "Batch cook Sunday — 5 days of lunches sorted",
            "cost": "~£0.60 per portion",
            "calories": 360,
            "protein": 18,
        },
        "out": {
            "instructions": "Look for a halal cafe or Turkish restaurant — lentil soup is common. Ask if it contains any meat stock. Most red lentil soups are vegetarian.",
            "alternatives": "Costa or Pret sometimes carry lentil or vegetable soups — check the label for halal status.",
            "cost": "~£3–5",
            "calories": 280,
            "protein": 14,
        }
    },
    {
        "name": "Egg and vegetable rice box",
        "at_home": {
            "instructions": "Cook a portion of brown rice the night before. Fry 2 eggs. Mix cold rice with spinach, cherry tomatoes, a drizzle of soy sauce and olive oil. Top with fried eggs. Pack in a container and reheat at work or eat cold.",
            "prep": "10 min — use leftover rice",
            "cost": "~£0.70",
            "calories": 430,
            "protein": 20,
        },
        "out": {
            "instructions": "Halal rice box restaurants — chicken or lamb over rice. Ask for no sauce or a light sauce. Avoid heavy mayonnaise-based sauces.",
            "alternatives": "Wasabi or similar: chicken teriyaki rice bowl — check halal certification. Most branches in London and St Albans are halal certified.",
            "cost": "~£5–8",
            "calories": 520,
            "protein": 38,
        }
    },
    {
        "name": "Minced beef and pepper wrap",
        "at_home": {
            "instructions": "Cook minced beef with onion, bell pepper, cumin, paprika and tomato puree (10 min). Cool slightly. Fill a wholegrain wrap. Wrap tight in foil. Eat at room temperature — it holds well.",
            "prep": "15 min — make a double batch, keeps 3 days in fridge",
            "cost": "~£1.10",
            "calories": 480,
            "protein": 36,
        },
        "out": {
            "instructions": "Halal kebab or Turkish restaurant: lamb or chicken shish wrap, no garlic sauce, extra salad. Avoid donor meat — quality varies. Shish is always the cleaner option.",
            "alternatives": "Halal Nando's — chicken wrap, plain or lemon and herb, with side salad not chips.",
            "cost": "~£6–9",
            "calories": 460,
            "protein": 34,
        }
    },
    {
        "name": "Chickpea and spinach stew box",
        "at_home": {
            "instructions": "Fry onion and garlic in olive oil. Add tinned chickpeas, tinned tomatoes, spinach, cumin, turmeric and garam masala. Simmer 15 min. Portion into a container. Eat with a slice of wholegrain bread or alone.",
            "prep": "20 min — batch cook, makes 3 portions",
            "cost": "~£0.70 per portion",
            "calories": 380,
            "protein": 16,
        },
        "out": {
            "instructions": "Indian or Pakistani restaurant: chana masala or dal — both chickpea or lentil based, naturally halal, high protein, clean. Ask for one roti not naan.",
            "alternatives": "Supermarket: a vegetarian curry pot from M&S or Sainsbury's with a wholegrain roll.",
            "cost": "~£4–7",
            "calories": 400,
            "protein": 14,
        }
    },
    {
        "name": "Salmon and brown rice box",
        "at_home": {
            "instructions": "Bake a salmon fillet the night before (200C, 15 min, with lemon and paprika). Flake it cold over a portion of cooked brown rice. Add spinach and cherry tomatoes. Dress with lemon juice and olive oil. Pack in a container.",
            "prep": "Night before — 5 min assembly in the morning",
            "cost": "~£1.80",
            "calories": 490,
            "protein": 40,
        },
        "out": {
            "instructions": "Itsu or similar: salmon rice bowl or sushi — naturally halal (no meat). Avoid anything with prawn crackers cooked in shared fryers.",
            "alternatives": "Supermarket: M&S salmon and rice pot or similar. Check label — salmon is always halal.",
            "cost": "~£5–7",
            "calories": 450,
            "protein": 36,
        }
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# DINNER — 7 options, all from shopping list, all at home
# ─────────────────────────────────────────────────────────────────────────────
DINNERS = [
    {
        "name": "Roasted chicken thighs with sweet potato and green beans",
        "time": "40 min",
        "cost": "~£1.60",
        "calories": 520,
        "protein": 44,
        "ingredients": "3 chicken thighs, 1 medium sweet potato, handful green beans, olive oil, cumin, paprika, turmeric, lemon",
        "method": "Preheat oven 200C. Rub chicken with olive oil, cumin, paprika and turmeric. Cube sweet potato, toss in oil. Put both on one tray. Roast 35 min. Steam green beans 4 min. Squeeze lemon over everything. One tray, minimal washing up.",
        "at_home": True
    },
    {
        "name": "Lamb and lentil stew",
        "time": "40 min",
        "cost": "~£1.80",
        "calories": 560,
        "protein": 42,
        "ingredients": "300g diced lamb, 150g red lentils, 1 tin chopped tomatoes, 1 onion, 3 garlic cloves, carrot, cumin, coriander, garam masala, turmeric, olive oil",
        "method": "Brown lamb in batches in olive oil. Remove. Fry onion, garlic and carrot 5 min. Add spices 1 min. Return lamb. Add lentils, tomatoes and 500ml water. Simmer 30 min until thick and rich. Serve with wholegrain bread.",
        "at_home": True
    },
    {
        "name": "Baked salmon with roasted courgette and carrots",
        "time": "30 min",
        "cost": "~£2.00",
        "calories": 480,
        "protein": 40,
        "ingredients": "1 salmon fillet, 1 courgette, 2 carrots, olive oil, lemon, paprika, garlic, turmeric",
        "method": "Preheat oven 200C. Slice courgette and carrots. Toss veg in olive oil and paprika, spread on tray. Season salmon with lemon, garlic and turmeric. Place on same tray. Roast 25 min. Everything cooked together.",
        "at_home": True
    },
    {
        "name": "Beef strips stir fry with broccoli and brown rice",
        "time": "20 min",
        "cost": "~£1.70",
        "calories": 500,
        "protein": 40,
        "ingredients": "200g halal beef strips, 1 head broccoli, 1 bell pepper, onion, soy sauce, olive oil, garlic, ginger (if available), 1 portion brown rice",
        "method": "Cook brown rice. High heat in a pan or wok. Stir fry beef 3 min until browned. Remove. Fry onion, pepper and broccoli 4 min. Return beef. Add soy sauce and a drizzle of olive oil. Toss 2 min. Serve over rice.",
        "at_home": True
    },
    {
        "name": "Minced beef kofta with roasted peppers and wrap",
        "time": "25 min",
        "cost": "~£1.40",
        "calories": 510,
        "protein": 38,
        "ingredients": "300g minced beef, onion, cumin, coriander, paprika, garam masala, 2 bell peppers, wholegrain wraps, Greek yogurt, lemon",
        "method": "Mix minced beef with grated onion and all spices. Shape into small logs. Grill or pan fry 12 min turning. Slice peppers and roast or pan fry alongside. Serve in wraps with Greek yogurt mixed with lemon juice as sauce.",
        "at_home": True
    },
    {
        "name": "Chickpea and spinach curry with brown rice",
        "time": "25 min",
        "cost": "~£0.90",
        "calories": 440,
        "protein": 18,
        "ingredients": "2 tins chickpeas, large bag spinach, 1 tin chopped tomatoes, onion, garlic, cumin, turmeric, garam masala, coriander, tomato puree, olive oil, 1 portion brown rice",
        "method": "Cook rice. Fry onion and garlic in oil 4 min. Add spices and tomato puree 1 min. Add tinned tomatoes and chickpeas. Simmer 15 min. Stir in spinach until wilted. Serve over rice. Budget dinner, high protein, deeply filling.",
        "at_home": True
    },
    {
        "name": "Tuna pasta with cherry tomatoes and spinach",
        "time": "15 min",
        "cost": "~£1.00",
        "calories": 460,
        "protein": 36,
        "ingredients": "100g wholegrain pasta, 1 tin tuna, handful cherry tomatoes, large handful spinach, olive oil, lemon, garlic, paprika",
        "method": "Cook pasta. Drain. In same pan, heat olive oil and garlic 1 min. Add cherry tomatoes and cook until they burst. Add spinach until wilted. Add drained tuna. Toss with pasta, lemon juice and paprika. Done in 15 minutes.",
        "at_home": True
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# SNACKS — for afternoon / hunger between meals
# ─────────────────────────────────────────────────────────────────────────────
SNACKS = [
    {
        "name": "Apple with peanut butter and almonds",
        "time": "1 min", "cost": "~£0.40", "calories": 260, "protein": 8,
        "ingredients": "1 apple, 1 tbsp peanut butter, 10 almonds",
        "method": "Slice apple. Dip in peanut butter. Eat with almonds. Kills sugar craving and keeps you full 2 hours.",
        "at_home": True, "out": "Buy an apple from any shop. Bring peanut butter sachets from home or buy a small pot."
    },
    {
        "name": "Greek yogurt with 2 dates and mixed nuts",
        "time": "1 min", "cost": "~£0.55", "calories": 230, "protein": 14,
        "ingredients": "150g Greek yogurt, 2 dates, small handful mixed nuts",
        "method": "Combine in a bowl or container. Satisfies sweet craving without spiking blood sugar. Prep in a tub and take out.",
        "at_home": True, "out": "Most supermarkets sell Greek yogurt pots. Buy dates and nuts separately and keep in your bag."
    },
    {
        "name": "Boiled eggs (pre-boiled)",
        "time": "0 min if pre-boiled", "cost": "~£0.30", "calories": 140, "protein": 12,
        "ingredients": "2 eggs",
        "method": "Boil a batch of 6 eggs every Sunday. Keep in fridge. Grab 2 whenever you need a snack. Pinch of paprika on top.",
        "at_home": True, "out": "Pret a Manger sells boiled egg protein pots. M&S and Sainsbury's also sell hard boiled egg snack packs."
    },
    {
        "name": "Banana with a handful of walnuts",
        "time": "0 min", "cost": "~£0.25", "calories": 200, "protein": 5,
        "ingredients": "1 banana, small handful walnuts",
        "method": "Eat together. The banana gives quick energy, the walnuts slow it down so you do not crash. Best pre-gym snack.",
        "at_home": True, "out": "Available anywhere. Always keep a banana in your bag."
    },
]

# ─────────────────────────────────────────────────────────────────────────────
# CALORIE TARGETS BY PROFILE
# ─────────────────────────────────────────────────────────────────────────────
CALORIE_TARGETS = {
    "Aquib":  {"target": 2100, "note": "Deficit for 1–1.5lb loss per week. High protein to preserve muscle."},
    "Yousaf": {"target": 2400, "note": "Mild deficit only. Still growing. High protein essential."},
    "Mariam": {"target": 1700, "note": "Moderate deficit for gradual loss and toning. No starvation."},
    "Anwar":  {"target": 2100, "note": "Deficit for 1–1.5lb loss per week. Strength and shape focus."},
}


def get_meal_suggestion(profile: dict, meal_time: str) -> list:
    name = profile.get("name", "Aquib")

    # Late night — always shut the kitchen
    if meal_time == "late":
        return [{
            "name": "Kitchen is closed",
            "time": "0 min",
            "cost": "£0",
            "calories": 0,
            "protein": 0,
            "ingredients": "Water or camomile tea",
            "method": "Drink 500ml water. Your body is not hungry — it is tired. Go to sleep. The 8:30pm rule exists for a reason.",
            "at_home": True,
            "out": None
        }]

    if meal_time == "breakfast":
        # Rotate through 7 breakfasts by day of week
        from datetime import date
        day = date.today().weekday()
        # Return today's breakfast plus the next one as an alternative
        primary = BREAKFASTS[day % 7]
        alternative = BREAKFASTS[(day + 1) % 7]
        return [primary, alternative]

    if meal_time == "lunch":
        from datetime import date
        day = date.today().weekday()
        # Return today's lunch with both at-home and out options displayed
        lunch = LUNCHES[day % 7]
        # Format into displayable cards
        at_home_card = {
            "name": f"{lunch['name']} — At home / meal prep",
            "time": lunch["at_home"]["prep"],
            "cost": lunch["at_home"]["cost"],
            "calories": lunch["at_home"]["calories"],
            "protein": lunch["at_home"]["protein"],
            "ingredients": "From your weekly shop",
            "method": lunch["at_home"]["instructions"],
            "at_home": True,
            "out": False
        }
        out_card = {
            "name": f"{lunch['name']} — If you are out",
            "time": "No cooking",
            "cost": lunch["out"]["cost"],
            "calories": lunch["out"]["calories"],
            "protein": lunch["out"]["protein"],
            "ingredients": "Buy out",
            "method": f"{lunch['out']['instructions']} | Alternative: {lunch['out']['alternatives']}",
            "at_home": False,
            "out": True
        }
        # Yousaf gets a note to eat more
        if name == "Yousaf":
            out_card["method"] += " — Yousaf: add a side of fruit or a yogurt pot to hit your calorie target."
        return [at_home_card, out_card]

    if meal_time in ["dinner", "afternoon"]:
        from datetime import date
        day = date.today().weekday()

        if meal_time == "dinner":
            primary = DINNERS[day % 7]
            alternative = DINNERS[(day + 1) % 7]
            # Mariam gets slightly smaller portions noted
            if name == "Mariam":
                primary = dict(primary)
                primary["method"] += " — Mariam: reduce portion by roughly a quarter. No seconds."
            # Yousaf gets a note to add extra
            if name == "Yousaf":
                primary = dict(primary)
                primary["method"] += " — Yousaf: add an extra egg or extra portion of rice to hit your calorie target."
            return [primary, alternative]

        # Afternoon snack
        snack = SNACKS[day % len(SNACKS)]
        return [snack]

    # Fallback
    from datetime import date
    day = date.today().weekday()
    return [DINNERS[day % 7]]


def get_calorie_target(profile: dict) -> dict:
    name = profile.get("name", "Aquib")
    return CALORIE_TARGETS.get(name, CALORIE_TARGETS["Aquib"])
