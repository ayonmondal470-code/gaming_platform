import random

def play():
    print("\n=== Guess the Number ===")
    number = random.randint(1, 10)

    while True:
        try:
            guess = int(input("১ থেকে ১০-এর মধ্যে একটি সংখ্যা লিখুন: "))

            if guess == number:
                print("🎉 অভিনন্দন! আপনি সঠিক সংখ্যা ধরেছেন।")
                break
            elif guess < number:
                print("আরও বড় সংখ্যা চেষ্টা করুন।")
            else:
                print("আরও ছোট সংখ্যা চেষ্টা করুন।")
        except ValueError:
            print("শুধু সংখ্যা লিখুন।")
