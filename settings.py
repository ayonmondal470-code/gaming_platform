import json
import os

FILE = "settings.json"

DEFAULT = {
    "theme": "Dark",
    "language": "Bangla",
    "sound": True,
    "autosave": True
}

def load_settings():
    if not os.path.exists(FILE):
        with open(FILE, "w") as f:
            json.dump(DEFAULT, f, indent=4)
        return DEFAULT

    with open(FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    with open(FILE, "w") as f:
        json.dump(settings, f, indent=4)

def menu():
    settings = load_settings()

    while True:
        print("\n===== SETTINGS =====")
        print("1. Theme")
        print("2. Language")
        print("3. Sound")
        print("4. Auto Save")
        print("5. Back")

        choice = input("Choose: ")

        if choice == "1":
            settings["theme"] = "Light" if settings["theme"] == "Dark" else "Dark"

        elif choice == "2":
            settings["language"] = "English" if settings["language"] == "Bangla" else "Bangla"

        elif choice == "3":
            settings["sound"] = not settings["sound"]

        elif choice == "4":
            settings["autosave"] = not settings["autosave"]

        elif choice == "5":
            break

        save_settings(settings)

        print("✅ Settings Saved!")


from settings import menu as settings_menu


10. Settings
11. Exit


elif choice == "10":
    settings_menu()

elif choice == "11":
    break
