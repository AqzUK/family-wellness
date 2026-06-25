from datetime import datetime

# All meals: halal, cheap (Aldi-sourced), fulfilling, high protein where needed

MEALS = {
    "breakfast": [
        {
            "name": "Spiced scrambled eggs on toast",
            "time": "10 min",
            "cost": "~£0.60",
            "calories": 380,
            "protein": 24,
            "ingredients": "3 eggs, 2 slices wholegrain bread, cumin, turmeric, chilli flakes, olive oil",
            "method": "Heat oil, add spices for 30 sec, scramble eggs in. Serve on toast."
        },
        {
            "name": "Overnight oats with banana and honey",
            "time": "5 min (prep night before)",
            "cost": "~£0.40",
            "calories": 420,
            "protein": 14,
            "ingredients": "80g oats, 200ml milk, 1 banana, 1 tsp honey, cinnamon",
            "method": "Mix oats and milk, leave in fridge overnight. Top with banana and honey in morning."
        },
        {
            "name": "Full fat Greek yogurt with berries and walnuts",
            "time": "2 min",
            "cost": "~£0.80",
            "calories": 310,
            "protein": 18,
            "ingredients": "200g Greek yogurt, handful frozen berries (defrosted), 6 walnuts, drizzle honey",
            "method": "Layer yogurt, berries, nuts, drizzle honey. Done."
        },
    ],
    "lunch": [
        {
            "name": "Chicken and lentil dhal",
            "time": "25 min",
            "cost": "~£1.20",
            "calories": 520,
            "protein": 38,
            "ingredients": "2 chicken thighs (boneless), 150g red lentils, 1 tin chopped tomatoes, onion, garlic, ginger, cumin, coriander, turmeric, garam masala, oil",
            "method": "Fry onion, garlic, ginger 3 min. Add spices 1 min. Add chicken, brown 5 min. Add lentils, tomatoes, 400ml water. Simmer 20 min until thick. Serve with 1 small roti or rice."
        },
        {
            "name": "Lamb and vegetable stew",
            "time": "35 min",
            "cost": "~£1.80",
            "calories": 580,
            "protein": 42,
            "ingredients": "300g diced halal lamb, carrot, potato, onion, garlic, tomato puree, stock, cumin, paprika",
            "method": "Brown lamb in batches. Fry onion and garlic. Add veg, puree, spices, stock. Simmer 30 min. Hearty and filling."
        },
        {
            "name": "Tuna and chickpea salad",
            "time": "5 min",
            "cost": "~£0.90",
            "calories": 410,
            "protein": 34,
            "ingredients": "1 tin tuna, 1 tin chickpeas, cucumber, tomato, lemon, olive oil, cumin, salt",
            "method": "Drain tuna and chickpeas, mix everything together. Squeeze lemon, drizzle oil. Quick and high protein."
        },
        {
            "name": "Grilled chicken wrap",
            "time": "15 min",
            "cost": "~£1.10",
            "calories": 460,
            "protein": 36,
            "ingredients": "2 chicken thighs, wholegrain wrap, lettuce, cucumber, yogurt, garlic, lemon, chilli",
            "method": "Season and grill chicken 10–12 min. Slice. Mix yogurt, garlic, lemon for sauce. Wrap it all up."
        },
    ],
    "afternoon": [
        {
            "name": "Apple with peanut butter and handful of almonds",
            "time": "1 min",
            "cost": "~£0.40",
            "calories": 260,
            "protein": 8,
            "ingredients": "1 apple, 1 tbsp peanut butter (no added sugar), 12 almonds",
            "method": "Slice apple, dip in peanut butter. Eat with almonds. That is it."
        },
        {
            "name": "Greek yogurt with 2 dates and walnuts",
            "time": "1 min",
            "cost": "~£0.50",
            "calories": 220,
            "protein": 12,
            "ingredients": "150g Greek yogurt, 2 Medjool dates, 5 walnuts",
            "method": "Combine. Satisfies sweet craving without spiking blood sugar."
        },
        {
            "name": "Boiled eggs with a slice of wholegrain toast",
            "time": "8 min",
            "cost": "~£0.30",
            "calories": 240,
            "protein": 16,
            "ingredients": "2 eggs, 1 slice wholegrain toast, pinch of salt",
            "method": "Boil eggs 7 min for firm yolk. Toast bread. Eat."
        },
    ],
    "dinner": [
        {
            "name": "Baked salmon with roasted sweet potato and green beans",
            "time": "30 min",
            "cost": "~£2.20",
            "calories": 520,
            "protein": 40,
            "ingredients": "1 salmon fillet, 1 medium sweet potato, handful green beans, olive oil, garlic, lemon, paprika",
            "method": "Preheat oven 200C. Cube sweet potato, roast 20 min with oil and paprika. Season salmon, bake 15 min. Steam green beans 4 min. Squeeze lemon over everything."
        },
        {
            "name": "Halal beef stir-fry with brown rice",
            "time": "20 min",
            "cost": "~£1.60",
            "calories": 490,
            "protein": 38,
            "ingredients": "200g halal beef strips, broccoli, pepper, onion, garlic, soy sauce (halal), ginger, sesame oil, 1 portion brown rice",
            "method": "Cook rice. High heat wok, stir-fry beef 3 min. Remove. Fry veg 4 min. Add beef back, sauce, ginger, garlic. Toss 2 min. Serve on rice."
        },
        {
            "name": "Lentil soup with wholegrain bread",
            "time": "25 min",
            "cost": "~£0.70",
            "calories": 380,
            "protein": 22,
            "ingredients": "200g red lentils, onion, garlic, carrot, cumin, coriander, turmeric, lemon, olive oil, 1 slice bread",
            "method": "Fry onion and garlic in oil 3 min. Add spices 1 min. Add lentils, carrot, 800ml water. Simmer 20 min. Blend half for texture. Squeeze lemon. Serve with bread."
        },
        {
            "name": "Chicken thighs with roasted veg",
            "time": "40 min",
            "cost": "~£1.40",
            "calories": 480,
            "protein": 44,
            "ingredients": "3 chicken thighs (bone-in), courgette, pepper, onion, garlic, olive oil, cumin, paprika, turmeric",
            "method": "Preheat oven 200C. Rub chicken with spices and oil. Chop veg, toss in oil. Roast everything together 35–40 min. One tray, minimal washing up."
        },
    ],
    "late": [
        {
            "name": "Kitchen is closed",
            "time": "0 min",
            "cost": "£0",
            "calories": 0,
            "protein": 0,
            "ingredients": "Water or camomile tea",
            "method": "Drink 500ml water. Your body is not hungry — it is bored or tired. Go to sleep."
        }
    ]
}

# Yousaf gets slightly higher calorie options (growing teen)
YOUSAF_EXTRAS = {
    "lunch": [
        {
            "name": "Pasta with tuna and vegetables",
            "time": "15 min",
            "cost": "~£0.90",
            "calories": 620,
            "protein": 38,
            "ingredients": "100g wholegrain pasta, 1 tin tuna, cherry tomatoes, spinach, garlic, olive oil, parmesan",
            "method": "Cook pasta. Fry garlic in oil, add tomatoes, spinach, tuna. Toss with pasta."
        }
    ]
}


def get_meal_suggestion(profile: dict, meal_time: str) -> list:
    name = profile.get("name", "")
    pool = MEALS.get(meal_time, MEALS["lunch"])

    # Yousaf gets extra calorie options
    if name == "Yousaf" and meal_time in YOUSAF_EXTRAS:
        pool = pool + YOUSAF_EXTRAS[meal_time]

    # For Mariam, keep portions slightly smaller — return first 2
    if name == "Mariam" and len(pool) > 2:
        return pool[:2]

    # For late night — always return the kitchen-closed message
    if meal_time == "late":
        return pool

    # Return up to 3 suggestions
    return pool[:3]
