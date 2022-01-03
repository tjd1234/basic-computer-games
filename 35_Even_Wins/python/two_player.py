# two_player.py

#
# General structure of a 2-player turn-taking game.
#

def get_str_once(prompt):
    ans = input(prompt).strip().lower()
    return ans

def get_str_repeat(ask_once, error_prompt, good_input):
    result = ask_once()
    while not good_input(result):
        print(error_prompt)
        result = ask_once()
    return result

def ask_once_first_player():
    ans = get_str_once('Do you want to play first? (y/n) --> ')
    if ans == 'y':
        return 'human'
    elif ans == 'n':
        return 'computer'
    else:
        return 'error'

def get_first_player():
    result = get_str_repeat(
                ask_once_first_player,
                'Please type "y" if you want to go first, "n" if you want to go second',
                lambda s: s != 'error'
             )
    return result

# def ask_once_first_player():
#     prompt = 'Do you want to play first? (y/n) --> '
#     ans = input(prompt).strip()
#     if ans == 'y':
#         return 'human'
#     elif ans == 'n':
#         return 'computer'
#     else:
#         return 'error'

# def get_first_player():
#     result = ask_once_first_player()
#     while result == 'error':
#         print('Please enter "y" if you want to go first')
#         print('Or "n" if you want the computer to go first')
#         print()
#         result = ask_once_first_player()
#     return result

def game_over():
    print('Game over!') 
    result = get_str_once('Do you want to play again? (y/n) --> ')
    if result != 'y':
        print('Okay, bye bye!')
        exit()
    print("Okay, let's do it again! ...")

def opposite(p):
    if p == 'computer':
        return 'human'
    elif p == 'human':
        return 'computer'
    else:
        raise f"error: opposite got unknown player p='{p}'"

def play_game(first_player):
    player = first_player
    for i in range(10):
        print(f'{player}s turn ...')
        player = opposite(player)
    game_over()

def main():
    first_player = get_first_player()
    print(f'first player: "{first_player}"')
    play_game(first_player)

if __name__ == "__main__":
    main()
    print('done!')