import tkinter as tk
from tkinter import messagebox
import sqlite3
from encryption import verify_password, decrypt_data


def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please enter username and password.")
        return

    conn = sqlite3.connect("database/securelogin.db")
    cursor = conn.cursor()

    # Parameterized query prevents SQL Injection
    cursor.execute(
        "SELECT password ,secret FROM users WHERE username=?",
        (username,)
    )

    record = cursor.fetchone()
    conn.close()

    if record and verify_password(password, record[0]):
        secret=decrypt_data(record[1])
        messagebox.showinfo("Success", f"Login Successful!\n\n Your Secret Information:\n{secret}")
        root.destroy()

        import dashboard

    else:
        messagebox.showerror("Error", "Invalid Username or Password")


root = tk.Tk()
root.title("Secure Login System")
root.geometry("400x300")
root.configure(bg="#EAF2F8")

tk.Label(
    root,
    text="Secure Login",
    font=("Arial", 18, "bold"),
    bg="#EAF2F8"
).pack(pady=20)

tk.Label(root, text="Username", bg="#EAF2F8").pack()

username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

tk.Label(root, text="Password", bg="#EAF2F8").pack()

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

tk.Button(
    root,
    text="Login",
    command=login,
    bg="#007ACC",
    fg="white",
    width=20
).pack(pady=20)

root.mainloop()