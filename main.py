import pygame
import os
img_path = os.path.join('./player.png')
from cube import cub
import random
#open a window with a 720x480 resolution and keep the screen open
pygame.init()
screen = pygame.display.set_mode((720,480))
pygame.display.set_caption("JitterCube")
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

running = True
while running:
    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    cube.handle_keys()
    cube.draw(screen)
    if cube.timehasntmoved>3000:
        cube.timehasntmoved=3000

    pygame.display.update()

