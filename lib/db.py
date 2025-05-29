import sqlite3
DB_NAME = "workout.db"

def get_connection():
    return sqlite3.connect(DB_NAME)