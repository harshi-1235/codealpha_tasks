import tkinter as tk
from tkinter import messagebox
import sqlite3

# ---------------- DATABASE ---------------- #

def connect_db():
    conn = sqlite3.connect("redundancy.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            phone TEXT
        )
    """)

    conn.commit()
    return conn


# ---------------- CRUD FUNCTIONS ---------------- #

def add_record():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    if name == "" or email == "" or phone == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=? OR phone=?", (email, phone))
    if cursor.fetchone():
        messagebox.showerror("Duplicate", "Record already exists!")
    else:
        cursor.execute(
            "INSERT INTO users(name,email,phone) VALUES(?,?,?)",
            (name, email, phone)
        )
        conn.commit()
        messagebox.showinfo("Success", "Record added successfully!")
        clear_fields()

    conn.close()


def view_records():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    conn.close()

    window = tk.Toplevel(root)
    window.title("All Records")
    window.geometry("600x400")

    tk.Label(window, text="ID | Name | Email | Phone",
             font=("Arial", 11, "bold")).pack(pady=10)

    for r in records:
        tk.Label(
            window,
            text=f"ID: {r[0]}   Name: {r[1]}   Email: {r[2]}   Phone: {r[3]}",
            justify="left"
        ).pack(anchor="w", padx=10)


def search_record():
    email = email_entry.get().strip()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    record = cursor.fetchone()
    conn.close()

    if record:
        messagebox.showinfo(
            "Found",
            f"ID: {record[0]}\nName: {record[1]}\nEmail: {record[2]}\nPhone: {record[3]}"
        )
    else:
        messagebox.showerror("Not Found", "Record not found!")


def update_record():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET name=?, phone=? WHERE email=?",
        (name, phone, email)
    )
    conn.commit()

    if cursor.rowcount > 0:
        messagebox.showinfo("Success", "Record updated successfully!")
        clear_fields()
    else:
        messagebox.showerror("Error", "Record not found!")

    conn.close()


def delete_record():
    email = email_entry.get().strip()

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE email=?", (email,))
    conn.commit()

    if cursor.rowcount > 0:
        messagebox.showinfo("Success", "Record deleted successfully!")
        clear_fields()
    else:
        messagebox.showerror("Error", "Record not found!")

    conn.close()


def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Data Redundancy Removal System")
root.geometry("650x600")
root.configure(bg="#ecf0f1")
root.resizable(False, False)

frame = tk.Frame(root, bg="white")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title
tk.Label(
    frame,
    text="User Management System",
    font=("Helvetica", 16, "bold"),
    bg="white",
    fg="#2c3e50"
).grid(row=0, column=0, columnspan=2, pady=15)

# Name
tk.Label(frame, text="Name", bg="white").grid(row=1, column=0, pady=8, sticky="e")
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=1, column=1, pady=8)

# Email
tk.Label(frame, text="Email", bg="white").grid(row=2, column=0, pady=8, sticky="e")
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=2, column=1, pady=8)

# Phone
tk.Label(frame, text="Phone", bg="white").grid(row=3, column=0, pady=8, sticky="e")
phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=3, column=1, pady=8)

# Buttons
tk.Button(frame, text="Add Record", command=add_record,
          bg="#2ecc71", fg="white", width=18).grid(row=4, column=0, pady=8)

tk.Button(frame, text="View Records", command=view_records,
          bg="#34495e", fg="white", width=18).grid(row=4, column=1, pady=8)

tk.Button(frame, text="Search", command=search_record,
          bg="#3498db", fg="white", width=18).grid(row=5, column=0, pady=5)

tk.Button(frame, text="Update", command=update_record,
          bg="#9b59b6", fg="white", width=18).grid(row=5, column=1, pady=5)

tk.Button(frame, text="Delete Record", command=delete_record,
          bg="#e74c3c", fg="white", width=38).grid(row=6, column=0, columnspan=2, pady=12)

root.mainloop()
