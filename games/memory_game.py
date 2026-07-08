import random

def play():
    print("\n🧠 Memory Game")
    print("সংখ্যাগুলো ৫ সেকেন্ড মনে রাখুন!\n")

    numbers = [random.randint(0, 9) for _ in range(5)]
    print(" ".join(map(str, numbers)))

    input("\nমনে রাখলে Enter চাপুন...")

    print("\n" * 40)

    answer = input("এখন সংখ্যাগুলো একই ক্রমে লিখুন (স্পেস দিয়ে): ")

    if answer.strip() == " ".join(map(str, numbers)):
        print("🎉 অসাধারণ! আপনি জিতেছেন!")
    else:
        print("❌ ভুল হয়েছে!")
        print("সঠিক উত্তর:", " ".join(map(str, numbers)))




from games.memory_game import play as memory_game



8. Memory Game



elif choice == "8":
    if current_user:
        memory_game()
    else:
        print("আগে Login করুন!")





