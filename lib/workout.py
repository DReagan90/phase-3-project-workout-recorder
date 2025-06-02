from db import insert_workout
from datetime import datetime
from db import fetch_workouts_by_date

def add_workout():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    workout_type = input("Workout type: ")
    duration = int(input("Duration (minutes): "))
    notes = input("Notes (optional): ")

    insert_workout(date, workout_type, duration, notes)
    print("✅ Workout added!")

def view_workouts_by_date():
    date = input("Enter date (YYYY-MM-DD): ")
    workouts = fetch_workouts_by_date(date)

    if not workouts:
        print(f"No workouts recorded on {date}.")
    else:
        print(f"🏋️ Workouts on {date}:")
        for i, (type_, duration, notes) in enumerate(workouts, 1):
            print(f"{i}. {type_} - {duration} minutes. Notes: {notes}")