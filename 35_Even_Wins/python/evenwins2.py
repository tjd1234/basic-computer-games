# evenwins2.py 

#
# Version of evenwins.bas based on game decscription and *not*
# a re-do of the source code.
#
# For simplicity, global variables are used to store the game state.
# A good exercise would be to replace this with a class.
#

import random

# global variables
marbles_in_middle = -1
human_marbles     = -1
computer_marbles  = -1
whose_turn        = ''

# Only called during development for serious errors that are due to mistakes
# in the program. Should never be called during a regular game.
def serious_error(msg):
    print('serious_error: ' + msg)
    exit(1)

def welcome_screen():
    print('Welcome to Even Wins!')
    print()

def marbles_str(n):
    if n == 1: return '1 marble'
    return f'{n} marbles'

def choose_first_player():
    global whose_turn
    while True:
        ans = input('Do you want to play first? (y/n) --> ')
        if ans == 'y': 
            whose_turn = 'human'
            return
        elif ans == 'n':
            whose_turn = 'computer'
            return
        else:
            print()
            print('Please enter "y" if you want to play first,')
            print('or "n" if you want to play second.')

def next_player():
    global whose_turn
    if whose_turn == 'human':
        whose_turn = 'computer'
    elif whose_turn == 'computer':
        whose_turn = 'human'
    else:
        serious_error(f'play_game: unknown player {whose_turn}')

# Converts a string s to an int, if possible.
def to_int(s):
    try:
        n = int(s)
        return True, n
    except:
        return False, 0

def print_board():
    global marbles_in_middle
    global human_marbles
    global computer_marbles
    print()
    print(f' marbles in the middle: {marbles_in_middle} ' + marbles_in_middle*'*')
    print(f'    # marbles you have: {human_marbles}')
    print(f'# marbles computer has: {computer_marbles}')
    print()

def human_turn():
    global marbles_in_middle
    global human_marbles

    # get number in range 1 to min(4, marbles_in_middle)
    max_choice = min(4, marbles_in_middle)
    print("It's your turn!")
    while True:
        s = input(f'Marbles to take? (1 - {max_choice}) --> ')
        ok, n = to_int(s)
        if not ok:
            print()
            print(f'  Please enter a whole number from 1 to {max_choice}')
            print()
            continue
        if n < 1:
            print()
            print('  You must take at least 1 marble!')
            print()
            continue
        if n > max_choice:
            print()
            print(f'  You can take at most {marbles_str(max_choice)}')
            print()
            continue
        print()
        print(f'Okay, taking {marbles_str(n)} ...')
        marbles_in_middle -= n
        human_marbles += n
        return

def game_over():
    global marbles_in_middle
    global human_marbles
    global computer_marbles
    print()
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!! All the marbles are taken: Game Over!')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print()
    print_board()
    if human_marbles % 2 == 0:
        print('You are the winner! Congratulations!')
    else:
        print('The computer wins: all hail mighty silicon!')
    print('')

def computer_turn():
    global marbles_in_middle
    global computer_marbles

    print("It's the computer's turn ...")
    max_choice = min(4, marbles_in_middle)

    # choose at random
    n = random.randint(1, max_choice)
    print(f'Computer takes {marbles_str(n)} ...')
    marbles_in_middle -= n
    computer_marbles += n

def play_game():
    global marbles_in_middle
    global human_marbles
    global computer_marbles

    # initialize the game state
    marbles_in_middle = 27
    human_marbles = 0
    computer_marbles = 0
    print_board()

    while True:
        if marbles_in_middle == 0:
            game_over()
            return
        elif whose_turn == 'human':
            human_turn()
            print_board()
            next_player()
        elif whose_turn == 'computer':
            computer_turn()
            print_board()
            next_player()
        else:
            serious_error(f'play_game: unknown player {whose_turn}')

def main():
    global whose_turn
    # welcome screen
    welcome_screen()

    while True:
        choose_first_player()
        play_game()

        # ask if the user if they want to play again
        print()
        again = input('Would you like to play again? (y/n) --> ')
        if again == 'y':
            print()
            print("Ok, let's play again ...")
            print()
        else:
            print('Ok, thanks for playing ... goodbye!')
            return

if __name__ == '__main__':
    main()
