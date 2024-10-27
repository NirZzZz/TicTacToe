from Logic import create_table, screen_cleaner, whose_turn

options = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
create_table(options)

live = True
turn = 0

while live:
    screen_cleaner()
    create_table(options)
    move = input()
    if move == "s":
        live = False

    turn += 1
    options[int(move)] = whose_turn(turn)
