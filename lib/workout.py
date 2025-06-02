from db import insert_workout
from datetime import date, datetime
from db import fetch_workouts_by_date
from db import fetch_statistics

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



def show_statistics():
    total, minutes, top_day = fetch_statistics()

    print("\n📊 Workout Stats:")
    print(f"- Total workouts: {total or 0}")
    print(f"- Total minutes: {minutes or 0}")
    if top_day:
        print(f"- Most active day: {top_day[0]} ({top_day[1]} workouts)")


while True:
    try:
        duration = int(input("Duration (minutes): "))
        break
    except ValueError:
        print("⛔ Please enter a valid number.")

print("\n🏋️ Workouts on", date)
print("-" * 30)
for i, (type_, duration, notes) in enumerate(workouts, 1): # type: ignore
    print(f"{i}. {type_:10} | {duration:3} min | {notes}")


if total == 0: # type: ignore
    print("No workouts recorded yet.")
else:
    print("\n📊 Workout Stats:")