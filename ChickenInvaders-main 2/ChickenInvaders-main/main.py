
import pygame
from pygame import mixer
import config
from game import *
from plane import *
from chicken import *
from util import *




def main():
    """This function defines main menu.
    Parameter: none
    Return: none
    """
    pygame.init()
    screen= pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("Chicken Invader")
    # game variables
    menu_state="main"
    # define color

    # creat button instances
    blurred_bg=pygame.image.load(config.bg_blurred_img) 
    title_button= Button(240, 50, config.title_img,0.5)
    start_button= Button(310, 300, config.start_img,0.5)
    guide_button= Button(310, 350, config.guide_img,0.45)
    quit_button= Button(310, 400, config.quit_img,0.5) 
    arcade_button= Button(335, 330, config.arcade_img,0.5)
    xmas_button= Button(350, 400, config.xmas_img,0.5)
    run = True
    menu_music=music(config.menu_music,repeat=True)
    while run:
        screen.blit(blurred_bg,(0,0))
        title_button.draw(screen)
        if menu_state=="main":
            if start_button.draw(screen):
                menu_state="start"
            if guide_button.draw(screen):
                menu_state="guide"
            if quit_button.draw(screen):
                run= False
        if menu_state== "start":
            back_button= Button(50, 450, config.back_img,0.5) 
            if back_button.draw(screen):
                menu_state="main"
            if arcade_button.draw(screen):
                menu_music.stop()
                config.THEME='arcade'
                Game(screen)
                menu_state="main"
            if xmas_button.draw(screen):
                menu_music.stop()
                config.THEME='xmas'
                Game(screen)
                menu_state="main"
        if menu_state== "guide":
            guide_screen(screen)
            back_button= Button(50, 450, config.back_img,0.5) 
            if back_button.draw(screen):
                menu_state="main"
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                run= False
        pygame.display.update()
        
    pygame.quit()

if __name__=='__main__':
    main()