from workout import add_workout, view_workouts_by_date, show_statistics
from db import init_db

def main():
    init_db()

    while True:
        print("\n=== Workout Tracker ===")
        print("1. Add Workout")
        print("2. View Workouts by Date")
        print("3. View Statistics")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == '1':
            add_workout()
        elif choice == '2':
            view_workouts_by_date()
        elif choice == '3':
            show_statistics()
        elif choice == '4':
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
