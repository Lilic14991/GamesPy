import pygame, sys
from pygame import *
import time

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400,300))
pygame.display.set_caption('Hello World!')

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,255)

# Create a pygame.font.Font object.
fontObj = pygame.font.Font('freesansbold.ttf',50)
# Create a Surface object with the text drawn on it by calling the Font object’s render() method
textSurfaceObj = fontObj.render('Hello world!', True, GREEN, BLUE)
# Create a Rect object from the Surface object by calling the Surface object’s get_rect() method.
# This Rect object will have the width and height correctly set for the text that was rendered,
# but the top and left attributes will be 0.
textRectObj = textSurfaceObj.get_rect()
# Set the position of the Rect object by changing one of its attributes.
textRectObj.center = (200,150)
#======================================================================================================
# Sound
soundObj = pygame.mixer.Sound('bip.wav')
soundObj.play()
time.sleep(1) # wait and let the sound play for 1 second
soundObj.stop()
# load background music
pygame.mixer.music.load('EpicOrchestral.mp3')
pygame.mixer.music.play(-1,00)
pygame.mixer.music.stop()

while True:
    DISPLAYSURF.fill(WHITE)
#   Blit the Surface object with the text onto the Surface object returned by pygame.display.set_mode()   
    DISPLAYSURF.blit(textSurfaceObj,textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
