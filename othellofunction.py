import random
import time
from fourlinefile import *
import copy
def printf(l): #Prints the board
    ''' This function prints the matrix in a readable manner'''
    print " ",
    for i in range(8):
        print i,
    print
    k = 0
    for i in l:
        print k,
        for j in i:
            print j,
        print ""
        k+=1

def counter(l): # Counts the number of X's and O's
    ''' This function counts the number of X's and O's'''
    #Try to shorten
    countX,countO = 0,0
    for i in l:
        for j in i:
            if j=="X":
                countX+=1
            elif j=="O":
                countO+=1
    return [countX,countO]

def check(l,c): #This function returns a dictionary of coordinates of all the empty positions around X or O
    ''' This function returns a dictionary of coordinates of all the empty positions around X or O.
    The dictionary return type is of the form {(coordinates):[list of tuples of coordinates around
    it.]}'''
    m = []
    b=  []
    d = {}
    #Try to shorten the codes
    for i in range(8):
        for j in range(8):
            if l[i][j] == c:
                m.append((i,j))
    for i in m:
        x,y = i
        for j in range(-1,2):
            for k in range(-1,2):
                if j==0 and k==0:
                    continue
                elif x+j >7 or x+j<0 or y+k>7 or y+k<0:
                    continue
                elif l[x+j][y+k]!= "-":
                    continue
                elif (x,y) in d:
                    d[(x,y)].append((x+j,y+k))
                else:
                    d[(x,y)]=[(x+j,y+k)]
                    #print d
    return d
    
def checkValidity(l,k): 
    m = []
    if k: c = "X";e = "O"
    else: c = "O";e = "X"
    if e == "X":checkdict = check(l,c)
    else: checkdict = check(l,c)
    d = checkdict
    d1 = {}
    for i in d:
        '''For each possible sqaure around the coin, check if a move is valid.''' 
        for j in range(len(d[i])):
            count = 0 #This is the score of each move
            t = (i[0] - d[i][j][0],i[1] - d[i][j][1]) #This indicates the direction to move in
            if d[i][j] not in d1:
                d1[d[i][j]] = []
            k = recur(l,d[i][j],d[i][j],i,t,d1)
            if k[1]:
                l[d[i][j][0]][d[i][j][1]] = '+'
                d1.update(k[0])
    d2,count = {},0
    for i in d1:
        if d1[i]:
            d2[i] = d1[i]
            count+=1
    if count: return [d2,True]
    else: return [{},False]

def recur(l,first,old,t,dif,d1):
    ''' Old is the guy who undergoes recursion. first is the starting pint of the recursion(the square for whose validity is being checked.) d1 is the ditionary being passed repatedly to get updated. dif is the tuple of the direction co-ordinates. '''
    x,y = t #t is the coin around which we are trying to validate moves in 
    a,b = dif #Direction
    n,m = old 
    p,q = n+a,m+b #The new square
    if p>7 or p<0 or q>7 or q<0:
        return [{},False] #Subject to change
    elif l[p][q]=='+':
        return [d1,False]
    elif l[p][q]=='-':
        return [{},False] #Subject to change
    elif l[x][y]== l[p][q]:
        z =  recur(l,first,(p,q),t,dif,d1)
        if z[1]:
            if first in d1:
                d1[first].append((p,q))
            else:
                d1[first] = [(p,q)]
        return z
    elif (l[x][y]=='O' and l[p][q]=='X') or (l[x][y]=='X' and l[p][q]=='O'):
        return [d1,True] 

def change(l,c,d,t):
    ''' This function changes the blacks to whites and vice-versa.'''
    m = d[t]
    x,y = t
    l[x][y] = c
    for i in m:
        x,y = i
        l[x][y] = c
    #restart(l)
    
def restart(l):
    '''This is used to restart the matrix i.e. to remove the markers for the available moves.'''
    for i in range(8):
        for j in range(8):
            if l[i][j]=="+":
                l[i][j] = "-"
            elif l[i][j] =="#": l[i][j] = "X"
            elif l[i][j] == "0": l[i][j] = "O"



