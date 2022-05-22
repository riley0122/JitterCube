from re import X
from tabnanny import verbose
import pygame
import os
import json
img_path = os.path.join('./food.png')
logo_path= os.path.join('./logo.png')
from cube import cub
import random
import math
#open a window with a 720x480 resolution and keep the screen open
pygame.init()
screen = pygame.display.set_mode((720,480))
pygame.display.set_caption("JitterCube")
#set the icon to the logo
pygame.display.set_icon(pygame.image.load(logo_path))
#make the on the left side of the screen 67, 225, 240
screen.fill((67, 225, 240))
#make the on the right side of the screen the inverted color of the left side
screen.fill((255-67, 255-225, 255-240), (360, 0, 720, 480))
#draw cube
cube = cub((255,255,255), (100, 100), (360, 220))

class fud(pygame.sprite.Sprite):
    def __init__(self, coords):

        self.image = pygame.image.load(img_path)

        #give the image a red hue
        self.image.set_colorkey((255,255,255))

        self.x = coords[0]-5
        self.y = coords[1]-5

food = fud((random.randrange(10,710), random.randrange(10,470)))
fx=random.randrange(10,470)
fy=random.randrange(10,470)
screen.blit(food.image, (fx,fy))
running = True
score=0
#draw text in the bottom left corner
font = pygame.font.Font(None, 36)
text = font.render("Score: "+str(score), 1, (255,255,255))
screen.blit(text, (10, 450))
pygame.mixer.music.load("./song.wav")
pygame.mixer.music.play(-1)
filepath = os.path.dirname(os.path.abspath(__file__))
with open(filepath+'/optionsMenu/options.json', 'r') as f:
    options = json.loads(f.read())
    volume = options['volume']
pygame.mixer.music.set_volume(volume)

def foodCheckBeen(fx,fy):
    if cube.been.__contains__([fx, fy]) or cube.been.__contains__([fx-1, fy]) or cube.been.__contains__([fx+1, fy]) or cube.been.__contains__([fx, fy-1]) or cube.been.__contains__([fx, fy+1]):
        fx=random.randrange(10,470)
        fy=random.randrange(10,470)
        foodCheckBeen(fx,fy)
    elif cube.been.__contains__([fx, fy]) or cube.been.__contains__([fx-2, fy]) or cube.been.__contains__([fx+2, fy]) or cube.been.__contains__([fx, fy-2]) or cube.been.__contains__([fx, fy+2]):
        fx=random.randrange(10,470)
        fy=random.randrange(10,470)
        foodCheckBeen(fx,fy)
    elif cube.been.__contains__([fx, fy]) or cube.been.__contains__([fx-3, fy]) or cube.been.__contains__([fx+3, fy]) or cube.been.__contains__([fx, fy-3]) or cube.been.__contains__([fx, fy+3]):
        fx=random.randrange(10,470)
        fy=random.randrange(10,470)
        foodCheckBeen(fx,fy)
    elif cube.been.__contains__([fx, fy]) or cube.been.__contains__([fx-4, fy]) or cube.been.__contains__([fx+4, fy]) or cube.been.__contains__([fx, fy-4]) or cube.been.__contains__([fx, fy+4]):
        fx=random.randrange(10,470)
        fy=random.randrange(10,470)
        foodCheckBeen(fx,fy)
    elif cube.been.__contains__([fx, fy]) or cube.been.__contains__([fx-5, fy]) or cube.been.__contains__([fx+5, fy]) or cube.been.__contains__([fx, fy-5]) or cube.been.__contains__([fx, fy+5]):
        fx=random.randrange(10,470)
        fy=random.randrange(10,470)
        foodCheckBeen(fx,fy)
    else:
        return (fx,fy)

#main loop
while running:    
    #if the food is touching the cube, make it go to a new location
    if math.sqrt((fx-cube.px)**2 + (fy-cube.py)**2)<=10:
        fx=random.randrange(10,470)
        fy=random.randrange(10,470)
        screen.blit(food.image, foodCheckBeen(fx,fy))
        print(score)
        score+=1
        #draw a cube in the colour of the background over the text
        screen.fill((67, 225, 240), (10, 450, 100, 50))

        text = font.render("Score: "+str(score), 1, (255,255,255))
        screen.blit(text, (10, 450))
        pygame.mixer.Sound.play(pygame.mixer.Sound("./pickUp.wav"))
    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #close the window
            pygame.quit()
            #exit the program
            quit()
    
    cube.handle_keys()
    cube.draw(screen)
    if cube.timehasntmoved>3000:
        pygame.mixer.music.fadeout(300)
        pygame.mixer.Sound.play(pygame.mixer.Sound("./death.wav"))
        #get the number in highscore.csv
        with open('highscore.csv', 'r') as f:
            highscore = int(f.read())
            print('score'+str(score))
            print('highscore'+str(highscore))
        #if the score is greater than the highscore, write the score to highscore.csv
        if score>highscore:
            with open('highscore.csv', 'w') as f:
                f.write(str(score))
        running=False
        os.system('cmd /c "startded.bat"')
        #close the window
        pygame.quit()
        #exit the program
        quit()
        
    
    pygame.display.update()

