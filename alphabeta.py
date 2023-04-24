from Game import *

def alpha_beta_search(game,depth=4):  #choose depth
    if game.turn==1:
        _ , value2 = MAX(game,float("-inf"),float("inf"),depth)
    elif game.turn==-1:
        _ , value2 = MIN(game,float("-inf"),float("inf"),depth)
    return value2

def MAX(game,alpha,beta,depth):
    col=None
    if game.is_terminal() or depth==0:
        col=game.last
        return game.utility(),col
    
    max_value = float("-inf")
    for s in game.possible_moves():
        value, _ = MIN(s,alpha,beta, depth - 1)
        if value>max_value:
            max_value=value
            col=s.last
        if max_value>=beta:
            break
        alpha=max(alpha,max_value)

    return max_value,col

def MIN(game,alpha,beta,depth):
    col=None
    if game.is_terminal() or depth==0:
        col=game.last
        return game.utility(),col

    min_value = float("inf")
    for s in game.possible_moves():
        value, _ = MAX(s,alpha,beta, depth - 1)
        if value<min_value:
            min_value=value
            col = s.last
        if min_value<=alpha:
            break
        beta=min(beta,min_value)

    return min_value,col

def play_alpha_beta():
    config=[[' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ']]
    jogo=Game(config)
    print(jogo)

    while (not jogo.is_terminal()):
        if jogo.turn==1:
            column=int(input())
            jogo.move(column)
            print(jogo)
        else:
            col=alpha_beta_search(jogo)
            jogo.move(col)
            print(jogo)
            
    if jogo.winner()==1:
            print("X WINS")
    elif jogo.winner()==-1:
            print("O WINS")
    else:
            print("DRAW") 

play_alpha_beta()