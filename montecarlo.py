from Game import *
import math                    
import random                     
import time



#turns
class Node:

    def __init__(self,state,parent=None):
        self.state=state 
        self.w=0          #win count
        self.v=0          #visit count
        self.children=[]
        self.parent=parent

    def __lt__(self,other):
        return self.f_uct()<other.f_uct()

    def __eq__(self,other):
        return self.f_uct()==other.f_uct()

    def f_uct(self):
        if self.v==0:
            return  100000000000   #consider infinity
        return (self.w/self.v)+math.sqrt(2)*math.sqrt(math.log(self.parent.v)/self.v) 
          
    def get_highest_child(self):                    
        if len(self.children)!=0:                                      
            return max(self.children)           

    def expand_node(self):
        lista=[]
        if self._is_terminal():
            return lista
        for i in self.state.possible_moves():
            no=Node(i,self)             
            lista.append(no)    
        return lista
    
    def has_child(self):
        if self._is_terminal():
            return False
        if len(self.children)>0:
            return True
        return False
   
    def has_parent(self):
        if self.parent:
            return True
        return False

    def _is_terminal(self):  
        return self.state.is_terminal()

class MCTS:

    def __init__(self,node): 
        self.root=node
        self.explored=0

    def selection(self): 
        cur=self.root  
        c=0
        if cur._is_terminal():
                return cur
        while(cur.has_child()): 
            cur=cur.get_highest_child()
            self.explored+=1
            c+=1
        if c==0:
            filhos=cur.expand_node()
            cur.children=filhos
            if cur.has_child():
                cur=cur.get_highest_child()
                self.explored+=1
        else:
            if cur.v>0:                           
                filhos=cur.expand_node()
                cur.children=filhos
                if cur.has_child():
                    cur=cur.get_highest_child() 
                    self.explored+=1
        return cur
                    
    def simulation(self,node):             
        game=deepcopy(node.state)
        while (not game.is_terminal()):
            column = random.randint(1, 7)  
            game.move(column)
        value = game.winner()
        if value==1 or value==0 :                     
            ret=0                               
        else:                                   
            ret=1                                  
        return value                 

    def back_propagate(self,node):
        if node._is_terminal():                #if terminal, no simulation()
            value=node.state.winner()         
            if value==1 or value==0:                          
                wincr=0                               
            else:                                   
                wincr=1
        else:
            wincr=self.simulation(node)        #where simultion ocurs 
        vincr=1                              
        cur=node                               
        cur.w+=wincr                           
        cur.v+=vincr                          
        while(cur.has_parent()):
            cur=cur.parent
            cur.w+=wincr
            cur.v+=vincr

    def play_according_to_UCT(self):
        next_node = self.root.get_highest_child().state  
        return next_node
    
    def play_according_to_visits(self):
        l=self.root.children
        n=l[0]
        nv=n.v
        for i in range(1,len(l)):
            if l[i].v>nv:
                n=l[i]
                nv=n.v
        return n.state

def montecarlo_search(state,limit_time):
    start_node=Node(state)                        
    Search=MCTS(start_node)                      
    init_time=time.time()
    count=0
    while time.time()-init_time <= limit_time: 
        count+=1     
        selected_node=Search.selection()
        Search.back_propagate(selected_node)
    print("iteraçoes", count)
    print("number: ", Search.explored)
    return Search.play_according_to_visits()  #change function


def play_montecarlo(limit_time):
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
        elif jogo.turn==-1:
            jogo=montecarlo_search(jogo, limit_time)     
            print(jogo)

    if jogo.winner()==1:
            print("X WINS")
    elif jogo.winner()==-1:
            print("O WINS")
    else:
            print("DRAW") 

play_montecarlo(2) #choose time in seconds
        


