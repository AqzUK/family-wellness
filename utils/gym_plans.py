from datetime import date

# Day of week: 0=Mon, 1=Tue, 2=Wed, 3=Thu, 4=Fri, 5=Sat, 6=Sun

AQUIB_PLAN = {
    # MONDAY — Push
    0: {
        "day_name": "Monday — Push Day 💪",
        "focus": "Chest · Shoulders · Triceps — Build upper body strength",
        "blocks": [
            {
                "name": "Warm-up (5 min)",
                "exercises": [
                    "Arm circles x20 each direction",
                    "Band pull-aparts x15",
                    "Light dumbbell press x15 (very light)"
                ]
            },
            {
                "name": "Main lifts",
                "exercises": [
                    "Barbell bench press — 4 sets x 8 reps (rest 90 sec)",
                    "Overhead dumbbell press — 3 sets x 10 reps (rest 75 sec)",
                    "Incline dumbbell press — 3 sets x 10 reps (rest 75 sec)",
                    "Cable lateral raises — 3 sets x 12 reps (rest 60 sec)",
                ]
            },
            {
                "name": "Triceps finisher",
                "exercises": [
                    "Tricep rope pushdowns — 3 sets x 12 reps",
                    "Overhead tricep extension — 3 sets x 10 reps",
                ]
            }
        ],
        "cardio": "20 min brisk treadmill walk at 5–6 km/h after lifting. Not a run. Walk.",
    },
    # TUESDAY — Rest / Walk
    1: {
        "day_name": "Tuesday — Active Recovery 🚶",
        "focus": "Rest and light movement. Do not skip this — recovery is when you grow.",
        "blocks": [
            {
                "name": "Active recovery",
                "exercises": [
                    "30 min walk outside — brisk pace",
                    "10 min stretching: quads, hamstrings, chest, shoulders",
                    "Optional: 15 min swimming if available"
                ]
            }
        ],
        "rest_note": "The Prophet ﷺ said: 'Your body has a right over you.' (Bukhari 1975) — Rest IS part of the plan.",
    },
    # WEDNESDAY — Pull
    2: {
        "day_name": "Wednesday — Pull Day 🏋️",
        "focus": "Back · Biceps — Build the posterior chain",
        "blocks": [
            {
                "name": "Warm-up (5 min)",
                "exercises": [
                    "Cat-cow stretches x10",
                    "Band face pulls x15",
                    "Light Romanian deadlift x10 (bar only)"
                ]
            },
            {
                "name": "Main lifts",
                "exercises": [
                    "Deadlifts — 4 sets x 6 reps (rest 2 min — your biggest strength builder)",
                    "Lat pulldown — 3 sets x 10 reps (rest 75 sec)",
                    "Seated cable row — 3 sets x 10 reps (rest 75 sec)",
                    "Single-arm dumbbell row — 3 sets x 10 each side (rest 60 sec)",
                ]
            },
            {
                "name": "Biceps finisher",
                "exercises": [
                    "Barbell curl — 3 sets x 10 reps",
                    "Hammer curl — 3 sets x 12 reps",
                ]
            }
        ],
        "cardio": "20 min brisk treadmill walk after lifting.",
    },
    # THURSDAY — Rest / Walk
    3: {
        "day_name": "Thursday — Active Recovery 🚶",
        "focus": "Light day. Protect your joints. Eat well and sleep on time.",
        "blocks": [
            {
                "name": "Active recovery",
                "exercises": [
                    "30 min walk outside",
                    "Full body stretch 10 min",
                ]
            }
        ],
        "rest_note": "Use this day to prep your gym bag and plan tomorrow's session.",
    },
    # FRIDAY — Legs
    4: {
        "day_name": "Friday — Legs + Core 🦵",
        "focus": "Quads · Hamstrings · Glutes · Core — Your biggest muscle groups",
        "blocks": [
            {
                "name": "Warm-up (5 min)",
                "exercises": [
                    "Bodyweight squats x15",
                    "Hip circles x10 each side",
                    "Leg swings x10 each leg"
                ]
            },
            {
                "name": "Main lifts",
                "exercises": [
                    "Barbell squats — 4 sets x 8 reps (rest 2 min — prioritise depth and form)",
                    "Romanian deadlift — 3 sets x 10 reps (rest 90 sec)",
                    "Leg press — 3 sets x 12 reps (rest 75 sec)",
                    "Walking lunges — 3 sets x 12 each leg (rest 60 sec)",
                ]
            },
            {
                "name": "Core",
                "exercises": [
                    "Plank — 3 x 45 seconds",
                    "Dead bug — 3 x 10 each side",
                    "Pallof press — 3 x 10 each side",
                ]
            }
        ],
        "cardio": "20 min walk. No running on leg day — joints are loaded enough.",
    },
    # SATURDAY — Optional cardio
    5: {
        "day_name": "Saturday — Cardio & Mobility 🏊",
        "focus": "Optional session. Great for fat burn without joint stress.",
        "blocks": [
            {
                "name": "Choose one",
                "exercises": [
                    "30 min swim (excellent for your size — zero joint impact)",
                    "OR 30 min cycling (stationary or outdoors)",
                    "OR 45 min brisk walk",
                ]
            },
            {
                "name": "Mobility (10 min)",
                "exercises": [
                    "Hip flexor stretch — 60 sec each side",
                    "Thoracic rotation — 10 each side",
                    "Shoulder cross-body stretch — 60 sec each side"
                ]
            }
        ],
        "rest_note": "This is optional but recommended in the first 8 weeks.",
    },
    # SUNDAY — Full rest
    6: {
        "day_name": "Sunday — Full Rest 🌿",
        "focus": "Rest completely. Spend time with family. Recovery is growth.",
        "blocks": [
            {
                "name": "Rest day",
                "exercises": [
                    "No training required today",
                    "Light walk is fine if you feel good",
                    "Focus on sleep tonight — prepare for the week ahead",
                ]
            }
        ],
        "rest_note": "'The most beloved of deeds to Allah are those most consistent, even if small.' — Bukhari 6464. Consistency over intensity.",
    },
}

