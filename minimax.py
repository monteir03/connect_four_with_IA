from Game import *
import time

def minimax_search(game,depth=4): #define aqui a profundidade
    if game.turn==1:
        _ , value2 = MAX(game,depth)
    elif game.turn==-1:
        _ , value2 = MIN(game,depth,)
    return value2

def MAX(game,depth,):
    col=None
    if game.is_terminal() or depth==0:
        col=game.last
        return game.utility(),col
    
    max_value = float("-inf")
    for s in game.possible_moves():
        value, _ = MIN(s, depth - 1)
        if  value>max_value:
            max_value=value
            col=s.last

    return max_value,col

def MIN(game,depth,):
    col=None
    if game.is_terminal() or depth==0:
        col=game.last
        return game.utility(),col

    min_value = float("inf")
    for s in game.possible_moves():
        value, _ = MAX(s, depth - 1,)
        if value<min_value:
            min_value=value
            col = s.last
            
    return min_value,col


def play_minimax():
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
            col=minimax_search(jogo)
            jogo.move(col)
            print(jogo)

    if jogo.winner()==1:
            print("X WINS")
    elif jogo.winner()==-1:
            print("O WINS")
    else:
            print("DRAW") 

play_minimax()