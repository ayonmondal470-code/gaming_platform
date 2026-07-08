import json
import os

PROFILE_FILE = "profiles.json"

def show_statistics(username):
    if not os.path.exists(PROFILE_FILE):
        print("কোনো Profile পাওয়া যায়নি!")
        return

    with open(PROFILE_FILE, "r") as f:
        profiles = json.load(f)

    if username not in profiles:
        print("Player পাওয়া যায়নি!")
        return

    p = profiles[username]

    played = p.get("games_played", 0)
    wins = p.get("wins", 0)
    losses = played - wins

    if played > 0:
        win_rate = (wins / played) * 100
    else:
        win_rate = 0

    print("\n========== PLAYER STATISTICS ==========")
    print(f"👤 Username : {username}")
    print(f"🎮 Games Played : {played}")
    print(f"🏆 Wins : {wins}")
    print(f"❌ Losses : {losses}")
    print(f"⭐ Level : {p.get('level', 1)}")
    print(f"✨ XP : {p.get('xp', 0)}")
    print(f"🪙 Coins : {p.get('coins', 0)}")
    print(f"📈 Win Rate : {win_rate:.2f}%")

import json
import os

PROFILE_FILE = "profiles.json"

def show_statistics(username):
    if not os.path.exists(PROFILE_FILE):
        print("কোনো Profile পাওয়া যায়নি!")
        return

    with open(PROFILE_FILE, "r") as f:
        profiles = json.load(f)

    if username not in profiles:
        print("Player পাওয়া যায়নি!")
        return

    p = profiles[username]

    played = p.get("games_played", 0)
    wins = p.get("wins", 0)
    losses = played - wins

    if played > 0:
        win_rate = (wins / played) * 100
    else:
        win_rate = 0

    print("\n========== PLAYER STATISTICS ==========")
    print(f"👤 Username : {username}")
    print(f"🎮 Games Played : {played}")
    print(f"🏆 Wins : {wins}")
    print(f"❌ Losses : {losses}")
    print(f"⭐ Level : {p.get('level', 1)}")
    print(f"✨ XP : {p.get('xp', 0)}")
    print(f"🪙 Coins : {p.get('coins', 0)}")
    print(f"📈 Win Rate : {win_rate:.2f}%")


import json
import os

PROFILE_FILE = "profiles.json"

def show_statistics(username):
    if not os.path.exists(PROFILE_FILE):
        print("কোনো Profile পাওয়া যায়নি!")
        return

    with open(PROFILE_FILE, "r") as f:
        profiles = json.load(f)

    if username not in profiles:
        print("Player পাওয়া যায়নি!")
        return

    p = profiles[username]

    played = p.get("games_played", 0)
    wins = p.get("wins", 0)
    losses = played - wins

    if played > 0:
        win_rate = (wins / played) * 100
    else:
        win_rate = 0

    print("\n========== PLAYER STATISTICS ==========")
    print(f"👤 Username : {username}")
    print(f"🎮 Games Played : {played}")
    print(f"🏆 Wins : {wins}")
    print(f"❌ Losses : {losses}")
    print(f"⭐ Level : {p.get('level', 1)}")
    print(f"✨ XP : {p.get('xp', 0)}")
    print(f"🪙 Coins : {p.get('coins', 0)}")
    print(f"📈 Win Rate : {win_rate:.2f}%")

from statistics import show_statistics

13. Player Statistics
14. Exit



elif choice == "13":
    if current_user:
        show_statistics(current_user)
    else:
        print("আগে Login করুন!")

elif choice == "14":
    print("ধন্যবাদ!")
    break