YOUSAF_PLAN = {
    # Monday — Upper body (bodyweight + light weights)
    0: {
        "day_name": "Monday — Upper Body 💪",
        "focus": "Form first. No ego lifting at 16. Growth comes from consistency.",
        "blocks": [
            {
                "name": "Warm-up",
                "exercises": ["Jumping jacks x30", "Arm circles x15 each", "Push-up x10 (slow)"]
            },
            {
                "name": "Session",
                "exercises": [
                    "Push-ups — 4 sets x 12 (controlled, chest to floor)",
                    "Dumbbell shoulder press — 3 sets x 10 (light weight, perfect form)",
                    "Lat pulldown or assisted pull-up — 3 sets x 10",
                    "Dumbbell row — 3 sets x 10 each side",
                    "Dumbbell curl — 3 sets x 12",
                ]
            }
        ],
        "cardio": "15 min jog or 25 min brisk walk after session.",
    },
    1: {
        "day_name": "Tuesday — Cardio + Core 🏃",
        "focus": "Cardiovascular fitness and core strength for a 16 year old.",
        "blocks": [
            {
                "name": "Session",
                "exercises": [
                    "20 min jog (conversational pace — you should be able to talk)",
                    "Plank — 3 x 30 seconds",
                    "Bicycle crunches — 3 x 15 each side",
                    "Leg raises — 3 x 12",
                ]
            }
        ],
    },
    2: {
        "day_name": "Wednesday — Lower Body 🦵",
        "focus": "Build leg strength safely — no heavy barbell squats until form is perfect.",
        "blocks": [
            {
                "name": "Session",
                "exercises": [
                    "Goblet squat (dumbbell) — 4 sets x 12",
                    "Romanian deadlift (light barbell) — 3 sets x 10",
                    "Leg press — 3 sets x 12",
                    "Calf raises — 3 sets x 15",
                    "Glute bridge — 3 sets x 15",
                ]
            }
        ],
        "cardio": "15 min walk after session.",
    },
    3: {"day_name": "Thursday — Rest 🌿", "focus": "Rest or light walk. School and study come first.", "blocks": [{"name": "Rest", "exercises": ["Light 20 min walk", "Stretch: hamstrings, quads, chest"]}]},
    4: {
        "day_name": "Friday — Full Body 🏋️",
        "focus": "One full-body session to finish the week strong.",
        "blocks": [
            {
                "name": "Session",
                "exercises": [
                    "Goblet squats — 3 x 12",
                    "Push-ups — 3 x 15",
                    "Dumbbell row — 3 x 10 each",
                    "Shoulder press — 3 x 10",
                    "Plank — 3 x 30 sec",
                ]
            }
        ],
        "cardio": "20 min jog or football with friends.",
    },
    5: {"day_name": "Saturday — Sport or Walk 🏃", "focus": "Play sport, go for a walk, enjoy being active.", "blocks": [{"name": "Activity", "exercises": ["Football / basketball / swimming — anything you enjoy", "OR 30 min walk with family"]}]},
    6: {"day_name": "Sunday — Full Rest 🌿", "focus": "Rest. You are still growing. Sleep is essential.", "blocks": [{"name": "Rest", "exercises": ["Sleep well tonight", "Prepare for the week"]}]},
}

