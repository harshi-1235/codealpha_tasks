import sqlite3

conn = sqlite3.connect("database/busbooking.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("Users in database:")
print(rows)

conn.close()