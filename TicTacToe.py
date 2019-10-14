#tic tac toe
####global variables

#board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#if game is still running 
game_still_going = True 
#only false when the game is over
#who won or tie
winner = None
#whos turn is it 
current_player = "X"
#display
#create a function
def display_board():
  print("\n")
  print(board[0] +" | " + board[1] +" | " + board[2])
  print(board[3] +" | " + board[4] +" | " + board[5])
  print(board[6] +" | " + board[7] +" | " + board[8])
  print("\n")
#call the function
display_board()
#play a game- creates newgame 
#create a function
def play_game():
  display_board
  #display iitial board
  #handling a turn 
  while game_still_going:
#loop and handle a single turn of a player
    handle_turn(current_player)
    #check if game ended
    check_if_game_over()
    #flip to other player
    flip_player()

    #game over 
    if winner == "X" or winner == "O":
      print(winner + " won.")
    elif winner == None:
      print("Tie.")

def check_if_game_over():
  check_if_win()
  check_if_tie()

def check_if_win():
  #set up global variables
  global winner
  #winner matches line 13
# check rows 
  row_winner = check_rows()
#check columns 
  column_winner = check_columns()
#check diagonals
  diagonal_winner = check_diagonals()
  if row_winner:
    #someone won 
    winner = row_winner
  elif column_winner:
    #someone won 
    winner = column_winner
  elif diagonal_winner:
    #someone won
    winner = diagonal_winner
  else:
    #there was no win aka a tie 
    winner = None
  return

def check_rows():
  #set up global variable
  global game_still_going
  #check if any rows are same values and not empty
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    game_still_going = False
  #return winner (x or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return 

def check_columns():
  #set up global variable
  global game_still_going
  #check if any columns are same values and not empty
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  if column_1 or column_2 or column_3:
    game_still_going = False
  #return winner (x or O)
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return 

def check_diagonals():
  #set up global variable
  global game_still_going
  #check if any diagonals are same values and not empty
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  if diagonal_1 or diagonal_2:
    game_still_going = False
  #return winner (x or O)
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]

  return

def check_if_tie():
  global game_still_going
  if "-" not in board:
    game_still_going = True
    return False
  else:
    return True

def flip_player():
  #global variables
  global current_player
  #if the current player was x, then change to o
  if current_player == "X":
    current_player = "O"
  #if the current player was o, then change to x
  elif current_player == "O":
    current_player = "X"
  return

#handle a single turn 
def handle_turn(player):
  print(player + "'s turn.")
  position = input("choose a position from 1-9:")
  valid = False
  while not valid:
      while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Choose a position from 1-9:")
      #string 
      position = int(position) - 1

      if board[position] == "-":
        valid = True
      else:
        print("Space occupied. Try again.")


  board[position] = player
  display_board()


play_game()

#handle a turn 
#win /
  # check rows 
  #check columns 
  #check diagonals
#tie 
#flip players 
