def genBoard(dimension):
    table = [["-" for c in range(dimension)] for r in range(dimension)]
    return table

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end = " ")
        print("\n")

def checkWinDiag1(board):
    c = board[0][0]
    count = 0
    for i in range(len(board)):
        if (c == board[i][i]):
            count += 1
    if(count == len(board) and c != "-"):
        return True
    return False

def checkWinDiag2(board):
    c = board[0][len(board)-1]
    count = 0
    i = 0
    for x in range(len(board)-1, -1, -1):
        if (c == board[i][x]):
            count += 1
            i += 1
    if(count == len(board) and c != "-"):
        return True
    return False 

def checkWinHorizontal(board):
    count = 0
    for i in range(len(board)):
        c = board[i][0]
        for j in range(len(board)):
            if (c == board[i][j]):
                count += 1
        if (count == len(board) and c != "-"):
            return True
        count = 0
    return False

def checkWinVertical(board):
    count = 0
    for i in range(len(board)):
        c = board[0][i]
        for j in range(len(board)):
            if (c == board[j][i]):
                count += 1
        if (count == len(board) and c != "-"):
            return True
        count = 0
    return False

def finalCondition(board):
    if (checkWinDiag1(board)):
        return True
    elif (checkWinDiag2(board)):
        return True
    elif (checkWinHorizontal(board)):
        return True
    elif (checkWinVertical(board)):
        return True
    else:
        return False

win = False

dimension = int(input("Please enter the dimension of the tic tac toe board: "))
board = genBoard(dimension)
print("this is the current board")
printBoard(board)

#board [y][x]
#p1 is X
#p2 is O

count = 0
while(win == False):
    valid_input1 = False
    if (count == dimension**2):
        print("it's a tie")
        break
    while (valid_input1 == False):
        p1_x = int(input("Player 1 (X): enter the x location for your move: "))
        p1_y = int(input("Player 1 (X): enter the y location for your move: "))
        if (board[p1_y][p1_x] == "-"):
            board[p1_y][p1_x] = "X"
            valid_input1 = True
            count += 1
        else:
            print("Invalid input. Please try again.")
    printBoard(board)
    if (finalCondition(board)):
        print("player 1 won the game!")
        win = True
        break
    if (count == dimension**2):
        print("it's a tie")
        break
    valid_input2 = False
    while(valid_input2 == False):
        p2_x = int(input("Player 2 (O): enter the x location for your move: "))
        p2_y = int(input("Player 2 (O): enter the y location for your move: "))
        if (board[p2_y][p2_x] == "-"):
            board[p2_y][p2_x] = "O"
            valid_input2 = True
            count += 1
        else:
            print("Invalid input. Please try again.")
    printBoard(board)
    if (finalCondition(board)):
        print("player 2 won the game!")
        win = True
        break