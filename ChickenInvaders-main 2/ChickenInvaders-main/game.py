"""
The program defines class Game.
Author: Ho Bui My Duyen
Time spent (days): 2
"""
import pygame
import math
import sys
import time
from pygame import mixer
from chicken import *
import config
from plane import *
from util import *
class Game():
    def __init__(self,screen) -> None:
        """
        The function defines the background music, creates the game window, 
        setting time, and basic controls to start playing and end game.
        Parameter:self (instances of the class)
        Return: NONE
        """
        self.end=False
        # speed
        self.K_DOWN = self.K_UP = self.K_LEFT = self.K_RIGHT = self.K_SPACE=False
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.plane=Plane()
        self.enemy=Chicken()
        if config.THEME=='arcade':
            self.bg=pygame.image.load(config.arcade_bg) 
            self.bg_music=music(config.arcade_music)
        elif config.THEME=='xmas':
            self.bg=pygame.image.load(config.xmas_bg) 
            self.bg_music=music(config.xmas_music)
        self.level=1
        scroll=0
        while not self.end:
            scroll=self.scroll(scroll) #bg on screen
            self.clock.tick(config.FPS)
            self.plane.display(self.screen)
            self.enemy.display(self.screen)
            self.show_score(10,0,self.plane.score,20)
            self.show_heart(10,20,self.plane.lives,20)
            self.show_level(config.SCREEN_WIDTH-100,0,self.enemy.level,20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_DOWN:
                        self.K_DOWN = True
                    if event.key == pygame.K_UP:
                        self.K_UP = True
                    if event.key == pygame.K_LEFT:
                        self.K_LEFT = True
                    if event.key == pygame.K_RIGHT:
                        self.K_RIGHT = True
                    if event.key == pygame.K_SPACE:
                        self.K_SPACE = True
                if event.type == pygame.KEYUP:  
                    if event.key == pygame.K_DOWN:
                        self.K_DOWN = False
                    if event.key == pygame.K_UP:
                        self.K_UP = False
                    if event.key == pygame.K_LEFT:
                        self.K_LEFT = False
                    if event.key == pygame.K_RIGHT:
                        self.K_RIGHT = False
                    if event.key == pygame.K_SPACE:
                        self.K_SPACE = False
                if self.K_DOWN:
                    self.plane.control('down')  
                if self.K_UP:
                    self.plane.control('up')
                if self.K_LEFT:
                    self.plane.control('left')
                if self.K_RIGHT:
                    self.plane.control('right')
                if self.K_SPACE:
                    self.plane.control('space')
                    music(config.shoot)
            self.check_plane_boom(self.enemy,self.plane)
            self.check_chic_boom(self.enemy,self.plane)
            self.check_endgame()
            self.level_up()
            pygame.display.update()
        self.bg_music.stop()
        if self.plane.dead:
            self.lose()
        elif self.level>5:
            self.win()
        
    def level_up(self):
        """_The functions levels up the game.
        Parameter: NONE
        Return: NONE
        """
        if self.enemy.first_row_y>config.SCREEN_HEIGHT+10:
            self.enemy.level+=1
            self.level+=1
            self.plane.level+=1
            self.check_endgame()
            if self.end: return
            self.enemy.first_row_y=-20
            self.enemy.chicken_list.clear()
            self.enemy.allocate(self.enemy.level)
            self.plane.change_bullet()
    def check_endgame(self):
        """The function defines conditions to end game.
        Parameter: NONE
        Return: NONE
        """
        if self.plane.dead or self.level>5:
            self.end=True
    def win(self):
        """The function defines win.
        Paramter: none
        Return: none
        """
        self.screen.blit(config.menu_screen,(0,0))

        win=music(config.win,repeat=True)
        win_img=pygame.image.load(config.win_img)
        self.screen.blit(win_img,(self.screen.get_width()/2-win_img.get_width()/2,self.screen.get_height()/2-win_img.get_height()/2))
        config.THEME='arcade'
        self.show_score(self.screen.get_width()/2-80, self.screen.get_height()/2+100, self.plane.score,20)
        pygame.display.update()
        start=time.time()
        while time.time()-start<8:
            pass
        win.stop()
    def lose(self):
        """The function defines lose.
        Paramter: none
        Return: none
        """
        lose=music(config.lose,repeat=True)
        # lose=music(config.arcade_music)
        self.screen.blit(config.menu_screen,(0,0))
        lose_img=pygame.image.load(config.lose_img)
        self.screen.blit(lose_img,(self.screen.get_width()/2-lose_img.get_width()/2,self.screen.get_height()/2-lose_img.get_height()/2))
        pygame.display.update()
        start=time.time()
        while time.time()-start<10:
            pass
        lose.stop()

    def scroll(self,scroll): 
        """
        The fucntion defines the scroll of the game background.
        Parameter: scroll (int)
        Return: scroll (int)
        """
        bg_height=self.bg.get_height()
        tiles=math.ceil(config.SCREEN_HEIGHT/bg_height)+1
        for i in range(-1,tiles):
            self.screen.blit(self.bg,(0,i*bg_height+scroll))
        scroll+=2
        if abs(scroll) > bg_height:
            scroll = 0
        return scroll    

    

    def show_score(self, x, y, scores, size):  
        """
        The function defines the live scores shown in game.
        Parameters:
            x (int): vertical axis position of scores
            y (int) : horizontal axis position of scores
            scores (string): live scores display
            size (int): size of live scores
        Return: NONE
        """
        font = pygame.font.SysFont("Helvetica", size,bold=True)
        if config.THEME=='arcade':
            color=config.color['WHITE']
        elif config.THEME=='xmas':
            color=config.color['WHITE']
        score = font.render(f'SCORE: {scores}', True, color)
        self.screen.blit(score, (x, y))
    def show_heart(self, x, y, lives, size):  
        """The fuction defines the live heart shown in game.
        Parameters:
            x (int): vertical axis position of hearts
            y (int): horizontal axis position of hearts
            lives (string): live lives display
            size (int): size of live hearts
        Return: NONE
        """
        font = pygame.font.SysFont("Helvetica", size,bold=True)
        if config.THEME=='arcade':
            color=config.color['WHITE']
        elif config.THEME=='xmas':
            color=config.color['WHITE']
        score = font.render(f'HEART: {lives}', True, color)
        self.screen.blit(score, (x, y))
    def show_level(self, x, y, level, size):  
        """The function defines the level shown in game.
        Paramters:
            x (int): vertical axis position of level
            y (int): horizontal axis position of level
            level (string): live level display
            size (int): size of live level
        Return: NONE
        """
        font = pygame.font.SysFont("Helvetica", size,bold=True)
        if config.THEME=='arcade':
            color=config.color['WHITE']
        elif config.THEME=='xmas':
            color=config.color['WHITE']
        score = font.render(f'LEVEL {level}', True, color)
        self.screen.blit(score, (x, y))


    def check_plane_boom(self,chicken,plane):
        """The function checks if chicken and plane collides.

        Paramters:
            chicken (class Chicken Object)
            plane (class Plane Object)
        Return: NONE
        """
        boom=pygame.image.load(config.planeboom_img)
        plane_rect = plane.icon.get_rect().move(plane.x, plane.y) 
        
        for i in chicken.chicken_list:
            chic_rect = chicken.icon.get_rect().move(chicken.chicken_list[i]['x'], chicken.chicken_list[i]['y']) 
            if plane_rect.colliderect(chic_rect):
                self.screen.blit(boom,(plane.x,plane.y))
                music(config.boom)
                plane.lose_life()
                chicken.lose_chicken(i)
                return
    def check_chic_boom(self,chicken,plane):
        """The function checks if the bullets of plan collides with chickens.
        Parameters:
            chicken (class Chicken object)
            plane (class Plane Object)
        Return: NONE
        """
        boom=pygame.image.load(config.chicboom_img)
        for i in chicken.chicken_list:
            chic_rect = chicken.icon.get_rect().move(chicken.chicken_list[i]['x'], chicken.chicken_list[i]['y']) 

            for j in range(len(plane.bullet_list)):
                bullet_rect = plane.bullet_icon.get_rect().move(plane.bullet_list[j]['x'], plane.bullet_list[j]['y']) 
                if bullet_rect.colliderect(chic_rect):
                    self.screen.blit(boom,(plane.bullet_list[j]['x'],plane.bullet_list[j]['y']))
                    music(config.boom)
                    plane.lose_bullet(j)
                    plane.add_score(chicken.level*10)
                    chicken.lose_chicken(i)
                    return



