import tkinter as tk
from tkinter import ttk,messagebox
import sqlite3

# ------------------ FUNCTIONS ------------------

def search_booking():
    name = search_entry.get()

    conn = sqlite3.connect("database/busbooking.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, passenger_name, phone, source,
               destination, journey_date, seat_no
        FROM bookings
        WHERE passenger_name LIKE ?
    """, ('%' + name + '%',))

    rows = cursor.fetchall()

    for item in tree.get_children():
        tree.delete(item)

    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()


def load_data():
    conn = sqlite3.connect("database/busbooking.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, passenger_name, phone, source,
               destination, journey_date, seat_no
        FROM bookings
    """)

    rows = cursor.fetchall()

    for item in tree.get_children():
        tree.delete(item)

    for row in rows:
        tree.insert("", tk.END, values=row)

    conn.close()
from tkinter import messagebox

def delete_booking():
    selected = tree.focus()

    if not selected:
        messagebox.showwarning("Warning", "Please select a booking.")
        return

    values = tree.item(selected, "values")
    booking_id = values[0]

    confirm = messagebox.askyesno(
        "Confirm",
        "Are you sure you want to delete this booking?"
    )

    if confirm:
        conn = sqlite3.connect("database/busbooking.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM bookings WHERE id=?", (booking_id,))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Booking Deleted Successfully")
        load_data()

# ------------------ WINDOW ------------------

root = tk.Tk()
root.title("Cloud Bus Booking System - View Bookings")
root.geometry("1200x600")
root.configure(bg="#F5F7FA")

title = tk.Label(
    root,
    text="🚌 All Bus Bookings",
    font=("Arial", 22, "bold"),
    bg="#004080",
    fg="white",
    pady=10
)
title.pack(fill="x")

# ------------------ SEARCH ------------------

search_frame = tk.Frame(root, bg="#F5F7FA")
search_frame.pack(pady=10)

tk.Label(
    search_frame,
    text="Search Passenger:",
    font=("Arial", 12),
    bg="#F5F7FA"
).pack(side="left", padx=5)

search_entry = tk.Entry(search_frame, width=30)
search_entry.pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Search",
    command=search_booking,
    bg="#3498DB",
    fg="white"
).pack(side="left", padx=5)

tk.Button(
    search_frame,
    text="Show All",
    command=load_data,
    bg="#2ECC71",
    fg="white"
).pack(side="left", padx=5)
tk.Button(
    search_frame,
    text="Delete Booking",
    command=delete_booking,
    bg="red",
    fg="white"
).pack(side="left", padx=5)
# ------------------ TABLE ------------------

style = ttk.Style()
style.theme_use("clam")

style.configure("Treeview", rowheight=30, font=("Arial", 11))
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))

columns = (
    "ID",
    "Passenger",
    "Phone",
    "Source",
    "Destination",
    "Journey Date",
    "Seat"
)

tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.column("ID", width=60, anchor="center")
tree.column("Passenger", width=180, anchor="center")
tree.column("Phone", width=150, anchor="center")
tree.column("Source", width=150, anchor="center")
tree.column("Destination", width=150, anchor="center")
tree.column("Journey Date", width=180, anchor="center")
tree.column("Seat", width=80, anchor="center")

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)
scrollbar.pack(side="right", fill="y")

# ------------------ LOAD DATA ------------------

load_data()

root.mainloop()