import json
import os

FILE = "profiles.json"

def load_profiles():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_profiles(profiles):
    with open(FILE, "w") as f:
        json.dump(profiles, f, indent=4)

def create_profile(username):
    profiles = load_profiles()

    if username not in profiles:
        profiles[username] = {
            "games_played": 0,
            "wins": 0,
            "coins": 100,
            "level": 1,
            "xp": 0
        }

    save_profiles(profiles)

def show_profile(username):
    profiles = load_profiles()

    if username not in profiles:
        print("Profile পাওয়া যায়নি!")
        return

    p = profiles[username]

    print("\n===== PLAYER PROFILE =====")
    print("Username :", username)
    print("Level    :", p["level"])
    print("XP       :", p["xp"])
    print("Coins    :", p["coins"])
    print("Wins     :", p["wins"])
    print("Played   :", p["games_played"])






   from profile import create_profile, show_profile



current_user = login()

if current_user:
    create_profile(current_user)




7. Player Profile
8. Exit



elif choice == "7":
    if current_user:
        show_profile(current_user)
    else:
        print("আগে Login করুন!")




def add_reward(username, win=False):
    profiles = load_profiles()

    if username not in profiles:
        return

    p = profiles[username]

    p["games_played"] += 1
    p["xp"] += 20

    if win:
        p["wins"] += 1
        p["coins"] += 50
        p["xp"] += 30

    while p["xp"] >= 100:
        p["xp"] -= 100
        p["level"] += 1
        print(f"🎉 Level Up! এখন Level {p['level']}")

    save_profiles(profiles)




from profile import add_reward


add_reward(current_user, True)



add_reward(current_user, False)



tictactoe(current_user)



if not current_user:
    print("আগে Login করুন!")
    continue

