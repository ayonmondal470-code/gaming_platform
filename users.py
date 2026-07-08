import json
import os

FILE = "users.json"

def load_users():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f, indent=4)

def register():
    users = load_users()

    username = input("নতুন Username: ")

    if username in users:
        print("❌ Username আগে থেকেই আছে!")
        return None

    password = input("Password: ")

    users[username] = {
        "password": password
    }

    save_users(users)

    print("✅ Registration সফল!")
    return username

def login():
    users = load_users()

    username = input("Username: ")
    password = input("Password: ")

    if username in users and users[username]["password"] == password:
        print(f"✅ Welcome {username}")
        return username

    print("❌ ভুল Username অথবা Password")
    return None
