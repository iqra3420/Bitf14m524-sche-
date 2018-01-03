from __future__ import print_function

option = []

for x in range (0, 9) :
    option.append(str(x + 1))

playerOne = True
win = False

def gameBoard() :
    print( '\n -----')
    print( '|' + option[0] + '|' + option[1] + '|' + option[2] + '|')
    print( ' -----')
    print( '|' + option[3] + '|' + option[4] + '|' + option[5] + '|')
    print( ' -----')
    print( '|' + option[6] + '|' + option[7] + '|' + option[8] + '|')
    print( ' -----\n')

while not win :
    gameBoard()

    if playerOne :
        print( "Player A:")
    else :
        print( "Player B:")

    try:
        opt = int(input(">> "))
    except:
        print("please enter a valid field")
        continue
    if option [opt - 1] == 'X' or option [opt-1] == 'Y':
        print("Plase try again!")
        continue

    if playerOne :
        option[opt - 1] = 'X'
    else :
        option[opt - 1] = 'Y'

    playerOne = not playerOne

    for x in range (0, 3) :
        y = x * 3
        if (option[y] == option[(y + 1)] and option[y] == option[(y + 2)]) :
            win = True
            gameBoard()
        if (option[x] == option[(x + 3)] and option[x] == option[(x + 6)]) :
            win = True
            gameBoard()

    if((option[0] == option[4] and option[0] == option[8]) or 
       (option[2] == option[4] and option[4] == option[6])) :
        win = True
        gameBoard()

print ("Player " + str(int(playerOne + 1)) + " won!\n")
raw_input()
