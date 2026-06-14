from ai.workout_generator import generate_plan

user = {
    "name": "Mohammed Saad",
    "age": 20,
    "height": 178,
    "weight": 60,
    "goal": "Muscle Gain",
    "diet": "Non-Vegetarian",
    "equipment": "None"
}

result = generate_plan(user)

print(result)