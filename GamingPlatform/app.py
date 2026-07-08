import os

def clear():
    os.system("clear")

def guess_game():
    from games.guess import play
    play()

def tic_tac_toe():
    from games.tictactoe import play
    play()

def main():
    while True:
        clear()
        print("=" * 40)
        print("      🎮 PYTHON GAMING PLATFORM")
        print("=" * 40)
        print("1. Guess the Number")
        print("2. Tic Tac Toe")
        print("3. Exit")
        print("=" * 40)

        choice = input("Select an option: ")

        if choice == "1":
            guess_game()
        elif choice == "2":
            tic_tac_toe()
        elif choice == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice!")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
