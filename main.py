import pygame

#open a window with a 720x480 resolution and keep the screen open
pygame.init()
while True:
    screen = pygame.display.set_mode((720,480))
    pygame.display.set_caption("JitterCube")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
