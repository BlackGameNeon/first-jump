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

screen_running = True

def fontsInit():
    #Fonts used in the Window
    FONT_PLAYER1 = pygame.font.SysFont("comicsans", 20)
    FONT_PLAYER2 = pygame.font.SysFont("arial", 12)

#Initializing sound

def imagesInit():
    #Background image. First load image to a constant, the another constant for it's scale
    GAME_BG_IMAGE = pygame.image.load(os.path.join('Assets', 'game1.png'))
    GAME_BG_IMAGE_SCALE = pygame.transform.scale(GAME_BG_IMAGE, (800, 600))

    PLAYER1_IMAGE = pygame.image.load(os.path.join('Assets', 'player.png'))
    #PLAYER1_IMAGE_SCALE = pygame.transform.scale(PLAYER_IMAGE, (160, 160))
    PLAYER1_VEL = 3

    PLAYER2_IMAGE = pygame.image.load(os.path.join('Assets', 'enemy.png'))
    #PLAYER2_IMAGE_SCALE = pygame.transform.scale(ENEMY_IMAGE, (120, 120))
    PLAYER2_VEL = 5

def gameInit():
    fontsInit()
    imagesInit()

def player1():
    player1_PosX = 100
    player1_PosY = 200
    player1_WIDTH = 100
    player1_HEIGHT = 100
    player1 = pygame.rect(player1_PosX, player1_PosY, player1_WIDTH, player1_HEIGHT)

def player2():
    player2_PosX = 200
    player2_PosY = 200

def main():
    gameInit()

    screen_running = True
    while screen_running:
        SCREEN_CLOCK.tick(SCREEN_FPS)
        print("Bien")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_running = False
                pygame.quit()
                
    

def char_handle_movement(keypressed, character):
    if keypressed[pygame.K_a]:
        character.x -= VEL
    if keypressed[pygame.K_d]:
        character.x += VEL

def game():
    character = pygame.Rect(30, 450, 160, 160)
    mainDoor = pygame.Rect(400, 800, 130, 120)

    gameRunning = True
    while gameRunning:
        mainClock.tick(SCREEN_FPS)

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
