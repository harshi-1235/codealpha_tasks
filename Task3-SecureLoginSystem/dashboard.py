import tkinter as tk

root = tk.Tk()
root.title("Secure Login Dashboard")
root.geometry("600x400")
root.configure(bg="#EAF2F8")

tk.Label(
    root,
    text="Secure Login System",
    font=("Arial", 22, "bold"),
    bg="#004080",
    fg="white"
).pack(fill="x", pady=10)

tk.Label(
    root,
    text="Login Successful!",
    font=("Arial", 18),
    bg="#EAF2F8"
).pack(pady=20)

tk.Label(
    root,
    text="Security Features",
    font=("Arial", 16, "bold"),
    bg="#EAF2F8"
).pack()

features = [
    "✔ Password Hashing (bcrypt)",
    "✔ AES-256 Data Encryption",
    "✔ SQL Injection Prevention",
    "✔ SQLite Secure Database"
]

for item in features:
    tk.Label(root, text=item, bg="#EAF2F8", font=("Arial", 12)).pack(anchor="w", padx=120)

tk.Button(
    root,
    text="Logout",
    command=root.destroy,
    bg="red",
    fg="white",
    width=15
).pack(pady=30)

root.mainloop()