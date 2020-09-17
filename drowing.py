import pygame,sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Drawing')

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SILVER = (192,192,192)

# The fill() method is not a function but a method of pygame.Surface objects.
# It will completely fill in the entire 
# Surface object with whatever color value you pass as for the color parameter.
screen.fill(WHITE)
# crtanje polygon-a
#  pygame.draw.polygon(surface, color, pointlist, width) 
pygame.draw.polygon(screen,GREEN,((146,0),(291,106),(236,277),(56,277),(0,106)))
# crtanje linije
# pygame.draw.line(surface, color, start_point, end_point, width)
pygame.draw.line(screen,BLUE,(60,60),(120,60),4)
pygame.draw.line(screen,SILVER,(120,60),(60,120))
pygame.draw.line(screen,BLUE,(60,120),(120,120),4)
# crtanje circle
# pygame.draw.circle(surface, color, center_point, radius, width)
# pygame.draw.lines(surface, color, closed, pointlist, width)
pygame.draw.circle(screen,BLUE,(300,50),50,0)
pygame.draw.circle(screen,BLUE,(400,50),20,0)
pygame.draw.circle(screen,BLUE,(450,50),20,0)
# crtanje ellipse
pygame.draw.ellipse(screen,RED,(300,250,40,89),3)
# crtanje rectangle-a
pygame.draw.rect(screen,RED,(200,150,100,50),0)

pixObj = pygame.PixelArray(screen)
pixObj[480][380] = BLACK
pixObj[482][382] = WHITE
pixObj[484][384] = BLACK
pixObj[486][386] = GREEN
pixObj[488][388] = BLACK
del pixObj









while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()