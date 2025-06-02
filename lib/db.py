import sqlite3
DB_NAME = "workout.db"

def get_connection():
    return sqlite3.connect(DB_NAME)
def init_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workouts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                type TEXT NOT NULL,
                duration INTEGER NOT NULL,
                notes TEXT
            )
        """)
        conn.commit()
def insert_workout(date, workout_type, duration, notes):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO workouts (date, type, duration, notes)
            VALUES (?, ?, ?, ?)
        """, (date, workout_type, duration, notes))
        conn.commit()

def fetch_workouts_by_date(date):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT type, duration, notes FROM workouts WHERE date = ?", (date,))
        return cursor.fetchall()

def fetch_statistics():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*), SUM(duration) FROM workouts")
        total_workouts, total_duration = cursor.fetchone()

        cursor.execute("""
            SELECT date, COUNT(*) as count
            FROM workouts
            GROUP BY date
            ORDER BY count DESC
            LIMIT 1
        """)
        result = cursor.fetchone()
        return total_workouts, total_duration, result
