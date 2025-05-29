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
