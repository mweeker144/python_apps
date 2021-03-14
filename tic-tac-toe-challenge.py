from random import randrange

#  Random player assignment function so the same player does not always go first each time.
def player_assignment(name1, name2):
    rando = randrange(10)
    print(rando)
    if rando <=4:
        name1 = "player_1"
        name2 = "player_2"
    else:
        name2 = "player_1"
        name1 = "player_2"
    print(f'{printable_n1} is {name1}')
    print(f'{printable_n2} is {name2}\n')

# Setting player 1 and 2 to either X or O.
player_1 = 'X'
player_2 = 'O'

# Validation function to check different scenarios for winners.
def check_for_winners(theBoard):
    # Horizontals
    if theBoard['7'] != ' ' and theBoard['7'] == theBoard['8'] and theBoard['8'] == theBoard['9']:
        return f"Great job, {theBoard['7']}. You won!\n"

    elif theBoard['4'] != ' ' and theBoard['4'] == theBoard['5'] and theBoard['5'] == theBoard['6']:
        return f"Great job, {theBoard['4']}. You won!\n"

    elif theBoard['1'] != ' ' and theBoard['1'] == theBoard['2'] and theBoard['2'] == theBoard['3']:
        return f"Great job, {theBoard['1']}. You won!\n"
    # Verticals
    elif theBoard['7'] != ' ' and theBoard['7'] == theBoard['4'] and theBoard['4'] == theBoard['1']:
        return f"Great job, {theBoard['7']}. You won!\n"

    elif theBoard['8'] != ' ' and theBoard['8'] == theBoard['5'] and theBoard['5'] == theBoard['2']:
        return f"Great job, {theBoard['8']}. You won!\n"

    elif theBoard['9'] != ' ' and theBoard['9'] == theBoard['6'] and theBoard['6'] == theBoard['3']:
        return f"Great job, {theBoard['9']}. You won!\n"
    # Diagonal
    elif theBoard['7'] != ' ' and theBoard['7'] == theBoard['5'] and theBoard['5'] == theBoard['3']:
        return f"Great job, {theBoard['7']}. You won!\n"

    elif theBoard['9'] != ' ' and theBoard['9'] == theBoard['5'] and theBoard['5'] == theBoard['1']:
        return f"Great job, {theBoard['9']}. You won!\n"
    else:
        return 'keep playing'


# Tic Tac Toe game itself using a series of nested while loops to keep rerunning either the game or various turns within the game.
keep_playing = True
while keep_playing:

    # The board as blank spaces to start
    theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '1': ' ' , '2': ' ' , '3': ' ' }
    
    # Printing the board with it's entry points.
    def printBoard(board):
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])

    # Game instructions below:
    print("Instructions: Enter a number from 1-9 when it is your turn. 7-9 represents the top row, 4-6 the middle, and 1-3 the bottom row. Type 'Exit' at any time to end the program.\n")
    print("Player 1 will go first and will be X's. Player 2 will go second and be O's. Enter your names for a random assignment as player 1 or player2.\n")
    
    # Logic for users to enter their names to randomly assign turn order.
    name1 = input('Input first name.\n') 
    printable_n1 = name1

    name2 = input('Input second name.\n')
    printable_n2 = name2

    # Function to randomly assign turn order.
    player_assignment(name1, name2)
    printBoard(theBoard)

    # Legal moves on the board to enforce a check in the game itself
    legal_moves = [1,2,3,4,5,6,7,8,9]

    # Individual game with 9 turn maximum. Game will have multiple ways to end
    turns = 9
    while turns > 0:
        stop = False
        keep_running = True
        while keep_running:
            p1_turn = input("Player1, what is your move?\n")
            if p1_turn.isnumeric()  and int(p1_turn) in legal_moves:
                if theBoard[p1_turn] == ' ':
                    theBoard[p1_turn] = player_1
                    printBoard(theBoard)
                    turns -=1
                    keep_running = False
                else: 
                    print("Sorry, that spot's been taken, replay your turn.\n")
                    continue
            elif p1_turn.lower() == 'exit':
                    turns = 0
                    stop = True
                    keep_playing = False
                    print("Thanks for playing!\n")
                    break
            else:
                print("Sorry, your input was not a number between 1 and 9.\n")
                continue
        x = check_for_winners(theBoard)
        if 'won' in x:
            print(x)
            turns = 0
            break
        elif stop == True:
            turns = 0
            break
        elif turns == 0:
            print("Game is a draw, play again.\n")
            turns = 0
            break
        keep_running2 = True
        while keep_running2:
            p2_turn = input("Player2, what is your move?\n")
            if p2_turn.isnumeric() and int(p2_turn) in legal_moves:
                if theBoard[p2_turn] == ' ':
                    theBoard[p2_turn] = player_2
                    printBoard(theBoard)
                    check_for_winners(theBoard)
                    turns -=1
                    keep_running = False
                else: 
                    print("Sorry, that spot's been taken, replay your turn.\n")
                    continue
            elif p2_turn.lower() == 'exit':
                    turns = 0
                    stop = True
                    keep_playing = False
                    print("Thanks for playing!\n")
                    break
            else:
                print("Sorry, your input was not a number between 1 and 9.\n")
                continue
            x = check_for_winners(theBoard)
            if 'won' in x:
                turns = 0
            elif turns == 0:
                print("Game is a draw, play again.\n")
                turns = 0
                break
            keep_running2 = False