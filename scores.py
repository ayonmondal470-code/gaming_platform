import json
import os

FILE = "scores.json"

def load_scores():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_scores(scores):
    with open(FILE, "w") as f:
        json.dump(scores, f, indent=4)

def add_win(player):
    scores = load_scores()
    scores[player] = scores.get(player, 0) + 1
    save_scores(scores)

def show_scores():
    scores = load_scores()

    print("\n🏆 High Scores")
    print("-" * 20)

    if not scores:
        print("এখনও কোনো স্কোর নেই!")
        return

    for player, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"{player}: {score}")
