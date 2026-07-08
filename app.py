from games.guess_number import play as guess_number

while True:
    print("\n=== Gaming Platform ===")
    print("1. Guess the Number")
    print("2. Exit")

    choice = input("একটি অপশন নির্বাচন করুন: ")

    if choice == "1":
        guess_number()
    elif choice == "2":
        print("ধন্যবাদ!")
        break
    else:
        print("ভুল অপশন! আবার চেষ্টা করুন।")
