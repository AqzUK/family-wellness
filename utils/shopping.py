# Weekly shopping list rotates across 4 weeks for variety.
# All items are halal. All meals in the meal plan use only these ingredients.
# Target: under £65 per week including all spices (one-off first week buy).
# Ongoing weekly shop (without spices): ~£55-60

# CORE items that appear every week — the foundation
CORE = {
    "🥛 Dairy & Eggs": [
        {"name": "Full fat Greek yogurt", "qty": "1kg tub", "price": 2.20},
        {"name": "Free range eggs", "qty": "12 pack", "price": 2.00},
        {"name": "Semi-skimmed milk", "qty": "4 pints", "price": 1.45},
    ],
    "🍌 Fresh Fruit": [
        {"name": "Bananas", "qty": "5 pack", "price": 0.55},
        {"name": "Apples", "qty": "6 pack", "price": 1.09},
        {"name": "Frozen mixed berries", "qty": "500g bag", "price": 1.89},
        {"name": "Lemons", "qty": "4 pack", "price": 0.59},
        {"name": "Dates", "qty": "200g", "price": 1.49},
    ],
    "🌾 Dry & Tinned Staples (every week)": [
        {"name": "Tinned chopped tomatoes", "qty": "4 tins", "price": 1.40},
        {"name": "Porridge oats", "qty": "1kg", "price": 0.99},
        {"name": "Wholegrain bread", "qty": "800g loaf", "price": 1.09},
        {"name": "Wholegrain wraps", "qty": "6 pack", "price": 1.29},
        {"name": "Peanut butter (no added sugar)", "qty": "340g", "price": 1.59},
    ],
    "🥜 Nuts (every week)": [
        {"name": "Mixed nuts (unsalted)", "qty": "200g", "price": 1.99},
        {"name": "Almonds", "qty": "200g", "price": 1.89},
    ],
    "💧 Drinks": [
        {"name": "Still water", "qty": "6 x 2L", "price": 2.40},
        {"name": "Camomile tea bags", "qty": "20 pack", "price": 0.85},
        {"name": "Green tea bags", "qty": "20 pack", "price": 0.79},
    ],
}

