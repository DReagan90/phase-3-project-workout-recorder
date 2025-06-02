from random import choice
from workout import add_workout, view_workouts_by_date, show_statistics
from db import init_db 
from workout import add_workout

def main():
    while True:
        print("\n=== Workout Tracker ===")
        print("1. Add Workout")
        print("2. View Workouts by Date")
        print("3. View Statistics")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == '4':
            print("Goodbye 👋")
            break

if __name__ == "__main__":
    main()
def add_workout():   
  if choice == '1':
    add_workout()

def view_workouts_by_date():
    if choice == '2':
        view_workouts_by_date()

def show_statistics():
    if choice == '3':
        show_statistics()