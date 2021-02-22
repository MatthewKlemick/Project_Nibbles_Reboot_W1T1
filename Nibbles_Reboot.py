import pygame
import sys
import random
import time
#seting up all of the global varibles
pygame.init()
pygame.font.init()
screanhight = 500
screanwith = 500
screansize = (screanwith,screanhight)
win = pygame.display.set_mode(screansize)
pygame.display.set_caption("Nibbles Reboot")
game_over = pygame.mixer.Sound("game_over.wav")
game_start = pygame.mixer.Sound("game_start.wav")
intro_music = pygame.mixer.Sound("intro_music.wav")
pickup_nibble = pygame.mixer.Sound("pickup_nibble.wav")
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
introM = False
fxplaying = False
fxplaying2 = False
pygame.mixer.Channel(1)
pygame.mixer.Channel(2)
#(255,255,0)

# Function to make text appare on in the display
def RenderText(text,x,y,TXTcolor=(255,255,255),size=30,):

    myfont = pygame.font.SysFont('Arial MT', size)
    textsurface = myfont.render(text, True, (TXTcolor))
    win.blit(textsurface,(x,y))
# Function to render the snakes tale
def tale():
    for x in range(len(snakePX)):
        snake = pygame.draw.rect(win,(255,255,0), (snakePX[x], snakePY[x], width, height))
        
    if snakeL <= len(snakePX):
        snakePX.pop()
        snakePY.pop()
# a Function use to come up with random cords
def r(screanh,screanw):
    x2 = random.randrange(10, screanw - 30, 10)
    y2 = random.randrange(10, screanh - 30, 10)
    return  x2 , y2

def test_r():
    E , Q =  r(500,500)   
    assert type(E) == int and type(Q) == int ,"Test faied the random numbers are not ints"
    assert E < 470 and Q < 470,"Test faied the random numbers were to high"
    assert E > 10 and Q > 10,"Test faied the random numbers were to low"

while gruning:
    keys = pygame.key.get_pressed()  
    pygame.time.delay(100)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gruning = False

    win.fill((0,0,0))
    # displays the menu when first started up 
    if  gamestate == 1:
        RenderText("Nibbles",100,50,(255,255,255),80)
        win.blit(nibbles_image, (100,150))
        RenderText("Press any key to start",100,100,(255,255,255),30)
        pressed = keys
        if introM == False:
            pygame.mixer.Channel(1).play(intro_music, 0, -1,50)
            introM = True
            
        event = pygame.event.wait()
        # starts up game when any key is pressed
        if (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONDOWN):
            pygame.mixer.Channel(1).fadeout(300)
            gamestate = 2
            introM = False
   
    elif gamestate == 2:
        win.fill((25,25,255))
        if fxplaying == False:
            pygame.mixer.Channel(2).play(game_start, 0, -1,0)
            fxplaying = True
        
        

        # movement is handed here
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

        # enforces the boundary
        if snakePX[0] > 470 :
            fxplaying, fxplaying2 = False ,False
            gamestate = 3
        elif snakePY[0] > 470:
            fxplaying, fxplaying2 = False ,False
            gamestate = 3
        elif snakePX[0] < 10:
            fxplaying, fxplaying2 = False ,False
            gamestate = 3
        elif snakePY[0] < 10:
            fxplaying, fxplaying2 = False ,False
            gamestate = 3

        
         
        pygame.draw.rect(win,(255,128,0), (0, 0, 500, 10))
        pygame.draw.rect(win,(255,128, 0), (0, 490, 500, 10))
        pygame.draw.rect(win,(255,128, 0), (0, 0, 10, 500))
        pygame.draw.rect(win,(255,128, 0), (490, 0, 10, 500))

        #sets up  a nibble at random cords once and handels snake length , spead and score

        if nibble_Active == True:
            pygame.draw.rect(win,(255, 255, 255), (nibbleX, nibbleY , width, height))
            if abs(snakePX[0] - nibbleX) <= 20  and abs(snakePY[0] - nibbleY) <= 20:
                
                snakeL = snakeL + 1
                vel = vel + 1
                score = score + 1
                nibble_Active = False
                
                pygame.mixer.Channel(2).play(pickup_nibble, 0, -1,0)
                 
        else:
            nibbleX , nibbleY = r(screanwith,screanhight)
            nibble_Active = True

        pygame.draw.rect(win,(0, 0, 0), (0, 0, 100, 30))
        score_text = "score = " + str(score)
        RenderText(score_text,0,0)

        #sets up 3 obstacles at random cords once the score reaches 5 
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
        if fxplaying2 == False:
            pygame.mixer.Channel(2).play(game_over, 0, -1,0)
            fxplaying2 = True

        win.fill((0,0,0))
        score_text = " your final score is = " + str(score)
        RenderText("Game Over",100,100,(255,0,0),80)
        RenderText(score_text,100,150,(255,255,255),30)
        RenderText("Press any key to try again",100,200,(255,255,255),30)
        pygame.display.update()
        event = pygame.event.wait()
        # starts up game when any key is pressed
        if (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONDOWN):
            nibble_Active = False
            objs = False
            objX = [0]
            objY = [0]
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
            fxplaying = False
            fxplaying2 = True
            gamestate = 2
    #updates the display with changes
    pygame.display.update() 
# allows pygame to stop when you X out of the window
pygame.quit()

