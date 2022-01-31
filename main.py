#importing files
import pygame
pygame.init()
#os to access files
import os

from mainMenu import *
from win import *
#Importing init functions from file

#Function wrap game's inits
#def gameInit():
#    winFontInit()
#    winMixerInit()
#gameInit()
winMixerInit()

#First window to appear when game starts
#mainMenu()
#BG image
GAME_BG_IMAGE = pygame.image.load(os.path.join('Assets', 'game1.png'))
GAME_BG_IMAGE_SCALE = pygame.transform.scale(GAME_BG_IMAGE, (800, 600))

PLAYER_IMAGE = pygame.image.load(os.path.join('Assets', 'player.png'))
PLAYER_IMAGE_SCALE = pygame.transform.scale(PLAYER_IMAGE, (160, 160))
VEL = 3

ENEMY_IMAGE = pygame.image.load(os.path.join('Assets', 'enemy.png'))
ENEMY_IMAGE_SCALE = pygame.transform.scale(ENEMY_IMAGE, (120, 120))

def main():
    mainMenuScreen()
    mainEvents()

            #if event.type == pygame.MOUSEBUTTONDOWN:
                    #if event.button:
                        #mouseClicked = True
                        #print("Hola")        

        #if PLAY_BUTTON.collidepoint((mouse_x, mouse_y)):
            #if mouseClicked:
              #game()

        #mouseClicked = False   

#Podría ir en win.py  
def mainEvents():
    while 1:
        
        mainClock.tick(SCREEN_FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #gameRunning = False
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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
