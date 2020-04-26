board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def printBoard():
  print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")                                   
  print("---|---|---")
  print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")  
  print("---|---|---")
  print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")                                   


def checkWin():
  if(board[0] == board[1] and board[0] == board[2] and board[0]  != ' ' ): #Across The Top
    return True    
  elif (board[3] == board[4] and board[3] == board[5] and board[3] != ' ' ):#Across The Middle
    return True
  elif (board[6] == board[7] and board[6] == board[8] and board[6] != ' ' ):#Across The Bottom
    return True
  elif (board[0] == board[4] and board[0] == board[8] and board[0] != ' ' ):#Diagonal
    return True2
  elif (board[2] == board[4] and board[2] == board[6] and board[2] != ' ' ):#Diagonal
    return True
  elif (board[0] == board[3] and board[0] == board[6] and board[0] != ' ' ):#down the left
    return True
  elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' ' ):#down the middel 
    return True
  elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' ' ):#down the right
    return True

#Start Game
printBoard()
turn = True
game = True

while(game):
  if(turn):
    move = int(input("player one, please enter a move from 0 to 8"))
    
    while (move>8 or move<0 or board[move]!=' '):
      move = int(input("That is an invalid move. Please enter a new move"))

    board[move] = 'X'
    printBoard()
    turn = False
  
    if(checkWin()):
      print("X wins")
      game = False
      break

    elif not(turn):
      move = int(input("player One, please enter a move from 0 to 8"))
      
      board[move] = 'O'
      printBoard()
      turn = True
  
    if(checkWin()):
      print("O wins")
      game = False
      break   
  








