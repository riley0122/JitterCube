import pygame
import os
been=[]
img_path = os.path.join('./player.png')
class cub(pygame.sprite.Sprite):
    def __init__(self, colour, scaling, coords):

        self.image = pygame.image.load(img_path)

        self.x = coords[0]-5
        self.y = coords[1]-5

        self.timehasntmoved=0
    
    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            if been.__contains__([self.x, self.y-5]):
                pass
            else:
                self.timehasntmoved=0
                self.y -= 1
                been.append([self.x, self.y])
        if key[pygame.K_DOWN]:
            if been.__contains__([self.x, self.y+5]):
                pass
            else:
                self.timehasntmoved=0
                self.y += 1
                been.append([self.x, self.y])
        if key[pygame.K_LEFT]:
            if been.__contains__([self.x-5, self.y]):
                pass
            else:
                self.timehasntmoved=0
                self.x -= 1
                been.append([self.x, self.y])
        if key[pygame.K_RIGHT]:
            if been.__contains__([self.x+5, self.y]):
                pass
            else:    
                self.timehasntmoved=0
                self.x += 1
                been.append([self.x, self.y])
        
    def draw(self, screen):
        self.timehasntmoved+=1
        #print(self.timehasntmoved)
        screen.blit(self.image, (self.x, self.y))
    