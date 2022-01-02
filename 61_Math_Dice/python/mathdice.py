from random import randint
print("Math Dice")
print("https://github.com/coding-horror/basic-computer-games")
print()
print("""This program generates images of two dice.
When two dice and an equals sign followed by a question
mark have been printed, type your answer, and hit the ENTER
key.
To conclude the program, type 0.
""")

face = [
"""
 -----
|     |
|  *  |
|     |
 -----
""",

"""
 -----
| *   |
|     |
|   * |
 -----
""",

"""
 -----
| *   |
|  *  |
|   * |
 -----
""",

"""
 -----
| * * |
|     |
| * * |
 -----
""",

"""
 -----
| * * |
|  *  |
| * * |
 -----
""",

""" 
 -----
| * * |
| * * |
| * * |
 -----
""",
]

# remove the leading \n at the start of each face
face = [d.lstrip('\n') for d in face]

def print_dice(n):
    print(face[n-1], end='')

def main():
    while True:
        d1 = randint(1, 6)
        d2 = randint(1, 6)
        total = d1 + d2
        guess = 13

        print_dice(d1)
        print('   +')
        print_dice(d2)
        print('   =')

        tries = 0
        while guess != total and tries < 2:
            if tries == 1:
                print('No, count the spots and give another answer.')
            try:
                guess = int(input())
            except ValueError:
                print("That's not a number!")
            if guess == 0:
                return
            tries += 1

        if guess != total:
            print(f'No, the answer is {total}!')
        else:
            print('Correct!')

        print('The dice roll again....')


if __name__ == '__main__':
    main()
