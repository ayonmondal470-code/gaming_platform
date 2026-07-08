import json
import os

PROFILE_FILE = "profiles.json"

def show_leaderboard():
    if not os.path.exists(PROFILE_FILE):
        print("কোনো Player Data নেই!")
        return

    with open(PROFILE_FILE, "r") as f:
        profiles = json.load(f)

    players = sorted(
        profiles.items(),
        key=lambda x: (
            x[1].get("wins", 0),
            x[1].get("level", 1),
            x[1].get("xp", 0)
        ),
        reverse=True
    )

    print("\n🏆 TOP 10 PLAYERS")
    print("=" * 35)

    if not players:
        print("এখনও কোনো Player নেই!")
        return

    for i, (name, data) in enumerate(players[:10], start=1):
        print(
            f"{i:2}. {name:<15} "
            f"Wins:{data.get('wins',0):<3} "
            f"Level:{data.get('level',1):<2} "
            f"XP:{data.get('xp',0)}"
        )



from leaderboard import show_leaderboard




9. Leaderboard