# WEEK-SPECIFIC items — protein and veg rotate each week
WEEK_VARIANTS = {
    0: {  # Week A
        "label": "Week A",
        "🥩 Meat & Fish": [
            {"name": "Halal chicken thighs (bone-in)", "qty": "2kg", "price": 5.50},
            {"name": "Salmon fillets", "qty": "4 pack", "price": 5.50},
            {"name": "Tinned tuna in spring water", "qty": "4 tins", "price": 2.40},
            {"name": "Halal minced beef (5% fat)", "qty": "500g", "price": 3.20},
        ],
        "🥦 Fresh Vegetables": [
            {"name": "Broccoli", "qty": "2 heads", "price": 1.00},
            {"name": "Spinach (bag)", "qty": "300g", "price": 0.89},
            {"name": "Sweet potatoes", "qty": "1kg bag", "price": 1.29},
            {"name": "Carrots", "qty": "1kg bag", "price": 0.45},
            {"name": "Onions", "qty": "1.5kg bag", "price": 0.99},
            {"name": "Bell peppers (mixed)", "qty": "3 pack", "price": 1.19},
            {"name": "Cherry tomatoes", "qty": "400g punnet", "price": 0.99},
            {"name": "Green beans", "qty": "300g", "price": 0.69},
        ],
        "🌾 Dry & Tinned (this week)": [
            {"name": "Red lentils", "qty": "500g", "price": 0.89},
            {"name": "Brown rice", "qty": "1kg", "price": 1.19},
            {"name": "Tinned chickpeas", "qty": "2 tins", "price": 0.98},
        ],
    },
    1: {  # Week B
        "label": "Week B",
        "🥩 Meat & Fish": [
            {"name": "Halal lamb diced (stew cuts)", "qty": "500g", "price": 4.50},
            {"name": "Halal beef strips (stir fry)", "qty": "400g", "price": 3.80},
            {"name": "Halal chicken thighs (bone-in)", "qty": "1.5kg", "price": 4.20},
            {"name": "Tinned tuna in spring water", "qty": "4 tins", "price": 2.40},
        ],
        "🥦 Fresh Vegetables": [
            {"name": "Courgettes", "qty": "3 pack", "price": 0.89},
            {"name": "Spinach (bag)", "qty": "300g", "price": 0.89},
            {"name": "Sweet potatoes", "qty": "1kg bag", "price": 1.29},
            {"name": "Onions", "qty": "1.5kg bag", "price": 0.99},
            {"name": "Carrots", "qty": "1kg bag", "price": 0.45},
            {"name": "Cucumber", "qty": "1", "price": 0.45},
            {"name": "Cherry tomatoes", "qty": "400g punnet", "price": 0.99},
            {"name": "Broccoli", "qty": "1 head", "price": 0.55},
        ],
        "🌾 Dry & Tinned (this week)": [
            {"name": "Wholegrain pasta", "qty": "500g", "price": 0.89},
            {"name": "Brown rice", "qty": "1kg", "price": 1.19},
            {"name": "Red lentils", "qty": "500g", "price": 0.89},
        ],
    },
    2: {  # Week C
        "label": "Week C",
        "🥩 Meat & Fish": [
            {"name": "Halal chicken thighs (bone-in)", "qty": "2kg", "price": 5.50},
            {"name": "Halal minced beef (5% fat)", "qty": "500g", "price": 3.20},
            {"name": "Salmon fillets", "qty": "4 pack", "price": 5.50},
            {"name": "Tinned tuna in spring water", "qty": "2 tins", "price": 1.20},
        ],
        "🥦 Fresh Vegetables": [
            {"name": "Bell peppers (mixed)", "qty": "3 pack", "price": 1.19},
            {"name": "Broccoli", "qty": "2 heads", "price": 1.00},
            {"name": "Spinach (bag)", "qty": "300g", "price": 0.89},
            {"name": "Onions", "qty": "1.5kg bag", "price": 0.99},
            {"name": "Sweet potatoes", "qty": "1kg bag", "price": 1.29},
            {"name": "Green beans", "qty": "300g", "price": 0.69},
            {"name": "Courgettes", "qty": "3 pack", "price": 0.89},
        ],
        "🌾 Dry & Tinned (this week)": [
            {"name": "Tinned chickpeas", "qty": "2 tins", "price": 0.98},
            {"name": "Brown rice", "qty": "1kg", "price": 1.19},
            {"name": "Wholegrain pasta", "qty": "500g", "price": 0.89},
        ],
    },
    3: {  # Week D
        "label": "Week D",
        "🥩 Meat & Fish": [
            {"name": "Halal lamb diced (stew cuts)", "qty": "750g", "price": 6.75},
            {"name": "Halal beef strips (stir fry)", "qty": "400g", "price": 3.80},
            {"name": "Tinned tuna in spring water", "qty": "4 tins", "price": 2.40},
            {"name": "Salmon fillets", "qty": "2 pack", "price": 3.00},
        ],
        "🥦 Fresh Vegetables": [
            {"name": "Carrots", "qty": "1kg bag", "price": 0.45},
            {"name": "Onions", "qty": "1.5kg bag", "price": 0.99},
            {"name": "Spinach (bag)", "qty": "300g", "price": 0.89},
            {"name": "Sweet potatoes", "qty": "1kg bag", "price": 1.29},
            {"name": "Cucumber", "qty": "1", "price": 0.45},
            {"name": "Cherry tomatoes", "qty": "400g punnet", "price": 0.99},
            {"name": "Broccoli", "qty": "1 head", "price": 0.55},
        ],
        "🌾 Dry & Tinned (this week)": [
            {"name": "Red lentils", "qty": "500g", "price": 0.89},
            {"name": "Tinned chickpeas", "qty": "2 tins", "price": 0.98},
            {"name": "Brown rice", "qty": "1kg", "price": 1.19},
        ],
    },
}

# Spices — one off buy, remind user every 4 weeks
SPICES = {
    "🧴 Oils & Spices (top up as needed — not every week)": [
        {"name": "Olive oil", "qty": "500ml", "price": 2.99},
        {"name": "Cumin (ground)", "qty": "jar", "price": 0.85},
        {"name": "Turmeric (ground)", "qty": "jar", "price": 0.85},
        {"name": "Paprika (smoked)", "qty": "jar", "price": 0.85},
        {"name": "Garam masala", "qty": "jar", "price": 0.85},
        {"name": "Coriander (ground)", "qty": "jar", "price": 0.85},
        {"name": "Tomato puree", "qty": "2 tubes", "price": 0.98},
        {"name": "Halal soy sauce", "qty": "150ml", "price": 0.89},
        {"name": "Honey (jar)", "qty": "340g", "price": 1.59},
        {"name": "Cheddar cheese (block)", "qty": "400g", "price": 2.10},
        {"name": "Walnuts", "qty": "100g", "price": 1.09},
    ]
}


def get_weekly_shopping_list(week_number: int = 0) -> dict:
    week_number = week_number % 4
    variant = WEEK_VARIANTS[week_number]
    result = {}

    # Week-specific protein and veg first
    for key in ["🥩 Meat & Fish", "🥦 Fresh Vegetables", "🌾 Dry & Tinned (this week)"]:
        if key in variant:
            result[key] = variant[key]

    # Core items every week
    for key, items in CORE.items():
        result[key] = items

    # Spices — always show but mark as top-up
    for key, items in SPICES.items():
        result[key] = items

    return result
