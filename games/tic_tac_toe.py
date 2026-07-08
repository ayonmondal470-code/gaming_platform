def play():
    board = [" "] * 9

    def show():
        print()
        print(f" {board[0]} | {board[1]} | {board[2]}")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]}")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]}")
        print()

    def winner(p):
        wins = [
            (0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)
        ]
        return any(board[a] == board[b] == board[c] == p for a,b,c in wins)

    player = "X"

    for _ in range(9):
        show()

        try:
            move = int(input(f"Player {player}, 1-9: ")) - 1
        except ValueError:
            print("সংখ্যা লিখুন!")
            continue

        if move < 0 or move > 8 or board[move] != " ":
            print("ভুল চাল!")
            continue

        board[move] = player

        if winner(player):
            show()
            print(f"🎉 Player {player} জিতেছে!")
            return

        player = "O" if player == "X" else "X"

    show()
    print("🤝 ম্যাচ ড্র!")
