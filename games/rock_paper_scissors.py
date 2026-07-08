import random

def play():
    choices = ["rock", "paper", "scissors"]

    while True:
        user = input("\nrock, paper, scissors লিখুন (exit লিখলে বের হবে): ").lower()

        if user == "exit":
            break

        if user not in choices:
            print("ভুল ইনপুট!")
            continue

        computer = random.choice(choices)

        print("আপনি:", user)
        print("কম্পিউটার:", computer)

        if user == computer:
            print("🤝 ড্র!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("🎉 আপনি জিতেছেন!")
        else:
            print("😢 কম্পিউটার জিতেছে!")
