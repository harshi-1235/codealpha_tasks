import tkinter as tk
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.title("Cloud Bus Booking System")
root.geometry("1000x600")
root.configure(bg="#EAF2F8")

# ---------- Functions ----------

def total_users():
    conn = sqlite3.connect("database/busbooking.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def total_bookings():
    conn = sqlite3.connect("database/busbooking.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM bookings")
    count = cursor.fetchone()[0]
    conn.close()
    return count

def book_ticket():
    import booking

def view_bookings():
    import view_bookings

def logout():
    root.destroy()
    import login

# ---------- Header ----------

header = tk.Label(
    root,
    text="🚌 CLOUD BUS BOOKING SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#004080",
    fg="white",
    pady=15
)
header.pack(fill="x")

# ---------- Statistics ----------

stats = tk.Frame(root, bg="#EAF2F8")
stats.pack(pady=30)

user_card = tk.Frame(stats, bg="white", relief="raised", bd=2)
user_card.grid(row=0, column=0, padx=20)

tk.Label(
    user_card,
    text="👤 Total Users",
    font=("Arial", 16, "bold"),
    bg="white"
).pack(padx=40, pady=10)

tk.Label(
    user_card,
    text=str(total_users()),
    font=("Arial", 22),
    fg="blue",
    bg="white"
).pack(pady=10)

booking_card = tk.Frame(stats, bg="white", relief="raised", bd=2)
booking_card.grid(row=0, column=1, padx=20)

tk.Label(
    booking_card,
    text="🎫 Total Bookings",
    font=("Arial", 16, "bold"),
    bg="white"
).pack(padx=40, pady=10)

tk.Label(
    booking_card,
    text=str(total_bookings()),
    font=("Arial", 22),
    fg="green",
    bg="white"
).pack(pady=10)

# ---------- Buttons ----------

button_frame = tk.Frame(root, bg="#EAF2F8")
button_frame.pack(pady=40)

tk.Button(
    button_frame,
    text="🚌 Book Ticket",
    font=("Arial", 14),
    width=20,
    bg="#3498DB",
    fg="white",
    command=book_ticket
).grid(row=0, column=0, padx=20, pady=15)

tk.Button(
    button_frame,
    text="📋 View Bookings",
    font=("Arial", 14),
    width=20,
    bg="#2ECC71",
    fg="white",
    command=view_bookings
).grid(row=0, column=1, padx=20, pady=15)

tk.Button(
    button_frame,
    text="🚪 Logout",
    font=("Arial", 14),
    width=20,
    bg="#E74C3C",
    fg="white",
    command=logout
).grid(row=1, column=0, columnspan=2, pady=20)

root.mainloop()