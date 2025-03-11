def display_board(board):

    print('     -------------')
    print('     | '+board[7]+' | '+board[8]+' | '+board[9]+' |')
    print('     -------------')
    print('     | '+board[4]+' | '+board[5]+' | '+board[6]+' |')
    print('     -------------')
    print('     | '+board[1]+' | '+board[2]+' | '+board[3]+' |')
    print('     -------------')


test_board=[' ']*10
pl1=''
pl2=''

def choose_player():
    from random import randint
    global pl1,pl2
    pl1=input("Enter first player name:")
    pl2=input("Enter second player name:")
    player=randint(1,2)
    if player==1:
        return pl1
    else:
        return pl2


def player_input(s):
    marker=''
    
    while marker!='X' and marker!='O':
        marker=input("Enter your preferable marker,{} ('X' or 'O'):".format(s))
    if marker=='O':
        return ("O","X")
    else:
        return("X","O")

#print(player1_marker)
#print(player2_marker)

def isavailable(board,pos):
    if board[pos]==' ':
        return True
    else: return False

def place_position(player):
    choice=''
    accptable_range=range(1,10)
    within_range=False
    while choice.isdigit()==False or within_range==False:
        choice=input("Enter a position {}, in which you want to place the marker(1-9):".format(player))
        if choice.isdigit()==False:
            pass
        if choice.isdigit()==True:
            if int(choice) in accptable_range:
                within_range=True
                print("Ok.We know your position")
            else:
                print("Out of bounds number.Please select a number from(1-9)")
    return int(choice)



def modified_board(test_board,player1_choice,pos):
    if isavailable(test_board,pos):
        test_board[pos]=player1_choice
        print("Here is your updated board")
        display_board(test_board)
    else:
        
        print("This position is already filled")
        return -1
    return 0



def win_check(board,marker):
    return(
    (board[1]==marker and board[2]==marker and board[3]==marker)or 
    (board[4]==marker and board[5]==marker and board[6]==marker)or
    (board[7]==marker and board[8]==marker and board[9]==marker)or
    (board[1]==marker and board[4]==marker and board[7]==marker)or
    (board[2]==marker and board[5]==marker and board[8]==marker)or
    (board[3]==marker and board[6]==marker and board[9]==marker)or
    (board[1]==marker and board[5]==marker and board[9]==marker)or
    (board[3]==marker and board[5]==marker and board[7]==marker)) 





def full_board_check(board):
    for i in range(1,10):
        if board[i]==' ':
            return False
    return True

def replay():
    opinion_list=['y','n']
    opinion=''
    while opinion.lower() not in opinion_list:
        opinion=input("Do you want to play more?(y/n):")
        if opinion.lower() not in opinion_list:
            print("Please enter 'y' or 'n'")
        
    return opinion


#------------Logic for Building Actual Game-----------
print("Welcome to Tic Tac Toe Game")
game_on=True
while game_on==True:
    print("Here is your Tic Tac Toe board")
    display_board(test_board)
    player=choose_player()

    print("Ok guys!We will pick a random player between you to ensure who will play first")
    print("So we select {} to play first".format(player))
    #print(player)
    player1_marker,player2_marker=player_input(player)

    if player==pl1:
        print("{} got the marker {}".format(pl1,player1_marker))
        print("{} got the marker {}".format(pl2,player2_marker))
    else:
        player1_marker,player2_marker=player2_marker,player1_marker#swapping for getting the correct marker
        print("{} got the marker {}".format(pl1,player1_marker))
        print("{} got the marker {}".format(pl2,player2_marker))

    display_board(test_board)
    game_decision=''
    while game_decision!=True and full_board_check(test_board)!=True:
        if player==pl1:
            pos=place_position(player)

            if(modified_board(test_board,player1_marker,pos)==-1):
                    
                player=pl1
                #print(game_decision)
            else:
                player=pl2
            game_decision=win_check(test_board,player1_marker)

            if(game_decision==True):
                print("Congratulations,{}!! You have won the game".format(pl1))
                break
            if full_board_check(test_board)==True:
                print("The match is tied")
        else:
            pos=place_position(player)
            if(modified_board(test_board,player2_marker,pos)==-1):
  
                player=pl2
            #print(game_decision)
            else:
                player=pl1
            game_decision=win_check(test_board,player2_marker)

            if(game_decision==True):
                print("Congratulations,{}!! You have won the game".format(pl2))
                break
            if full_board_check(test_board)==True:
                print("The match is tied")

    if replay()=='y':
        game_on=True
        test_board=[' ']*10
    else:
        print("Terminating the game...")
        game_on=False




