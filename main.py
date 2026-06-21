from database import create_database
from login import LoginWindow
create_database()
if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()