import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import sqlite3

root = tk.Tk()
root.title("Cloud Bus Booking System")
root.geometry("1000x550")
root.resizable(False, False)

# ---------------- Left Panel ----------------

left = tk.Frame(root, bg="#004d99", width=450)
left.pack(side="left", fill="y")

tk.Label(
    left,
    text="🚌\n\nCLOUD BUS\nBOOKING SYSTEM",
    font=("Arial", 24, "bold"),
    bg="#004d99",
    fg="white"
).pack(expand=True)

# ---------------- Right Panel ----------------

right = tk.Frame(root, bg="white")
right.pack(side="right", fill="both", expand=True)

tk.Label(
    right,
    text="Login",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="#004d99"
).pack(pady=30)

tk.Label(right, text="Username", bg="white").pack()

username = ttk.Entry(right, width=30)
username.pack(pady=10)

tk.Label(right, text="Password", bg="white").pack()

password = ttk.Entry(right, width=30, show="*")
password.pack(pady=10)

def login():
    user = username.get().strip()
    pwd = password.get().strip()

    conn = sqlite3.connect("database/busbooking.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (user, pwd)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Success", "Login Successful!")
        root.destroy()

        import dashboard

    else:
        messagebox.showerror("Error", "Invalid Username or Password")


ttk.Button(right, text="Login", command=login).pack(pady=20)

time_label = tk.Label(right, bg="white", fg="green")

time_label.pack()

def update_time():
    now = datetime.now().strftime("%d-%m-%Y\n%I:%M:%S %p")
    time_label.config(text=now)
    root.after(1000, update_time)

update_time()

root.mainloop()