import json
import os

SAVE_FILE = "savegame.json"

def save_game(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=4)
    print("✅ Game Saved!")

def load_game():
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r") as f:
        return json.load(f)




from save_manager import save_game, load_game



11. Save Game
12. Load Game
13. Exit




elif choice == "11":
    if current_user:
        save_game({
            "user": current_user
        })
    else:
        print("আগে Login করুন!")

elif choice == "12":
    data = load_game()
    if data:
        current_user = data["user"]
        print(f"✅ Welcome back {current_user}")
    else:
        print("❌ কোনো Save File পাওয়া যায়নি!")

elif choice == "13":
    print("ধন্যবাদ!")
    break
