# Connected_ Four

#### To play ConnectedFour against an AI opponent, first choose a search algorithm: minimax, alphabeta_pruning, or MCTS algorithm.

### To play with minimax:
Make sure you have the files Game.py and minimax.py.
Then, run "python3 minimax.py" in your terminal to start the game.
If you want to change the depth limit for minimax, you need to access the minimax.py file and select the desired limit where it says "choose depth."

### To play with alphabeta:
Make sure you have the files Game.py and alphabeta.py.
Then, run "python3 alphabeta.py" in your terminal to start the game.
If you want to change the depth limit for alphabeta, you need to access the alphabeta.py file and select the desired limit where it says "choose depth."

### To play with Monte Carlo Tree Search (MCTS):
Make sure you have the files Game.py and montecarlo.py.
Then, run "python3 montecarlo.py" in your terminal to start the game.
This search algorithm depends on time, so if you want to change the time limit for MCTS, you need to access the montecarlo.py file and choose the desired time where it says "choose time."

For Monte Carlo, you can also change the way it chooses its moves. By default, the choice is based on the UCB value of the children of the current move. But, if you want to, you can make this choice based on the number of visits using the "play_according_to_visits()" function (changeing "Search.play_according_to_UCT()" with "Search.play_according_to_visits() where is written "#change function"). However, through the tests we've done, we've understood that Monte Carlo performs better with UCB.


you will allways be the first player
