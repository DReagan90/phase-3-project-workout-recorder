from workout import add_workout, view_workouts_by_date, show_statistics
from db import init_db 

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