MARIAM_PLAN = {
    0: {
        "day_name": "Monday — Tone: Upper Body 💪",
        "focus": "Resistance training tones the body. Cardio alone will not do it.",
        "blocks": [
            {
                "name": "Warm-up",
                "exercises": ["March on spot 2 min", "Arm circles x15", "Shoulder rolls x10"]
            },
            {
                "name": "Session (home or gym)",
                "exercises": [
                    "Dumbbell shoulder press — 3 sets x 12",
                    "Dumbbell lateral raise — 3 sets x 12",
                    "Resistance band row — 3 sets x 15",
                    "Tricep dips (chair) — 3 sets x 10",
                    "Bicep curl — 3 sets x 12",
                ]
            }
        ],
        "cardio": "20 min brisk walk or YouTube Pilates video.",
    },
    1: {"day_name": "Tuesday — Active Rest 🧘", "focus": "Yoga or Pilates. Flexibility and core.", "blocks": [{"name": "Session", "exercises": ["30 min yoga (YouTube: Adriene Mishler free)", "OR 30 min Pilates", "OR gentle walk"]}]},
    2: {
        "day_name": "Wednesday — Tone: Lower Body 🦵",
        "focus": "Glutes, legs, core. The most effective toning work for women.",
        "blocks": [
            {
                "name": "Session",
                "exercises": [
                    "Bodyweight squats — 4 sets x 15",
                    "Resistance band glute bridge — 3 sets x 15",
                    "Reverse lunges — 3 sets x 12 each leg",
                    "Calf raises — 3 sets x 20",
                    "Side-lying leg raises — 3 sets x 15 each",
                ]
            }
        ],
        "cardio": "20 min brisk walk.",
    },
    3: {"day_name": "Thursday — Walk 🚶", "focus": "Light movement day.", "blocks": [{"name": "Session", "exercises": ["30–40 min brisk walk", "5 min stretch after"]}]},
    4: {
        "day_name": "Friday — Full Body Tone 🌟",
        "focus": "End the week with a full body session.",
        "blocks": [
            {
                "name": "Session",
                "exercises": [
                    "Squats — 3 x 15",
                    "Push-ups (on knees if needed) — 3 x 10",
                    "Resistance band row — 3 x 15",
                    "Glute bridge — 3 x 15",
                    "Plank — 3 x 30 sec",
                ]
            }
        ],
    },
    5: {"day_name": "Saturday — Walk or Swim 🏊", "focus": "Low impact, good for joints and mind.", "blocks": [{"name": "Activity", "exercises": ["30 min swim OR 40 min walk", "Family walk with the family"]}]},
    6: {"day_name": "Sunday — Rest 🌿", "focus": "Full rest. Family day.", "blocks": [{"name": "Rest", "exercises": ["No training required"]}]},
}


def get_todays_gym_plan(profile: dict) -> dict:
    name = profile.get("name", "")
    dow = date.today().weekday()  # 0=Mon ... 6=Sun

    if name == "Aquib":
        plan = AQUIB_PLAN
    elif name == "Yousaf":
        plan = YOUSAF_PLAN
    else:
        plan = MARIAM_PLAN

    return plan.get(dow, {
        "day_name": "Rest Day 🌿",
        "focus": "Full rest today.",
        "blocks": [{"name": "Rest", "exercises": ["No training required"]}]
    })
