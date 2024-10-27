import os


def create_table(options):
    table = (f"|{options[1]}|{options[2]}|{options[3]}|\n"
             f"|{options[4]}|{options[5]}|{options[6]}|\n"
             f"|{options[7]}|{options[8]}|{options[9]}|")
    print(table)


def whose_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"


def screen_cleaner():
    os.system("cls" if os.name == "nt" else "clear")


def check_win(options):
    if (options[1] == options[2] == options[3]) \
            or (options[4] == options[5] == options[6]) \
            or (options[7] == options[8] == options[9]):
        return True
    elif (options[1] == options[4] == options[7]) \
            or (options[2] == options[5] == options[8]) \
            or (options[3] == options[6] == options[9]):
        return True
    elif (options[1] == options[5] == options[9]) \
            or (options[3] == options[5] == options[7]):
        return True
    else:
        return False