def twoplayer(x,y,colour,l,count):
    '''As the name suggests, this function is responsible for the 2 player mode'''
    w = counter(l)
    if w[0]+w[1] == 64 or w[0]==0 or w[1]==0:
        return [False,w[0],w[1]]
    returnlist = [None]*5
    returnlist[4] = True
    restart(l)
    returnlist[2] = l
    returnlist[3] = count
    if colour: c = "O"
    else: c = "X"
    b = checkValidity(l,colour)
    if b[1]:
        returnlist[3] = 0
        dictionary = b[0]
        if (x,y) in dictionary.keys():
            change(l,c,dictionary,(x,y))
            returnlist[2] = l[:][:]
        else: return False

    else:
        dictionary = {}
        returnlist[2] = l
        returnlist[3]+=1
        if returnlist[3]>2:
            returnlist[4] = False
    w = counter(l)
    returnlist[0],returnlist[1] = w
    restart(l)
    printf(l)
    b = checkValidity(returnlist[2],not colour)
    return returnlist


def cpu(f,x,y,count,l):
    '''Here f is a function which would be called depending on the difficulty of the cpu. The first half of the code is the calculation required for the player's move while the second half is for the CPU'''
    restart(l)
    w = counter(l)
    if w[0]+w[1] == 64 or w[0]==0 or w[1]==0:
        return [False,w[0],w[1]]
    boolean = "O"
    cpu1 = "X"
    returnlist = [0]*5
    returnlist[2] = []
    returnlist[4] = True
    returnlist[3] = count
    b = checkValidity(l,True)
    if b[1]:
        returnlist[3] = 0
        dictionary = b[0]
        if (x,y) in dictionary.keys():
            change(l,boolean,dictionary,(x,y))
            restart(l)
        else: restart(l);return False
    else:
        dictionary = {}
        returnlist[3]+=1
        if returnlist[3]>2:
            returnlist[4] = False
    #drawgrid(l)
    #pygame.time.wait(1000)
    #time.sleep(1)
    #for i in range(30):
    #    drawgrid(l)
    #t_end = time.time() + 1
    #while True:
    #    if time.time()<t_end:
    #        drawgrid(l)
    #   else: break
    b = checkValidity(l,False)
    if b[1]:
        returnlist[3] = 0
        dictionary = b[0]
        t = f(dictionary,l)
        change(l,cpu1,dictionary,t)
        returnlist[2] = l[:][:]
    else:
        returnlist[2] = l
        returnlist[3]+=1
        if returnlist[3]>2:
            returnlist[4] = False
    w = counter(l)
    returnlist[0],returnlist[1] = w
    restart(l)
    b = checkValidity(returnlist[2],True)
    return returnlist

def easy(d = {},l = []): #Uses a greedy approach
    max = 0
    l = []
    for i in d:
        n = len(d[i])
        if n>max:
            l = []
            l.append(i)
            max = n
        elif n==max:
            l.append(i)
    k = len(l)
    k-=1
    r = random.randint(0,k)
    return l[r]

def medium(d = {},l = []):#Does the same stuff as easy, but prefers edges and corners more
    d1 = {}
    for i in d:
        d1[i] = len(d[i])
    for i in d1:
        m = counter(l)
        if (i[0]==0 and i[1]!=0) or (i[0]==7 and i[1]!=7):
            if (i[1]+1<7 and l[i[0]][i[1]+1]=="O" and m[0]+m[1]<40) or (i[1]-1>0 and l[i[0]][i[1]-1]=="O" and m[0]+m[1]<40):
                d1[i]+=3
            d1[i]+=1
        if (i[1]==0 and i[0]!=0 and i!=(7,0)) or (i[1]==7 and i[0]!=7 and i!=(0,7)):
            if (i[0]+1<7 and l[i[1]][i[0]+1]=="O" and m[0]+m[1]<40) or (i[0]-1>0 and l[i[1]][i[0]-1]=="O" and m[0]+m[1]<40):
                d1[i]+=3
            d1[i]+=1
        elif i == (0,0) or i==(0,7) or i == (7,0) or i == (7,7):
            d1[i] += 5
        d1[i]+=len(d[i])
        
    m,max = [],-99999999
    for i in d1:
        if d1[i]>max:
            m = []
            max = d1[i]
            m.append(i)
        elif d1[i]==max:
            m.append(i)
    k = len(m)
    k-=1
    r = random.randint(0,k)
    return m[r]

