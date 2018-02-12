returnlist = [0]*2
def menu():
    from fourlinefile import *
    import time

    #importing images
    othello=pygame.image.load("othello.png")
    opponent=pygame.image.load("opponent.png")
    comp=pygame.image.load("comp.png")
    human=pygame.image.load("human.png")
    level=pygame.image.load("level.png")
    easy=pygame.image.load("easy.png")
    medium=pygame.image.load("medium.png")
    click=pygame.image.load("click.png")
    hard=pygame.image.load("hard.png")        

    menu=True
    l=True
    cpu=False
    #loop for the menu
    while menu:
            for event in pygame.event.get():
                    if event.type == QUIT:
                            pygame.quit()
                            sys.exit()

                    DISPLAYSURF.fill((0,0,0))
                    DISPLAYSURF.blit(othello,(175,50))
                    DISPLAYSURF.blit(click,(240,500))
                    if event.type==pygame.MOUSEBUTTONDOWN:
                            DISPLAYSURF.fill((0,0,0))
                            menu=False
            pygame.display.update()
    #loop for select your opponent
    while l:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            for event in pygame.event.get():
                    if event.type==QUIT:
                            pygame.quit()
                            sys.exit()
                    DISPLAYSURF.blit(opponent,(150,10))
                    DISPLAYSURF.blit(human,(300,400))
                    DISPLAYSURF.blit(comp,(300,550))
                    if 20<mouse_x<800 and 350<mouse_y<500:
                            if event.type==MOUSEBUTTONDOWN:
                                    DISPLAYSURF.fill((0,0,0))
                                    #append statement here
                                    returnlist[0] = 0
                                    l=False
                    if 20<mouse_x<770 and 550<mouse_y<700:
                            if event.type==MOUSEBUTTONDOWN:
                                    DISPLAYSURF.fill((0,0,0))
                                    cpu=True
                                    #append statement here
                                    returnlist[0] = 1
                                    l=False
		    

                                    
            pygame.display.update()

    #loop for select level of difficulty
    while cpu:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            for event in pygame.event.get():
                    if event.type==QUIT:
                            pygame.quit()
                            sys.exit()
                    DISPLAYSURF.blit(level,(175,50))
                    DISPLAYSURF.blit(easy,(330,400))
                    DISPLAYSURF.blit(medium,(340,550))
		    DISPLAYSURF.blit(hard,(385,700))
                    if 20<mouse_x<700  and 330<mouse_y<500:
                            if event.type==MOUSEBUTTONDOWN:
                                    returnlist[1] = 0
                                    #append for easy
                                    cpu= False
                    if 20<mouse_x<700  and 550<mouse_y<700:
                            if event.type==MOUSEBUTTONDOWN:
                                    returnlist[1] = 1
                                    #append for easy
                                    cpu=False
                    if 20<mouse_x<700  and 690<mouse_y<800:
                            if event.type==MOUSEBUTTONDOWN:
                                    returnlist[1] = 2
                                    #append for easy
                                    cpu=False

            pygame.display.update()
    return returnlist
