"""
The program defines the class Button for UI in the game.
Author: Ho Bui My Duyen & Le Thi Diem My
Time spent (hours): 2
"""
import pygame
from pygame import mixer
import config
class Button():
    def __init__(self, x, y, image, scale):
        """The function defines the images and scale of buttons.

        Paramter:
            x (int): vertical axis position of level
            y (int): horizontal axis position of level
            image (png): buttons' image
            scale (int): scale of buttons
        Return: NONE
        """
        self.image=pygame.image.load(image).convert_alpha()
        self.image= pygame.transform.scale(self.image, (int(self.image.get_width()* scale), int(self.image.get_height()* scale)))      
        self.rect= self.image.get_rect()
        self.rect.topleft=(x,y)
        self.clicked= False
    
    def draw(self, surface):
        """The function draws buttons on screen surface.

        Parameter:
            surface: the surface on which the buttons shown

        Returns:
            action: the button get clicked 
        """
        action=False
        pos= pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked== False:
                self.clicked= True
                action= True
                music(config.enter)
            if pygame.mouse.get_pressed()[0]==0:
                self.clicked=False
                  
        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action   
def music(url,repeat=False):  
    """
    The function defines the game sound effect.
    Parameter:
        url
    Return: the sound played
    """
    sound = mixer.Sound(url)
    if repeat:
        sound.play(-1)
    else:
        sound.play()
    return sound

def draw_text(text, font, text_col, x, y,screen):
    """The function draws texts of buttons on the screen.

    Args:
        text (str): the texts of buttons
        font : font of texts
        text_col : color of texts
        x (int): vertical axis position of level
        y (int): horizontal axis position of level
        screen : the screen on which the buttons shown
    """
    font = pygame.font.SysFont(font,20,bold=True)
    img= font.render(text, True, text_col)
    screen.blit(img, (x,y))
def guide_screen(screen):
    """The function screens the guidance of the game.

    Parameter:
        screen : the screen on which the buttons shown
    """
    draw_text('PRESS SPACE TO SHOOT','Bungee',config.color['WHITE'],300,320,screen)
    draw_text('PRESS ARROW KEY TO MOVE','Bungee',config.color['WHITE'],300,360,screen)