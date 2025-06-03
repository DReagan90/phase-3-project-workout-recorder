# phase-3-project-workout-recorder
# 🏋️ Workout Tracker CLI (Python + SQLite)

This is a command-line interface (CLI) application that helps you track your workouts by recording sessions in an SQLite database. You can add workouts, view them by date, and get basic statistics about your activity.

---

## 🚀 Features

- Add workout entries with type, duration, and optional notes
- View workouts for a specific date
- See statistics like total time worked out and most active day
- Stores data persistently using SQLite
- Simple, menu-driven interface

---

## 🛠️ Tech Stack

- Python 3.8+
- SQLite (via `sqlite3` module)

---

## 📦 Project Structure
workout_tracker/
├── main.py # Entry point (menu + navigation)
├── db.py # Database setup and queries
├── workout.py # Logic for adding/viewing/statistics
├── workouts.db # SQLite database (created automatically)
└── README.md # You’re here!


---

## ⚙️ Setup Instructions

### 1. Clone or download the repo

```bash
git clone https://github.com/your-username/workout-tracker.git
cd workout-tracker
python main.py

use the menu
=== Workout Tracker ===
1. Add Workout
2. View Workouts by Date
3. View Statistics
4. Exit
💡 Sample Use
Add a workout:

Type: Running

Duration: 30

Notes: Morning jog

View workouts on 2025-05-29

See your stats:  Total workouts: 4
                  Total minutes: 105
                  Most active day: 2025-05-28 (2 workouts)
🧪 Testing & Tips
Delete workouts.db if you want to reset the data

You can open the DB with DB Browser for SQLite for inspection

🔧 Future Improvements
Tag workouts (e.g., cardio, strength)

Filter by workout type

Export to CSV or JSON

Add a calendar-style view

Add unit tests


