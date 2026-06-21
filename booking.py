import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Bus Booking")
root.geometry("600x500")
root.configure(bg="white")

tk.Label(root,
         text="Bus Ticket Booking",
         font=("Arial", 20, "bold"),
         bg="white",
         fg="blue").pack(pady=20)

# Passenger Name
tk.Label(root, text="Passenger Name", bg="white").pack()
name = ttk.Entry(root, width=35)
name.pack(pady=5)

# Phone Number
tk.Label(root, text="Phone Number", bg="white").pack()
phone = ttk.Entry(root, width=35)
phone.pack(pady=5)

# Source
tk.Label(root, text="Source", bg="white").pack()
source = ttk.Combobox(root, width=32)
source["values"] = (
    "Hyderabad",
    "Chennai",
    "Bangalore",
    "Mumbai",
    "Delhi"
)
source.pack(pady=5)

# Destination
tk.Label(root, text="Destination", bg="white").pack()
destination = ttk.Combobox(root, width=32)
destination["values"] = (
    "Hyderabad",
    "Chennai",
    "Bangalore",
    "Mumbai",
    "Delhi"
)
destination.pack(pady=5)

# Journey Date
tk.Label(root, text="Journey Date (DD-MM-YYYY)", bg="white").pack()
date = ttk.Entry(root, width=35)
date.pack(pady=5)

# Seat Number
tk.Label(root, text="Seat Number", bg="white").pack()
seat = ttk.Combobox(root, width=32)
seat["values"] = (
    "A1","A2","A3","A4",
    "B1","B2","B3","B4"
)
seat.pack(pady=5)

def book_ticket():

    conn = sqlite3.connect("database/busbooking.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO bookings
    (passenger_name, phone, source, destination, journey_date, seat_no)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        name.get(),
        phone.get(),
        source.get(),
        destination.get(),
        date.get(),
        seat.get()
    ))

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Ticket Booked Successfully!")

ttk.Button(root,
           text="Book Ticket",
           command=book_ticket).pack(pady=20)

root.mainloop()