def hard(d = {},l = []):#Does the same stuff as medium, but just one step ahead
    d1 = {}
    for i in d:
        d1[i] = len(d[i])
    for i in d1:
        m = counter(l)
        if (i[0]==0 and i[1]!=0) or (i[0]==7 and i[1]!=7):
            if (i[1]+1<7 and l[i[0]][i[1]+1]=="O" and m[0]+m[1]<40) or (i[1]-1>0 and l[i[0]][i[1]-1]=="O" and m[0]+m[1]<40):
                d1[i]+=4
            d1[i]+=1
        if (i[1]==0 and i[0]!=0 and i!=(7,0)) or (i[1]==7 and i[0]!=7 and i!=(0,7)):
            if (i[0]+1<7 and l[i[1]][i[0]+1]=="O" and m[0]+m[1]<40) or (i[0]-1>0 and l[i[1]][i[0]-1]=="O" and m[0]+m[1]<40):
                d1[i]+=4
            d1[i]+=1
        elif i == (0,0) or i==(0,7) or i == (7,0) or i == (7,7):
            d1[i] += 7
        d1[i]+=len(d[i])
    
    k = l[:][:]
    for j in d1:
        k = copy.deepcopy(l)
        b=  {}
        change(k,"X",d,j)
        w = counter(k)
        if w[0]!=0 and w[1]!=0 and w[0]+w[1]<62:
            b = checkValidity(k,True)
            if not b:continue
        else:
            continue
        e = {}
        if b[1]:
            for a in b[0]:
                e[a] = len(b[0][a])
        for i in e:
            m = counter(l)
            if (i[0]==0 and i[1]!=0) or (i[0]==7 and i[1]!=7):
                if (i[1]+1<7 and l[i[0]][i[1]+1]=="X" and m[0]+m[1]<41) or (i[1]-1>0 and l[i[0]][i[1]-1]=="X" and m[0]+m[1]<41):
                    e[i]+=5
                e[i]+=1
            if (i[1]==0 and i[0]!=0 and i!=(7,0)) or (i[1]==7 and i[0]!=7 and i!=(0,7)):
                if (i[0]+1<7 and l[i[1]][i[0]+1]=="X" and m[0]+m[1]<41) or (i[0]-1>0 and l[i[1]][i[0]-1]=="X" and m[0]+m[1]<41):
                    e[i]+=5
                e[i]+=1
            elif i == (0,0) or i==(0,7) or i == (7,0) or i == (7,7):
                e[i] += 20
            e[i]+=len(b[0][i])
        try:
            max1 = max(e.values())
        except:
            continue
        d1[j]-=max1

    m,max2 = [],-9999999
    for i in d1:
        if d1[i]>max2:
            m = []
            max2 = d1[i]
            m.append(i)
        elif d1[i]==max2:
            m.append(i)
    r = len(m)
    if r!=0: r-=1;s = random.randint(0,r)
    else: s = 0
    return m[s]


    
def run(l,x,y,count,colour = True,gametype = 1,difficulty = 0): #This is the general function which handles which path the game should take
    games = [twoplayer,cpu]
    cpu1 = [easy,medium,hard]
    if gametype==1:
        return games[1](cpu1[difficulty],x,y,count,l)
    elif gametype==0:
        return games[0](x,y,colour,l,count)
