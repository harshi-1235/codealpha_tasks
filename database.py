import sqlite3
import os

print("Current Folder:", os.getcwd())

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/busbooking.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    passenger_name TEXT,
    phone TEXT,
    source TEXT,
    destination TEXT,
    journey_date TEXT,
    seat_no TEXT
)
""")
conn.commit()
conn.close()

print("Database Created Successfully!")