from fourlinefile import *
from othellofunction import *
from checkboxes import *

def drawback():
    for i in range(8):        
        for j in range(4):
            if i%2==1:
                k=i*100
                pygame.draw.rect(DISPLAYSURF,(0,128,0),pygame.Rect(k,100+j*200,100,100))  
            else:
                k=i*100
                pygame.draw.rect(DISPLAYSURF,(0,128,0),pygame.Rect(k,j*200,100,100)) 

def drawgrid(l,mousex,mousey):
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
    scoreb,scorew = counter(l)
    blackscore = myfont.render('   Score : '+str(scoreb), True, (0, 0, 0))
    DISPLAYSURF.blit(blackscore,(800,350))
    whitescore = myfont.render('   Score : '+str(scorew), True, (255, 255, 255))
    DISPLAYSURF.blit(whitescore,(800,400))

def displayendmessage(gameender):
    if gameender == 0:
        return
    elif gameender==1:
        message = myfont2.render("The computer",True,(0,128,0))
        DISPLAYSURF.blit(message,(800,500))
        message2 = myfont2.render("       wins!!!",True,(0,128,0))
        DISPLAYSURF.blit(message2,(800,540))
    elif gameender==2:
        message = myfont2.render("    Cngratulations!!",True,(0,128,0))
        DISPLAYSURF.blit(message,(800,500))
        message2 = myfont2.render("   You win!!",True,(0,128,0))
        DISPLAYSURF.blit(message2,(800,540))


done = False
count = 0
m = []
l = [["-" for x in range(8)] for y in range(8)] #Initialisation of the matrix
l[3][3],l[4][4],l[3][4],l[4][3],l[2][4],l[3][5],l[5][3],l[4][2]= "O","O","X","X","+","+","+","+"
d = 0
colour = True
games = menu()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 50)
myfont2 = pygame.font.SysFont('Comic Sans MS', 40)
gamemode,difficulty = games
gameender = 0
while not done:
    mousex,mousey = pygame.mouse.get_pos()
    DISPLAYSURF.fill((128,128,0))
    drawback()
    drawgrid(l,mousex,mousey)
    displayscore()
    if gamemode ==0:
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

        #time1 = time.time()+5
    for i in range(10**3):
        displayendmessage(gameender)
        #pygame.quit()
        #sys.exit()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            j,i = mousex/100,mousey/100
            m = run(l,i,j,count,colour,gamemode,difficulty)
            if gamemode==1:
                if not m:
                    continue
                elif not m[0]: 
                    if m[1]>m[2] or m[2]==0:
                        gameender=1
                    elif m[1]<m[2] or m[1]==0:
                        gameender = 2
                        print "Congratulations!! You beat the computer!",m[1],m[2]
                    else:
                        gameender = 3
                        print "Draw!!",m[1],m[2]
                elif not m[4]:
                    gameender = 3
                    print "Draw!!"
                else: 
                    scoreb,scorew,l,breakcount,boolean = m
                    if boolean: pass
                    else: continue

            elif gamemode==0:
                if not m:
                    continue
                elif not m[0]: 
                    if m[1]>m[2] or m[2]==0:
                        gameender=4
                        print "Black Wins!!"
                    elif m[1]<m[2] or m[1]==0:
                        gameender = 5
                        print "White wins!!",m[1],m[2]
                    else:
                        gameender = 3
                        print "Draw!!",m[1],m[2]
                elif not m[4]:
                    gameender = 3
                    print "Draw!!"
                else: 
                    scoreb,scorew,l,breakcount,boolean = m
                    colour = not colour
                    if boolean: pass
                    else: continue

    pygame.display.update()
    

    

    
