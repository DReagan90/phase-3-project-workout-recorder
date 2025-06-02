from db import insert_workout
from datetime import datetime

def add_workout():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')

    workout_type = input("Workout type: ")
    duration = int(input("Duration (minutes): "))
    notes = input("Notes (optional): ")

    insert_workout(date, workout_type, duration, notes)
    print("✅ Workout added!")
