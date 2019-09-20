import pygame
import time
from random import *

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
crimson =(192, 57, 43)
purp =(155, 89, 182)
blue =(52, 152, 219 )
green =(46, 204, 113)
orange =(230, 126, 34 )
mint = (26, 188, 156)
colors =[crimson,purp,blue,green,orange,mint,white]
floor = 500
imageHeight = 35
imageWidth = 25
playWidth = 700
playHeight = 500
playCenter = ((playWidth / 2) , (playHeight/ 2))

pygame.init()
screen = pygame.display.set_mode((playWidth , playHeight))
pygame.display.set_caption('UFO')
clock = pygame.time.Clock()

def splash():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                intro = False

            screen.fill(white)
            msgUser("UFO")
            pygame.display.update()
 #creates my player obj 
def ufo (x, y, image):                                                    
    screen.blit(image, (x , y))
    image = pygame.image.load('ufo.png')
    
#block summmoning code
def blocks(x_block,y_block, block_width, block_height, gap, color):                 
    pygame.draw.rect(screen, color, [x_block,y_block, block_width, block_height])
    pygame.draw.rect(screen, color, [x_block, y_block+block_height+gap, block_width, playHeight])

def gameOver ():
    msgUser('¡Game Over!')
    
 #score text
def score(count):                                                      
    font = pygame.font.Font('freesansbold.ttf',20)
    text = font.render("Score: " + str(count), True, red)
    screen.blit(text,[0,0])

#restart ability
def replay():                                                            
    for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT, pygame.KEYUP]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            continue
        return event.key
    return None

def textObj(text, font):
    textUser = font.render(text, True, red)
    return textUser, textUser.get_rect()

def msgUser (text):
    optText = pygame.font.Font('freesansbold.ttf' , 30)
    mainText = pygame.font.Font('freesansbold.ttf', 110)
 #GAME OVER text position
    titleText,titlePos =  textObj(text, mainText)          
    titlePos.center = playCenter
    screen.blit(titleText,titlePos)
#restart text position
    typText, typPos = textObj('Press any key', optText)     
    typPos.center = playWidth / 2, ((playHeight / 2 + 100))
    screen.blit(typText, typPos)

    pygame.display.update()
    time.sleep(1)
#restart wait screen
    while replay() == None:                                 
        clock.tick()
    main()

def main():
    x = 100
    y = 200
    y_speed = 0

    x_block = playWidth
    y_block =0
    block_width = 75
    block_height = randint (0,(playWidth/2))
    block_speed = 4
    gap = imageHeight * 3.2
    player_score = 0
 #changes color of blocks randomly    
    blockColor= colors[randrange(0,len(colors))]           

    game_over = False
    while not game_over:
#gg; game over function
        for event in pygame.event.get():                    
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYUP:                  #auto y- while not going up
                 if event.key == pygame.K_UP:
                    y_speed = 7
            if event.type == pygame.KEYDOWN:                #up to go up; y+
                if event.key == pygame.K_UP:
                    y_speed = -4
        y += y_speed

        screen.fill(black)      #background/load queue
        ufo(x,y,image=pygame.image.load('ufo.png'))
        blocks(x_block, y_block, block_width, block_height, gap, blockColor)
        score(player_score)
        x_block -= block_speed

        if y > floor - 35 or y < 0:                         #screen edge collision detection; game over
            gameOver()
        if x_block < (-1*block_width):                      #when the block is off screen
            x_block = playWidth                             #summon block
            block_height = randint(0, (playHeight/2))       #blockheight
            blockColor = colors[randrange(0, len(colors))]  #changes block color
            player_score += 1                               #Score logic
        if x + imageWidth > x_block:
            if x < x_block + block_width:                   #within boundaries of x
                #print('passing through gap')
                if y < block_height:
                    #print('y crossover upper')
                    if x - imageWidth < block_width+x_block:    #upper boundary collision
                        #print('game over hit upper')
                        gameOver()
        if x + imageWidth > x_block:
           # print('image crossover')
            if y + imageHeight > block_height + gap:
               # print('y crossover lower')
                if x < block_width + x_block:                   #lower boundary collision
                  # print('game over hit upper lower')
                    gameOver()
        if x_block < (x-block_width)<x_block+block_speed:
            if 2 <= player_score < 4:                           #difficulty increase with score
                block_speed = 7
                gap = imageHeight * 2.7
            if 4 <= player_score < 6:
                block_speed = 10
                gap = imageHeight * 2.4
            if 6 <= player_score < 8:
                block_speed = 11.5
                gap = imageHeight * 2.3
            if 8 <= player_score < 10:
                block_speed = 13
                gap = imageHeight * 2.2
        pygame.display.update()
        clock.tick(60)
splash()
main()
pygame.quit()
quit()

