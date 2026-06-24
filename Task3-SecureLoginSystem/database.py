import sqlite3
import os

# Create database folder if it doesn't exist
if not os.path.exists("database"):
    os.makedirs("database")

# Connect to the database
conn = sqlite3.connect("database/securelogin.db")

cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    secret TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database and users table created successfully.")