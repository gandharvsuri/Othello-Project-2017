import pygame,sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Othello")
pygame.draw.rect(DISPLAYSURF,(0,0,0),(0,0,100,100))
gamemode = 0

def drawgrid(l):
    for i in range(8):
        for j in range(8):
            if l[i][j]=="O":
                #print "Entered"
                #pygame.draw.rect(DISPLAYSURF,(0,0,0),(0,0,100,100))
                pygame.draw.circle(DISPLAYSURF,(255,255,255),(j*100+50,i*100+50),30)
                pygame.display.update()
            elif l[i][j]=="X":
                pygame.draw.circle(DISPLAYSURF,(0,0,0),(j*100+50,i*100+50),30)
                pygame.display.update()
    pygame.display.update()

