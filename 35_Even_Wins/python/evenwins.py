# evenwins.py

# global variables
total = 0
m = 0
m1 = 0
go_first = ''
human_move = 0

intro_text = """
EVEN WINS
CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY

     THIS IS A TWO PERSON GAME CALLED 'EVEN WINS.'
TO PLAY THE GAME, THE PLAYERS NEED 27 MARBLES OR
OTHER OBJECTS ON A TABLE.

     THE ONLY RULES ARE THAT (1) YOU MUST ALTERNATE TURNS,
(2) YOU MUST TAKE BETWEEN 1 AND 4 MARBLES EACH TURN,
AND (3) YOU CANNOT SKIP A TURN.

     THE 2 PLAYERS ALTERNATE TURNS, WITH EACH PLAYER
REMOVING FROM 1 TO 4 MARBLES ON EACH MOVE.  THE GAME
ENDS WHEN THERE ARE NO MARBLES LEFT, AND THE WINNER
IS THE ONE WITH AN EVEN NUMBER OF MARBLES.

     TYPE A '1' IF YOU WANT TO GO FIRST, AND TYPE
A '0' IF YOU WANT ME TO GO FIRST.
"""

# 1160 PRINT
# 1170 PRINT "THE NUMBER OF MARBLES YOU TAKE MUST BE A POSITIVE"
# 1180 PRINT "INTEGER BETWEEN 1 AND 4."
# 1190 PRINT
# 1200 PRINT "     WHAT IS YOUR NEXT MOVE?"
# 1210 PRINT
bad_move_text = """
THE NUMBER OF MARBLES YOU TAKE MUST BE A POSITIVE
INTEGER BETWEEN 1 AND 4.

     WHAT IS YOUR NEXT MOVE?
"""

def bad_move(): print(bad_move_text)

def print_total(): print(f'\nTOTAL={total}')


def game_over():
    # 880 PRINT "THAT IS ALL OF THE MARBLES."
    # 890 PRINT
    # 900 PRINT " MY TOTAL IS";M1;", YOUR TOTAL IS";Y1
    # 910 PRINT
    # 920 IF INT(M1/2)=M1/2 THEN 950
    # 930 PRINT "     YOU WON.  DO YOU WANT TO PLAY"
    print('THAT IS ALL OF THE MARBLES.')
    print()
    print(f' MY TOTAL IS {m1}, YOUR TOTAL IS {y1}')
    print()
    if int(m1/2) == m1/2:
        # 950 PRINT "     I WON.  DO YOU WANT TO PLAY"
        print('     I WON.  DO YOU WANT TO PLAY')
    else:
        print('     YOU WON.  DO YOU WANT TO PLAY')
    # 960 PRINT "AGAIN?  TYPE 1 FOR YES AND 0 FOR NO."
    # 970 INPUT A1
    print('AGAIN?  TYPE 1 FOR YES AND 0 FOR NO.')
    play_again = input('? ')
    if play_again == '0':
        print('OK.  SEE YOU LATER.')
        return

def main():
    print(intro_text)
    go_first = input('? ')
    if go_first == '0':
        # computer goes first
        total = 27  # start with 27 marbles
        m = 2
        # 270 PRINT:PRINT "TOTAL=";T:PRINT
        # 280 M1=M1+M
        # 290 T=T-M
        # 300 PRINT "I PICK UP";M;"MARBLES."
        print_total()
        m1 = m1 + m
        total = total - m
        if total == 0:
            game_over()
        else: #  there are 1 or more marbles left   
            # 320 PRINT:PRINT "TOTAL=";T
            # 330 PRINT
            # 340 PRINT "     AND WHAT IS YOUR NEXT MOVE, MY TOTAL IS";M1
            # 350 INPUT Y
            # 360 PRINT
            print_total()
            print()
            print(f'     AND WHAT IS YOUR NEXT MOVE, MY TOTAL IS {m1}')
            human_move = input('? ')
            # 370 IF Y<1 THEN 1160
            # 380 IF Y>4 THEN 1160
            if human_move < 1: bad_move()
            if human_move > 4: bad_move()

            # 390 IF Y<=T THEN 430


    else:
        # human goes first


if __name__ == '__main__':
    main()
