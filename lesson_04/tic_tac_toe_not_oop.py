# TODO
# Change code to check win condition after each turn
# Improve win conditions with step slicing
# Refactor code to OOP - create another project for this!


import random
board_spaces = ['*', '*', '*', '*', '*', '*', '*', '*', '*']


def print_board():
    print('The board looks like this now:')
    print(board_spaces[0] + board_spaces[1] + board_spaces[2])
    print(board_spaces[3] + board_spaces[4] + board_spaces[5])
    print(board_spaces[6] + board_spaces[7] + board_spaces[8])


def start_game():
    while True:
        command = input('Where would you like to place your piece? (1-9)\n') + ''
        command = command.lower()
        check_command(command)


def wrong_input():
    print("I'm sorry, I don't recognize that command - please try again!\n")


def check_command(user_input):
    if user_input is None or len(user_input) < 1:
        print("I'm sorry, I didn't receive any input - please try again!\n")
    try:
        int(user_input)
    except ValueError:
        print("I'm sorry, I don't recognize that input - please try again!\n")
        start_game()
    position = int(user_input)
    if 0 < position < 10:
        place_piece(position)
        # check if there is a piece there already
    else:
        wrong_input()
        start_game()


def opponent_turn():
    random_number = int(random.randint(0, 8))
    if '*' not in board_spaces:
        check_win()
    if board_spaces[random_number] == '*':
        board_spaces[random_number] = 'O'
    else:
        opponent_turn()


def place_piece(position):
    if board_spaces[position-1] == '*':
        print("You place your piece on position " + str(position))
        board_spaces[position-1] = 'X'
        opponent_turn()
        print_board()
        start_game()
    else:
        print("A piece has already been placed there - try again!")
        print_board()
        start_game()


def check_win():
    if board_spaces[0] == 'X' and board_spaces[1] == 'X' and board_spaces[2] == 'X' or board_spaces[3] == 'X' and board_spaces[4] == 'X' and board_spaces[5] == 'X' or board_spaces[6] == 'X' and board_spaces[7] == 'X' and board_spaces[8] == 'X' or board_spaces[0] == 'X' and board_spaces[3] == 'X' and board_spaces[6] == 'X' or board_spaces[1] == 'X' and board_spaces[4] == 'X' and board_spaces[7] == 'X' or board_spaces[2] == 'X' and board_spaces[5] == 'X' and board_spaces[8] == 'X' or board_spaces[0] == 'X' and board_spaces[4] == 'X' and board_spaces[8] == 'X' or board_spaces[2] == 'X' and board_spaces[4] == 'X' and board_spaces[6] == 'X':
        print("You win, goodbye!")
        quit()
    elif board_spaces[0] == 'O' and board_spaces[1] == 'O' and board_spaces[2] == 'O' or board_spaces[3] == 'O' and board_spaces[4] == 'O' and board_spaces[5] == 'O' or board_spaces[6] == 'O' and board_spaces[7] == 'O' and board_spaces[8] == 'O' or board_spaces[0] == 'O' and board_spaces[3] == 'O' and board_spaces[6] == 'O' or board_spaces[1] == 'O' and board_spaces[4] == 'O' and board_spaces[7] == 'O' or board_spaces[2] == 'O' and board_spaces[5] == 'O' and board_spaces[8] == 'O' or board_spaces[0] == 'O' and board_spaces[4] == 'O' and board_spaces[8] == 'O' or board_spaces[2] == 'O' and board_spaces[4] == 'O' and board_spaces[6] == 'O':
        print("You lose, goodbye!")
        quit()
    else:
        print("No one wins, goodbye!")


def main():
    start_game()


main()

print_board()
