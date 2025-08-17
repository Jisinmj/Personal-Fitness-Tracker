import json
from datetime import datetime

data = {"user": {}, "workouts": [], "meals": []}

def add_user():
    data["user"]["name"] = input("Enter your name: ")
    data["user"]["age"] = int(input("Enter age: "))
    data["user"]["height"] = float(input("Enter height (cm): "))
    data["user"]["weight"] = float(input("Enter weight (kg): "))

def calculate_bmi():
    h = data["user"]["height"] / 100
    w = data["user"]["weight"]
    bmi = w / (h * h)
    print(f"Your BMI: {bmi:.2f}")

def log_workout():
    ex = input("Exercise name: ")
    sets = int(input("Sets: "))
    reps = int(input("Reps: "))
    data["workouts"].append({
        "date": str(datetime.now().date()),
        "exercise": ex,
        "sets": sets,
        "reps": reps
    })

def log_meal():
    meal = input("Meal name: ")
    calories = int(input("Calories: "))
    data["meals"].append({
        "date": str(datetime.now().date()),
        "meal": meal,
        "calories": calories
    })

def save_data():
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    add_user()
    calculate_bmi()
    log_workout()
    log_meal()
    save_data()
