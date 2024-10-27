from Logic import create_table, screen_cleaner, whose_turn, check_win

options = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
create_table(options)

live = True
turn = 0
prev_turn = -1

while live:
    screen_cleaner()
    create_table(options)
    print("Player " + str((turn % 2) + 1) + "'s turn: Do your move or type 'q' to quit the game")
    if prev_turn == turn:
        print("Invalid input, please pick another move")
    prev_turn = turn
    move = input()
    if move == "q":
        live = False
        print("Player " + str((turn % 2) + 1) + " chose to quit the game")
    elif str.isdigit(move) and int(move) in options:
        if not options[int(move)] in {"X", "O"}:
            turn += 1
            options[int(move)] = whose_turn(turn)
    win = check_win(options)
    if win:
        create_table(options)
        print("Player " + str(turn % 2) + " won the game!")
        live = False
    elif turn > 8:
        live = False
        create_table(options)
        print("Its a Tie!!")
    else:
        live = True
