def play():
    questions = [
        {
            "question": "Python কে তৈরি করেছেন?",
            "options": [
                "1. Guido van Rossum",
                "2. Dennis Ritchie",
                "3. James Gosling",
                "4. Bjarne Stroustrup"
            ],
            "answer": "1"
        },
        {
            "question": "2 + 2 = ?",
            "options": [
                "1. 3",
                "2. 4",
                "3. 5",
                "4. 6"
            ],
            "answer": "2"
        },
        {
            "question": "ভারতের রাজধানী কী?",
            "options": [
                "1. কলকাতা",
                "2. মুম্বাই",
                "3. নয়াদিল্লি",
                "4. চেন্নাই"
            ],
            "answer": "3"
        }
    ]

    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        ans = input("উত্তর: ")

        if ans == q["answer"]:
            print("✅ সঠিক!")
            score += 1
        else:
            print("❌ ভুল!")

    print(f"\n🎉 আপনার স্কোর: {score}/{len(questions)}")



from games.quiz import play as quiz_game


7. Quiz Game


elif choice == "7":
    if current_user:
        quiz_game()
    else:
        print("আগে Login করুন!")

