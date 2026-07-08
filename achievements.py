import json
import os

FILE = "achievements.json"

def load():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def unlock(username, achievement):
    data = load()

    if username not in data:
        data[username] = []

    if achievement not in data[username]:
        data[username].append(achievement)
        print(f"\n🏆 Achievement Unlocked: {achievement}")

    save(data)

def show(username):
    data = load()

    print("\n====== ACHIEVEMENTS ======")

    if username not in data or not data[username]:
        print("কোনো Achievement নেই।")
        return

    for a in data[username]:
        print("⭐", a)



from achievements import unlock


if p["wins"] == 1:
    unlock(username, "First Victory")

if p["wins"] == 5:
    unlock(username, "Winner x5")

if p["level"] == 5:
    unlock(username, "Level 5 Reached")

if p["coins"] >= 500:
    unlock(username, "Rich Player")

from achievements import show


8. Achievements
9. Exit

elif choice == "8":
    if current_user:
        show(current_user)
    else:
        print("আগে Login করুন!")

elif choice == "9":
    break

