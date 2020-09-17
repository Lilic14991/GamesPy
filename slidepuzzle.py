# Slide Puzzle

import pygame, sys, random
from pygame.locals import *

# Create constants 

BOARDWIDTH = 4 # number of columns in the board
BOARDHEIGHT = 4 # number of rows in the board
TILESIZE = 80 
WINDOWWIDTH = 640
WINDOWHIGHT = 480
FPS = 30
BLANK = None

#          R    G    B
BLACK =   (  0,  0,  0)
WHITE =   (255,255,255)
BRIGHTBLUE = (0,50,255)
DARKTURQUOiSE = (3,54,73)
RED   =   (255,  0,  0)
GREEN =   (  0,204,  0)
BLUE  =   (  0,  0,255)

BGCOLOR = DARKTURQUOiSE
TILECOLOR = GREEN
TEXTCOLOR = WHITE
BORDERCOLOR = BRIGHTBLUE
BASICFONTSIZE = 20

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MESSAGECOLOR = WHITE

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1)))/2)
YMARGIN = int((WINDOWHIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1)))/2)

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, RESET_SURF, RESET_RECT, NEW_SURF, NEW_RECT, SOLVE_SURF, SOLVE_RECT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode( (WINDOWWIDTH,WINDOWHIGHT) )
    pygame.display.set_caption('Slide Puzzle')
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    # Store the option buttons and their rectangles in OPTIONS:
    RESET_SURF,RESET_RECT = makeText('Reset', TEXTCOLOR, TILECOLOR, WINDOWWIDTH-120,WINDOWHIGHT-90)
    NEW_SURF,NEW_RECT = makeText('New Game', TEXTCOLOR, TILECOLOR, WINDOWWIDTH-120,WINDOWHIGHT-60) 

    SOLVE_SURF,SOLVE_RECT = makeText('Solve', TEXTCOLOR,TILECOLOR, WINDOWWIDTH-120,WINDOWHIGHT-30)

    mainBoard, solutionSeq = generateNewPuzzle(80)
    SOLVEDBOARD = getStartingBoard() # a solved board is the same as the board in a start state
    allMoves = [] # list of moves made from the solved configuration

    while True: # main game loop
        slideTo = None # the direction, if any, a tile should slide
        msg = '' # contains the message to show in the upper left corner.
        if mainBoard == SOLVEDBOARD:
            msg = 'Solved!'
        
        drawBoard(mainBoard,msg)

        checkForQuit()
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEBUTTONUP: 
                spotx, spoty = getSpotClicked(mainBoard, event.pos[0], event.pos[1])

                if (spotx,spoty) == (None,None):
                    # check if the user clicked on an option button
                    if RESET_RECT.collidepoint(event.pos):
                        resetAnimation(mainBoard,allMoves) # clicked on Reset button


