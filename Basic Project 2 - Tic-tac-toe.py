#set up the game board as a list
board=["-","-","-",
       "-","-","-",
       "-","-","-"]
def print_board():
    print(
        board[0]+"|"+board[1]+"|"+board[2]+"\n"+
        board[3]+"|"+board[4]+"|"+board[5]+"\n"+
        board[6]+"|"+board[7]+"|"+board[8]
        )

#define a function to handle a player's turn
def take_turn(player):
    print(player+"'s turn.")
    position=input("Choose a position from 1-9:")
    while position not in ["1","2","3","4","5","6","7","8","9"]:
        position=input("Invalid input.Choose a position from 1-9:")
    position = int(position) - 1 #to match with index 
    while board[position]!="-":
        position=input("Position already taken. Choose a different position:")-1
    board[position]=player #mark position as player X or O
    print_board()
    
#define a function to check if game is over
def check_game_over():
    # check for a win
    if(board[0]==board[1]==board[2]!="-") or \ #horizontal
      (board[3]==board[4]==board[5]!="-") or \
      (board[6]==board[7]==board[8]!="-") or \
      (board[0]==board[3]==board[6]!="-") or \ #vertical
      (board[1]==board[4]==board[7]!="-") or \
      (board[2]==board[5]==board[8]!="-") or \
      (board[0]==board[4]==board[8]!="-") or \ #diagnol 
      (board[2]==board[4]==board[6]!="-"):
        return "win"
    elif "-" not in board:
        return "tie"
    else:
        return "play"

def play_game():
    print_board()
    current_player="X" #X starts 
    game_over=False
    while not game_over:
        take_turn(current_player)   #current player plays 
        game_result=check_game_over() #check if the game is over 
        if game_result=="win":
            print(current_player + " wins!")
            game_over=True
        elif game_result=="tie":
            print("It's a tie.")
            game_over=True
        else:
            current_player="O" if current_player=="X" else "X" #switch the player 

play_game()

                                          
