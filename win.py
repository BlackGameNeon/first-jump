#from libs import *

import pygame
pygame.init()
#os to access files
import os

#Constants of the window's size
WIN_SIZE = WIDTH, HEIGHT = 800, 600
#Inizializing the Window
SCREEN = pygame.display.set_mode(WIN_SIZE)

#Caption of the window
#SCREEN_CAPTION = pygame.display.set_caption("The Art of War")
SCREEN_BACKGROUND_COLOR = (255, 255, 0)
SCREEN_FPS = 60

mainClock = pygame.time.Clock()

mouse_x, mouse_y = 0, 0

def winFontInit():
    pygame.font.init()

def winMixerInit():
    pygame.mixer.init()

def mouseInit():
    #Mouse actual position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    return mouse_x, mouse_y

