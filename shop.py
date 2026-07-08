import json
import os

PROFILE_FILE = "profiles.json"

SHOP_ITEMS = {
    "1": ("Dark Theme", 100),
    "2": ("Golden Avatar", 200),
    "3": ("VIP Badge", 500),
}

def load_profiles():
    if not os.path.exists(PROFILE_FILE):
        return {}

    with open(PROFILE_FILE, "r") as f:
        return json.load(f)

def save_profiles(data):
    with open(PROFILE_FILE, "w") as f:
        json.dump(data, f, indent=4)

def shop(username):
    profiles = load_profiles()

    if username not in profiles:
        print("❌ Profile পাওয়া যায়নি!")
        return

    player = profiles[username]

    print("\n====== GAME SHOP ======")
    print(f"Coins: {player['coins']}\n")

    for key, (name, price) in SHOP_ITEMS.items():
        print(f"{key}. {name} - {price} Coins")

    print("0. Back")

    choice = input("\nকি কিনতে চান? ")

    if choice == "0":
        return

    if choice not in SHOP_ITEMS:
        print("❌ ভুল অপশন!")
        return

    item, price = SHOP_ITEMS[choice]

    if player["coins"] < price:
        print("❌ পর্যাপ্ত Coins নেই!")
        return

    player["coins"] -= price

    inventory = player.get("inventory", [])
    inventory.append(item)
    player["inventory"] = inventory

    save_profiles(profiles)

    print(f"✅ আপনি '{item}' কিনেছেন!")


from shop import shop


9. Coin Shop
10. Exit


elif choice == "9":
    if current_user:
        shop(current_user)
    else:
        print("আগে Login করুন!")

elif choice == "10":
    break


