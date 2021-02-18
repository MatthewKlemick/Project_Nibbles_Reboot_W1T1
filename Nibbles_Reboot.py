import pygame
import sys
import random
import time

pygame.init()
pygame.font.init()
screanhight = 500
screanwith = 500
screansize = (screanwith,screanhight)
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
snakePX = [250]
snakePY = [250]
objX = [0]
objY = [0]
objx3 = 0
objy3 = 0
objs = False
gamestate = 1
score_text = "score ="
nibble_Active = False
nibbles_image = pygame.image.load('swerl.png')
#(255,255,0)

def RenderText(text,x,y,TXTcolor=(255,255,255),size=30,):

    myfont = pygame.font.SysFont('Arial MT', size)
    textsurface = myfont.render(text, True, (TXTcolor))
    win.blit(textsurface,(x,y))

def tale():
    for x in range(len(snakePX)):
        snake = pygame.draw.rect(win,(255,255,0), (snakePX[x], snakePY[x], width, height))
        
    if snakeL <= len(snakePX):
        snakePX.pop()
        snakePY.pop()

def r(screanh,screanw):
    x2 = random.randrange(10, screanw - 30, 10)
    y2 = random.randrange(10, screanh - 30, 10)
    return  x2 , y2

while gruning:
    keys = pygame.key.get_pressed()  
    pygame.time.delay(100)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gruning = False
            
    win.fill((0,0,0))
    if  gamestate == 1:
        RenderText("Nibbles",100,50,(255,255,255),80)
        win.blit(nibbles_image, (100,150))
        RenderText("Press any key to start",100,100,(255,255,255),30)
        pressed = keys

        

        if (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONDOWN):
            gamestate = 2

    elif gamestate == 2:
        win.fill((25,25,255))


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
            snakePX.insert(0,x + vel )
            snakePY.insert(0,y)
            x += vel
        elif faceing == 3:
            snakePX.insert(0,x)
            snakePY.insert(0,y - vel )
            y -= vel
        elif faceing == 4:
            snakePX.insert(0,x)
            snakePY.insert(0,y + vel )
            y += vel

        tale()

        
        if snakePX[0] > 470 :
            gamestate = 3
        elif snakePY[0] > 470:
            gamestate = 3
        elif snakePX[0] < 10:
            gamestate = 3
        elif snakePY[0] < 10:
            gamestate = 3

        pygame.draw.rect(win,(255,128,0), (0, 0, 500, 10))
        pygame.draw.rect(win,(255,128, 0), (0, 490, 500, 10))
        pygame.draw.rect(win,(255,128, 0), (0, 0, 10, 500))
        pygame.draw.rect(win,(255,128, 0), (490, 0, 10, 500))

        if nibble_Active == True:
            pygame.draw.rect(win,(255, 255, 255), (nibbleX, nibbleY , width, height))
            if abs(snakePX[0] - nibbleX) <= 20  and abs(snakePY[0] - nibbleY) <= 20:
                
                snakeL = snakeL + 1
                vel = vel + 1
                score = score + 1
                nibble_Active = False

        else:
            nibbleX , nibbleY = r(screanwith,screanhight)
            nibble_Active = True

        pygame.draw.rect(win,(0, 0, 0), (0, 0, 90, 30))
        score_text = "score = " + str(score)
        RenderText(score_text,0,0)

        if len(objX) == 3:
            for v in range(len(objX)):
                pygame.draw.rect(win,(255,128,0), (objX[v], objY[v], width, height))
                if abs(snakePX[0] - objX[v]) <= 20  and abs(snakePY[0] - objY[v]) <= 20:
                  gamestate = 3  

        if score >= 5 and objs == False:
            objX.pop(0)
            objY.pop(0)
            objx3 , objy3 = r(screanwith,screanhight)
            objX.append(objx3)
            objY.append(objy3)
            objx3 , objy3 = r(screanwith,screanhight)
            objX.append(objx3)
            objY.append(objy3)
            objx3 , objy3 = r(screanwith,screanhight)
            objX.append(objx3)
            objY.append(objy3)
            objs = True

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
            objs = False
            objX = []
            objY = []
            x = 250
            y = 250
            vel = 5
            faceing = 0
            nibbleX = 0
            nibbleY = 0
            snakeL = 3
            snakePX = [250]
            snakePY = [250]
            score = 0
            gamestate = 2

    pygame.display.update() 
pygame.quit()

