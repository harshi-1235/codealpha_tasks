import tkinter as tk
from tkinter import messagebox
import sqlite3

root = tk.Tk()
root.title("Register")
root.geometry("400x300")

tk.Label(root, text="Username").pack(pady=5)
username = tk.Entry(root)
username.pack()

tk.Label(root, text="Password").pack(pady=5)
password = tk.Entry(root, show="*")
password.pack()


def register():
    user = username.get().strip()
    pwd = password.get().strip()

    if user == "" or pwd == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    conn = sqlite3.connect("database/busbooking.db")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users WHERE username=?", (user,))
        existing = cursor.fetchone()

        if existing:
            messagebox.showerror("Error", "Username already exists")
        else:
            cursor.execute(
                "INSERT INTO users(username, password) VALUES(?, ?)",
                (user, pwd)
            )
            conn.commit()
            messagebox.showinfo("Success", "Registration Successful")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))

    finally:
        conn.close()


tk.Button(root, text="Register", command=register).pack(pady=20)

root.mainloop()