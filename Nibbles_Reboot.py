import pygame
import sys
import random
import time

pygame.init()
pygame.font.init()
screansize = (500,500)
win = pygame.display.set_mode(screansize)
pygame.display.set_caption("Nibbles Reboot")
x = 250
y = 250
width = 20
height = 20
vel = 5
score = 0
gruning = True
faceing = 0
nibbleX = 0
nibbleY = 0
snakeL = 3
snakePX = [250,250,250,250]
snakePY = [250,250,250,250]
gamestate = 1
score_text = "score ="
nibble_Active = False



def RenderText(text,x,y,TXTcolor=(255,255,255),size=30,):

    myfont = pygame.font.SysFont('Arial MT', size)
    textsurface = myfont.render(text, True, (TXTcolor))
    win.blit(textsurface,(x,y))

def tale():
    for x in range(len(snakePX)):
        pygame.draw.rect(win,(255,255,0), (snakePX[x], snakePY[x], width, height))
    if snakeL <= len(snakePX):
        snakePX.pop()
        snakePY.pop()

    

while gruning:
    keys = pygame.key.get_pressed()  
    pygame.time.delay(100)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gruning = False
            
    win.fill((0,0,0))
    if  gamestate == 1:
        RenderText("Nibbles",100,100,(255,255,255),80)
        RenderText("Press any key to start",100,200,(255,255,255),30)
        pressed = keys
        event = pygame.event.wait()

        if (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONDOWN):
            gamestate = 2

    elif gamestate == 2:
        win.fill((25,25,255))

        if snakePX[0] == 470:
            gamestate = 3
        elif snakePY[0] == 470:
            gamestate = 3
        elif snakePX[0] == 10:
            gamestate = 3
        elif snakePY[0] == 10:
            gamestate = 3

        if keys [pygame.K_LEFT]and not faceing == 2:
            faceing = 1
        elif keys [pygame.K_RIGHT] and not faceing == 1:
            faceing = 2
        elif keys [pygame.K_UP] and not faceing == 4:
            faceing = 3           
        elif keys [pygame.K_DOWN] and not faceing == 3:
            faceing = 4

        if faceing == 1:
            snakePX.insert(0,x - vel)
            snakePY.insert(0,y)
            x -= vel
        elif faceing == 2:
            snakePX.insert(0,x + vel)
            snakePY.insert(0,y)
            x += vel
        elif faceing == 3:
            snakePX.insert(0,x)
            snakePY.insert(0,y - vel)
            y -= vel
        elif faceing == 4:
            snakePX.insert(0,x)
            snakePY.insert(0,y + vel)
            y += vel
    
        tale()

        pygame.draw.rect(win,(255,128,0), (0, 0, 500, 10))
        pygame.draw.rect(win,(255,128, 0), (0, 490, 500, 10))
        pygame.draw.rect(win,(255,128, 0), (0, 0, 10, 500))
        pygame.draw.rect(win,(255,128, 0), (490, 0, 10, 500))
        
        if nibble_Active == True:
            pygame.draw.rect(win,(255, 255, 255), (nibbleX, nibbleY , width, height))
            if x <=  nibbleX and x >=  (nibbleX - 20) and y <= nibbleY  and y >= (nibbleY - 20):
                snakeL = snakeL + 1
                vel = vel + 1
                score = score + 1
                nibble_Active = False

        else:
            nibbleX = random.randrange(10, 470, 1)
            nibbleY = random.randrange(10, 470, 1)
            nibble_Active = True

        pygame.draw.rect(win,(0, 0, 0), (0, 0, 90, 30))
        score_text = "score = " + str(score)
        RenderText(score_text,0,0)

    elif gamestate == 3:

        win.fill((0,0,0))
        score_text = " your final score is = " + str(score)
        RenderText("Game Over",100,100,(255,255,255),80)
        RenderText(score_text,100,150,(255,255,255),30)
        RenderText("Press any key to try again",100,200,(255,255,255),30)
        pygame.display.update()
        event = pygame.event.wait()

        if (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONDOWN):
            nibble_Active = False
            x = 250
            y = 250
            faceing = 0
            nibbleX = 0
            nibbleY = 0
            snakeL = 3
            snakePX = [250,250,250,250]
            snakePY = [250,250,250,250]
            score = 0
            gamestate = 2

    pygame.display.update() 
pygame.quit()

