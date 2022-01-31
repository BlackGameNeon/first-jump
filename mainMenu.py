#importing libs
from libs import *
from win import *


#BG image
MAIN_MENU_BG_IMAGE = pygame.image.load(os.path.join('Assets', 'main_menu_bg_image.png'))
MAIN_MENU_BG_IMAGE_SCALE = pygame.transform.scale(MAIN_MENU_BG_IMAGE, (800, 600))

#MouseClicked = False
def mainMenuScreen():  
    SCREEN.blit(MAIN_MENU_BG_IMAGE_SCALE, (0, 0))

    #Main menu buttons
    PLAY_BUTTON = pygame.Rect(WIDTH/2 - 100, HEIGHT/2, 200, 50)

    #if PLAY_BUTTON.collidepoint((mouse_x, mouse_y)):
        #if mouseClicked:
            #print("Hola")
            
    pygame.draw.rect(SCREEN, (255, 0, 0), PLAY_BUTTON)
    
    pygame.display.update()