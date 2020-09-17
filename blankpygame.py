import pygame, sys
from pygame.locals import *

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BlUE = (0,0 255)


width = 1000
height = 800

pygame.init()
DISPLAYSUFR = pygame.display.set_mode((width, height))
pygame.display.set_caption('Hello World!')

# main game loop

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()