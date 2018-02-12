from fourlinefile import *
from othellofunction import *
from checkboxes import *

def drawback():
    ''' This draws the squares'''
    for i in range(8):        
        for j in range(4):
            if i%2==1:
                k=i*100
                pygame.draw.rect(DISPLAYSURF,(0,128,0),pygame.Rect(k,100+j*200,100,100))  
            else:
                k=i*100
                pygame.draw.rect(DISPLAYSURF,(0,128,0),pygame.Rect(k,j*200,100,100)) 

def drawgrid(l,mousex,mousey):
    '''This is responsible for changin gthe the blacks to whites and vice-versa. It is also responsible for the 'hover for available move' feature'''
    a,b = mousex/100,mousey/100
   
    for i in range(8):
        for j in range(8):
            if l[i][j]=="O":
                pygame.draw.circle(DISPLAYSURF,(255,255,255),(j*100+50,i*100+50),30)
            elif l[i][j]=="X":
                pygame.draw.circle(DISPLAYSURF,(0,0,0),(j*100+50,i*100+50),30)
    if a>7 or b>7:
        return
    if(l[b][a]=="+"):
        pygame.draw.circle(DISPLAYSURF,(0,51,0),(a*100+50,b*100+50),30)

def displayscore():
    '''As the name suggests, this function displays the score'''
    scoreb,scorew = counter(l)
    blackscore = myfont.render('   Black : '+str(scoreb), True, (0, 0, 0))
    DISPLAYSURF.blit(blackscore,(800,350))
    whitescore = myfont.render('   White : '+str(scorew), True, (255, 255, 255))
    DISPLAYSURF.blit(whitescore,(800,400))

def drawline():
    '''This function draws the lines diffrentiating the squares'''
    for i in range(9):
        pygame.draw.line(DISPLAYSURF,(0,0,0),(100*i,0),(100*i,800),2)
        pygame.draw.line(DISPLAYSURF,(0,0,0),(0,100*i),(800,100*i),2)
def displayendmessage(gameender):
    '''This function is called after the game ends to display 1 out of the 5 pre determined game ending messages'''
    myfont2 = pygame.font.SysFont('Comic Sans MS', 25)
    if gameender == 0:
        return
    elif gameender==1:
        message = myfont2.render("  The computer",True,(0,0,0))
        DISPLAYSURF.blit(message,(800,500))
        message2 = myfont2.render("          wins!!!",True,(0,0,0))
        DISPLAYSURF.blit(message2,(800,540))
    elif gameender==2:
        message = myfont2.render(" Congratulations!!",True,(0,0,0))
        DISPLAYSURF.blit(message,(800,500))
        message2 = myfont2.render("        You win!!",True,(0,0,0))
        DISPLAYSURF.blit(message2,(800,540))
    elif gameender==3:
        message = myfont2.render(" The match ends",True,(0,0,0))
        DISPLAYSURF.blit(message,(800,500))
        message2 = myfont2.render("      as a draw!! ",True,(0,0,0))
        DISPLAYSURF.blit(message2,(800,540))
    elif gameender==4:
        message = myfont2.render(" Congratulations!!",True,(0,0,0))
        DISPLAYSURF.blit(message,(800,500))
        message2 = myfont2.render("      Black wins!!",True,(0,0,0))
        DISPLAYSURF.blit(message2,(800,540))
    elif gameender==5: 
        message = myfont2.render(" Congratulations!!",True,(0,0,0))
        DISPLAYSURF.blit(message,(800,500))
        message2 = myfont2.render("      White wins!!",True,(0,0,0))
        DISPLAYSURF.blit(message2,(800,540))
    #pygame.draw.rect(DISPLAYSURF,(0,128,0),pygame.Rect(800,100,80,200))
    pygame.draw.rect(DISPLAYSURF,(0,102,0),pygame.Rect(802,100,200,100)) 




done = False
count = 0
m = []
l = [["-" for x in range(8)] for y in range(8)] #Initialisation of the matrix
l[3][3],l[4][4],l[3][4],l[4][3],l[2][4],l[3][5],l[5][3],l[4][2]= "O","O","X","X","+","+","+","+"
d = 0
colour = True
games = menu()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
myfont2 = pygame.font.SysFont('Comic Sans MS', 30)
gamemode,difficulty = games
print gamemode,difficulty
gameender = 0
while not done: 
    mousex,mousey = pygame.mouse.get_pos()
    DISPLAYSURF.fill((0,102,0))
    drawback()
    drawline()
    drawgrid(l,mousex,mousey)
    displayscore()
    if gamemode ==0: #This displays whose turn it is in the 2 player mode
        if colour:
            mcolour = myfont.render(" White's turn",True,(255,255,255))
            DISPLAYSURF.blit(mcolour,(800,100))
            mcolour2 = myfont.render("     to play",True,(255,255,255))
            DISPLAYSURF.blit(mcolour2,(800,150))
        if not colour:
            mcolour = myfont.render(" Black's turn",True,(0,0,0))
            DISPLAYSURF.blit(mcolour,(800,100))
            mcolour2 = myfont.render("     to play",True,(0,0,0))
            DISPLAYSURF.blit(mcolour2,(800,150))

    displayendmessage(gameender)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            j,i = mousex/100,mousey/100
            m = run(l,i,j,count,colour,gamemode,difficulty)
            w = counter(l)
            if gamemode==1:
                if not m:
                    continue
                elif not m[0] or w[0]+w[1]==64 or w[0]==0 or w[1]==0: 
                    if w[0]>w[1] or w[1]==0:
                        gameender = 1
                    elif w[0]<w[1] or w[0]==0:
                        gameender = 2
                    else:
                        gameender = 3
                elif not m[4]:
                    gameender = 3
                else: 
                    scoreb,scorew,l,breakcount,boolean = m
                    if boolean: pass
                    else: continue

            elif gamemode==0:
                if not m:
                    continue
                elif not m[0]: 
                    if w[0]>w[1] or w[1]==0:
                        gameender=4
                    elif w[0]<w[1] or w[0]==0:
                        gameender = 5
                    else:
                        gameender = 3
                elif not m[4]:
                    gameender = 3
                else: 
                    scoreb,scorew,l,breakcount,boolean = m
                    colour = not colour
                    if boolean: pass
                    else: continue

    pygame.display.update()
    

    

    
