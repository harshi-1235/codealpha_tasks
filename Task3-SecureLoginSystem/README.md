🔐 Secure Data Storage System
📌 Description:
The Secure Data Storage System is a Python-based desktop application developed to securely store and manage sensitive user information. The application implements modern security techniques, including password hashing with bcrypt, AES-256 encryption/decryption, and SQLite database integration, ensuring that confidential data remains protected from unauthorized access.
The project provides a simple and intuitive graphical user interface (GUI) built with Tkinter, allowing users to register, log in, securely save encrypted data, and retrieve it when needed. It demonstrates secure authentication, encrypted data storage, and best practices for handling sensitive information in desktop applications.
✨ Features:
🔐 Secure User Registration
👤 User Authentication (Login System)
🔒 Password Hashing using bcrypt
🛡️ AES-256 Encryption & Decryption
💾 Secure Data Storage with SQLite
🚫 SQL Injection Prevention using Parameterized Queries
🖥️ User-Friendly Tkinter GUI
📂 Store and Retrieve Encrypted Information
⚡ Fast and Lightweight Desktop Application
🛠️ Technologies Used:
Python 3.x
Tkinter
SQLite3
bcrypt
Cryptography (AES-256)
OS Module
Base64 Encoding
📁 Project Structure:
SecureLoginSystem/
│
├── main.py
├── login.py
├── register.py
├── dashboard.py
├── encryption.py
├── database.py
├── requirements.txt
├── database/
│   └── securelogin.db

▶️ How to Run:

1. Clone the Repository
Bash
git clone https://github.com/yourusername/SecureLoginSystem.git

2. Open the Project
Open the project folder using Visual Studio Code or your preferred Python IDE.

3. Install Required Packages
Bash
pip install -r requirements.txt
or install manually:
Bash
pip install bcrypt cryptography

4. Run the Application
Bash
python main.py
🔐 Security Features:
Passwords are securely hashed using bcrypt before storage.
Sensitive information is encrypted using AES-256 encryption.
SQLite database stores only encrypted data.
SQL Injection attacks are prevented through parameterized database queries.
User authentication ensures only authorized access to stored information.
🚀 Future Improvements:
Password Reset Functionality
Two-Factor Authentication (2FA)
Secure Cloud Backup
File Encryption Support
Multi-User Role Management
Activity Logs and Audit Trail

-----

👨‍💻 Author:
Harshitha Gedi
Python Programming Intern
CodeAlpha Internship
