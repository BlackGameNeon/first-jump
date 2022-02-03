#First, importing pygame library. Then, upcoming libs
from tkinter import font
import pygame
pygame.init()

#OS, to access files
import os

#Constants of the Window's size
WIN_SIZE = WIDTH, HEIGHT = 800, 600
#Inizializing the Window
SCREEN = pygame.display.set_mode(WIN_SIZE)
#Captions of the scenes of the Window. Defining a constant is not mandatory
SCREEN_CAPTION = pygame.display.set_caption("Code in one file")
SCREEN_CAPTION_MENU = "Main Menu"
SCREEN_CAPTION_SCENE1 = "Scene 1"
SCREEN_CAPTION_SCENE2 = "Scene 2"
SCREEN_CAPTION_SCENE3 = "Scene 3"
SCREEN_BACKGROUND_COLOR = (255, 255, 0)
#Defining the clock
SCREEN_CLOCK = pygame.time.Clock()
#Framerate
SCREEN_FPS = 60

#Fonts used in the Window
FONT_PLAYER1 = pygame.font.SysFont("comicsans", 20)
FONT_PLAYER2 = pygame.font.SysFont("arial", 12)

#Initializing sound

#Background image. First load image to a constant, the another constant for it's scale
GAME_BG_IMAGE_IMPORT = pygame.image.load(os.path.join('Assets', 'game1.png'))
GAME_BG_IMAGE_SCALE = pygame.transform.scale(GAME_BG_IMAGE_IMPORT, (800, 600))
GAME_BG_IMAGE = GAME_BG_IMAGE_SCALE

#Player 1 image, scale and velocity
PLAYER1_IMAGE_IMPORT = pygame.image.load(os.path.join('Assets', 'player.png'))
PLAYER1_IMAGE_SCALE = pygame.transform.scale(PLAYER1_IMAGE_IMPORT, (160, 160))
PLAYER1_IMAGE = PLAYER1_IMAGE_SCALE
PLAYER1_VEL = 3

#Player 2 image, scale and velocity
PLAYER2_IMAGE_IMPORT = pygame.image.load(os.path.join('Assets', 'enemy.png'))
PLAYER2_IMAGE_SCALE = pygame.transform.scale(PLAYER2_IMAGE_IMPORT, (120, 120))
PLAYER2_IMAGE = PLAYER2_IMAGE_SCALE
PLAYER2_VEL = 5

#Defining a Rect with player 1 properties
player1_PosX = 100
player1_PosY = 200
player1_WIDTH = 100
player1_HEIGHT = 100
player1 = pygame.Rect(player1_PosX, player1_PosY, player1_WIDTH, player1_HEIGHT)

#Defining a Rect with player 2 properties
player2_PosX = 200
player2_PosY = 200
player2_WIDTH = 100
player2_HEIGHT = 100
player2 = pygame.Rect(player2_PosX, player2_PosY, player2_WIDTH, player2_HEIGHT)

def drawWindow1():
    SCREEN.blit(GAME_BG_IMAGE, (0, 0))
    SCREEN.blit(PLAYER1_IMAGE, (player1.x, player1.y))
    SCREEN.blit(PLAYER2_IMAGE, (player2.x, player2.y))

    #Draws the Window with the blits written so far
    #Because it is called from a loop, it will continue draw
    pygame.display.update()

def drawWindow2():
    SCREEN.blit(GAME_BG_IMAGE, (0, 0))
    SCREEN.blit(PLAYER2_IMAGE, (player2.x, player2.y))

    #Draws the Window with the blits written so far
    #Because it is called from a loop, it will continue draw
    pygame.display.update()

def window_handle(key_pressed, screen_current):
    if key_pressed[pygame.K_1]:
        screen_current = 1
        print(screen_current)
    if key_pressed[pygame.K_2]:
        screen_current = 2
        print(screen_current)
    if key_pressed[pygame.K_3]:
        screen_current = 3
        print(screen_current)

#Both player's handle are called from inside the While
#Player 1 handling movements
def player1_handle_movement(key_pressed):
    if key_pressed[pygame.K_w]:
        print("W")
        player1.y -= PLAYER1_VEL
    if key_pressed[pygame.K_s]:
        print("S")
        player1.y += PLAYER1_VEL
    if key_pressed[pygame.K_d]:
        print("b")
        player1.x += PLAYER1_VEL
    if key_pressed[pygame.K_a]:
        print("a")
        player1.x -= PLAYER1_VEL

#Player 2 handling movements
def player2_handle_movement(key_pressed):
    if key_pressed[pygame.K_UP]:
        print("W")
        player2.y -= PLAYER1_VEL
    if key_pressed[pygame.K_DOWN]:
        print("S")
        player2.y += PLAYER1_VEL
    if key_pressed[pygame.K_RIGHT]:
        print("b")
        player2.x += PLAYER1_VEL
    if key_pressed[pygame.K_LEFT]:
        print("a")
        player2.x -= PLAYER1_VEL

def main():
    screen_running = True
    screen_current = 1

    while screen_running:
        SCREEN_CLOCK.tick(SCREEN_FPS)

        drawWindow1()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_running = False
                pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                drawWindow1()
            if event.key == pygame.K_2:
                drawWindow2()
            if event.key == pygame.K_3:
                screen_current = 3
                print(screen_current)

        #drawWindow is called inside While to have called images and update() every FPS
        
        
        #key_pressed saves the actual key pressed every FPS
        key_pressed = pygame.key.get_pressed()

        #key_pressed is sent to both player's moving handle
        player1_handle_movement(key_pressed)
        player2_handle_movement(key_pressed)

        #window_handle(key_pressed, screen_current)
        print(screen_current)

    
def game():
    character = pygame.Rect(30, 450, 160, 160)
    mainDoor = pygame.Rect(400, 800, 130, 120)

    gameRunning = True
    while gameRunning:
        SCREEN_CLOCK.tick(SCREEN_FPS)

        SCREEN.blit(PLAYER_IMAGE_SCALE, (character.x, character.y))

        SCREEN.blit(ENEMY_IMAGE_SCALE, (530, 490))
        SCREEN.blit(ENEMY_IMAGE_SCALE, (210, 490))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        keypressed = pygame.key.get_pressed()
        char_handle_movement(keypressed, character)



        pygame.display.update()

if __name__ == "__main__":
    #__name__ of the file and __main__ is the main file that was run
    #This means main() will be excecuted when running this file
    main()
