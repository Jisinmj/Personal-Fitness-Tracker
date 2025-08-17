import json
from datetime import date
import os

def bmi(weight, height):
    h_m = height / 100
    return weight / (h_m * h_m)

WORKOUT_FILE = "workouts.json"

def log_workout(kind, duration, calories):
    workout = {
        "date": str(date.today()),
        "type": kind,
        "duration": duration,
        "calories": calories
    }
    if os.path.exists(WORKOUT_FILE):
        with open(WORKOUT_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(workout)

    with open(WORKOUT_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print("Workout saved!")

def view_workouts():
    if not os.path.exists(WORKOUT_FILE):
        print("No workouts logged yet.")
        return
    with open(WORKOUT_FILE, "r") as f:
        data = json.load(f)
    for w in data:
        print(f"{w['date']} - {w['type']} ({w['duration']} min, {w['calories']} kcal)")

if __name__ == "__main__":
    print("1. Calculate BMI")
    print("2. Log workout")
    print("3. View workouts")
    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter your name: ")
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))
        print(f"Hello {name}!")
        print(f"Your BMI is {bmi(weight, height):.1f}")

    elif choice == "2":
        kind = input("Workout type (e.g., run, gym): ")
        duration = int(input("Duration (minutes): "))
        calories = int(input("Calories burned: "))
        log_workout(kind, duration, calories)

    elif choice == "3":
        view_workouts()
