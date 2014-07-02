from random import randint

board=[["O"]*5 for x in range(5)]
  
def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#assigns a random location to the first ship
first_ship_row = random_row(board)
first_ship_col = random_col(board)

#assigns a location to a second ship, and checks to make sure it isn't the same location as the first ship
second_ship_row = random_row(board)
while second_ship_row==first_ship_row:
    second_ship_row=random_row(board)
second_ship_col = random_col(board)
while second_ship_col==first_ship_col:
    second_ship_col=random_col(board)
    
#print first_ship_row, first_ship_col
#print second_ship_row, second_ship_col

#assigns values for whether the ships are sunk (1) or not (0)
first_ship_sunk=0
second_ship_sunk=0

#loops through 4 turns
for turn in range(4):
    print "Turn ", turn+1
    
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if (guess_row == first_ship_row and guess_col==first_ship_col):
        print "Congratulations! You sank a battleship!"
        first_ship_sunk=1
        #changes board to indicate positon where ship was sunk
        board[guess_row][guess_col]="-"
    elif guess_row==second_ship_row and guess_col==second_ship_col:
        print "Congratulations! You sank a battleship!"
        second_ship_sunk=1
        board[guess_row][guess_col]="-"
    
    #this will execute as long as one of the ships isn't sunk yet
    elif first_ship_sunk+second_ship_sunk<2:
        #checks to see if guess is on the board
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
              
        #checks to see if the guess has been made already in a previous turn        
        elif(board[guess_row][guess_col] == "X") or (board[guess_row][guess_col]=="-"):
            print "You guessed that one already."
                
        else:
            print "You missed my battleships!"
            #marks location of guess on the board
            board[guess_row][guess_col] = "X"
                
    #at the end of the turn, if both the ships have been sunk, the game is over and the player has won
    if first_ship_sunk==1 and second_ship_sunk==1:
            print "You sank all my battleships - You win!"
            break
    print_board(board)
    
#if first_ship_sunk==1 and second_ship_sunk==1:
 #   print "You sunk all my battleships! You win!"
else:
    print "Game Over"
  
