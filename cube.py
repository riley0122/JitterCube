from lib2to3.pgen2.grammar import opmap
import pygame
import os
import json
been=[]
filepath = os.path.dirname(os.path.realpath(__file__))
with open(filepath+'/optionsMenu/options.json', 'r') as f:
    options = json.loads(f.read())
    speed = options['speed']/4
img_path = os.path.join('./player.png')
class cub(pygame.sprite.Sprite):
    def __init__(self, colour, scaling, coords):

        self.image = pygame.image.load(img_path)

        self.x = coords[0]-5
        self.y = coords[1]-5

        self.timehasntmoved=0

        self.px=360
        self.py=220
        self.tmr=False
    
    def handle_keys(self):
        self.been = been
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.tmr=True
            if been.__contains__([self.x, self.y-5]) or self.y<0:
                pass
            else:
                self.timehasntmoved=0
                self.y -= speed
                self.py -= speed
                been.append([self.x, self.y])
        if key[pygame.K_DOWN]:
            self.tmr=True
            if been.__contains__([self.x, self.y+5]) or self.y>720:
                pass
            else:
                self.timehasntmoved=0
                self.y += speed
                self.py += speed
                been.append([self.x, self.y])
        if key[pygame.K_LEFT]:
            self.tmr=True
            if been.__contains__([self.x-5, self.y]) or self.x<0:
                pass
            else:
                self.timehasntmoved=0
                self.x -= speed
                self.px -= speed
                been.append([self.x, self.y])
        if key[pygame.K_RIGHT]:
            self.tmr=True
            if been.__contains__([self.x+5, self.y]) or self.x>720:
                pass
            else:    
                self.timehasntmoved=0
                self.x += speed
                self.px += speed
                been.append([self.x, self.y])
        
    def draw(self, screen):
        if self.tmr:
            self.timehasntmoved+=1
        #print(self.timehasntmoved)
        screen.blit(self.image, (self.x, self.y))
    