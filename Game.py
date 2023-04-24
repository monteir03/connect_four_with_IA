from copy import deepcopy

ROWS=6
COLS=7
#1ª: 1 X
#2ª: -1 O
class Game:
    
    def __init__(self,config) :
        self.state=config
        self.turn=self.to_move()
        self.last=None

    def __repr__(self):
        string='| 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n'
        for i in self.state:
            string+='+———+———+———+———+———+———+———+\n'
            string+='| '
            for j in i:
                string+=j
                string+=' | '
            string+='\n'
        string+='+———+———+———+———+———+———+———+\n'
        return string

    def __eq__(self,other):    
        if self.state==other.state:
            return True
        return False
    
    def to_move(self): #de quem é a vez de jogar
        sum_of_moves=0
        for i in self.state:
            for j in i:
                if(j=='X' or j=='O'):
                    sum_of_moves+=1
        if sum_of_moves%2==0:
            return 1 #X
        elif sum_of_moves%2==1:
            return -1 #O
    
    def has_space(self,col):#[0-6] #verificar se a coluna tem espaço para jogar
        if self.state[0][col]==' ':
            return True
        return False

    def full(self):
        for i in range(7):
            if self.state[0][i] == ' ':
                return False
        return True

    def move(self,col):#1-7 jogada
        self.last=col #guarda o move para ser considerado como o ultimo no minimax
        col-=1
        if self.has_space(col):
            i=0
            while(i<6 and self.state[i][col]==' '):
                i+=1
            i-=1
            if self.turn==1:
                self.state[i][col]='X'
                self.turn=self.to_move() 
                return
            elif self.turn==-1:
                self.state[i][col]='O' 
                self.turn=self.to_move()  
                return 

    def result(self,m): 
        result=deepcopy(self) 
        result.move(m)
        return result
    
    def legal_actions(self): 
        lista=[]
        if self.is_terminal()==False:
            for i in range(7):
                if self.has_space(i):
                    lista.append(i+1)
        return lista
    
    def possible_moves(self):
        lista=[]
        for i in self.legal_actions():
            jogo=self.result(i)
            lista.append(jogo)
        return lista

    def winner(self):
        if self.utility()==512:
            return 1                #Vitoria X
        elif self.utility()==-512:
            return -1               #Vitoria O
        return 0                    #Empate
        
    def is_terminal(self): 
        if (self.utility()==512) or (self.utility()==-512) or (self.full()==True):
            return True 
        return False    

#utilities
    def utility(self):
        if self.full()==True:
            return 0
        segment=[] # guardar segmentos de 4
        value=0
        #linhas
        for i in range(ROWS):
            for j in range(COLS-3):
                segment=self.state[i][j:j+4]
                k=self.evaluate_segment(segment)
                if k==512 or k==-512:
                    return k
                value+=k
        #colunas
        for i in range(COLS):
            for j in range(ROWS-3):
                segment=[self.state[j+inc][i] for inc in range(4)]
                k=self.evaluate_segment(segment)
                if k==512 or k==-512:
                    return k
                value+=k
        # diagonais do triangluo inferior esquerdo
        for i in range(ROWS-3):
            l=i
            for j in range(COLS-3-1-i):
                segment=[self.state[l+inc][j+inc] for inc in range(4)]
                k=self.evaluate_segment(segment)
                if k==512 or k==-512:
                    return k
                value+=k
                l+=1
        # diagonais do triangulo superior esquerdo
        for i in range(3,ROWS):
            l=i
            for j in range(COLS-3-(ROWS-i)):
                segment=[self.state[l-inc][j+inc] for inc in range(4)]
                k=self.evaluate_segment(segment)
                if k==512 or k==-512:
                    return k
                value+=k
                l-=1
        # diagonais do traingulo inferior direito (sem repetiçao de uma das diagonais maior)
        for i in range(ROWS-3):
            l=i
            for j in range(6,6-3+i,-1):#6,6-3+i,-1
                segment=[self.state[l+inc][j-inc] for inc in range(4)]
                k=self.evaluate_segment(segment)
                if k==512 or k==-512:
                    return k
                value+=k
                l+=1
        # diagonais do triangulo superior direito (sem repetiçao de uma das diagonais maior)
        for i in range(5,2,-1):
            l=i
            for j in range(6,6-(i-2),-1):
                segment=[self.state[l-inc][j-inc] for inc in range(4)]
                k=self.evaluate_segment(segment)
                if k==512 or k==-512:
                    return k
                value+=k
                l-=1
        
        return value
        
    def evaluate_segment(self,section):
        countx=0
        county=0
        value=0
        for i in section:
            if i=='X':
                countx+=1
            elif i=='O':
                county+=1

        if county==0 and countx!=0:
            if countx==4:
                return 512
            elif countx==3:
                return 50
            elif countx==2:
                return 10
            elif countx==1:
                return 1
        elif countx==0 and county!=0:
            if county==4:
                return -512
            elif county==3:
                return -50
            elif county==2:
                return -10
            elif county==1:
                return -1
        return 0

