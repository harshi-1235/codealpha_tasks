import tkinter as tk
from tkinter import messagebox
import sqlite3
from encryption import hash_password,encrypt_data

root = tk.Tk()
root.title("Secure Login System - Register")
root.geometry("400x350")
root.configure(bg="#EAF2F8")


def register():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    secret = secret_entry.get().strip()

    if username == "" or password == "" or secret == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    hashed_password = hash_password(password)
    encrypted_secret = encrypt_data(secret)

    conn = sqlite3.connect("database/securelogin.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users(username, password, secret) VALUES(?, ?, ?)",
            (username, hashed_password, encrypted_secret)
        )

        conn.commit()
        messagebox.showinfo("Success", "Registration Successful!")

        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        secret_entry.delete(0, tk.END)

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")

    conn.close()

tk.Label(root, text="Secret Information", bg="#EAF2F8").pack()
secret_entry = tk.Entry(root,width=30)
secret_entry.pack(pady=5)
tk.Label(root, text="Register", font=("Arial", 18, "bold"),
         bg="#EAF2F8").pack(pady=15)

tk.Label(root, text="Username", bg="#EAF2F8").pack()
username_entry = tk.Entry(root, width=30)
username_entry.pack(pady=5)

tk.Label(root, text="Password", bg="#EAF2F8").pack()
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)


tk.Button(root,
          text="Register",
          command=register,
          bg="#2E86C1",
          fg="white",
          width=20).pack(pady=20)

root.mainloop()