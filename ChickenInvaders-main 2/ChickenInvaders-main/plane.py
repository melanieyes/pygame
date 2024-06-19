"""
The program defines class Plane.
Author: Ho Bui My Duyen
Time spent (day): 1
"""
import pygame
import config
class Plane:
    def __init__(self) -> None:
        """The function defines plane and its features in game.
        Parameter: NONE
        Return: NONE
        """
        self.dead=False
        self.lives=5
        self.score=0
        self.level=1
        self.velocity=15
        self.bullet_velocity=10
        
        if config.THEME=='arcade':
            self.icon=pygame.image.load(config.arcade_plane) 
            self.bullet_icon=pygame.image.load(config.arcade_bullet[0])
        elif config.THEME=='xmas':
            self.icon=pygame.image.load(config.xmas_plane) 
            self.bullet_icon=pygame.image.load(config.xmas_bullet[0])
        self.x=config.SCREEN_WIDTH/2
        self.y=config.SCREEN_HEIGHT-self.icon.get_height()-15
        self.bullet_list=[]
    def change_bullet(self):
        if config.THEME=='arcade':
            self.bullet_icon=pygame.image.load(config.arcade_bullet[self.level-1])
        elif config.THEME=='xmas':
            self.bullet_icon=pygame.image.load(config.xmas_bullet[self.level-1])
    def lose_life(self):
        """The function defines the condition of losing lives.
        Parameter: NONE
        Return: NONE
        """
        self.lives-=1
        if self.lives==0:
            self.dead=True
    def control(self,key):
        """The function defines the plane control.

        Parameter:
            key: keys to control the plane
        Return: NONE
        """
        if key=='up':
            self.y-=self.velocity
        elif key=='down':
            self.y+=self.velocity
        elif key=='left':
            self.x-=self.velocity
        elif key=='right':
            self.x+=self.velocity
        elif key=='space':
            self.shoot()
        # Correct position
        w=self.icon.get_width()
        h=self.icon.get_height()
        self.x=min(max(self.x,0),config.SCREEN_WIDTH-w)
        self.y=min(max(self.y,0),config.SCREEN_HEIGHT-h+30)

    def display(self,screen):
        """The function displays the plane on the screen.

        Parameter:
            screen: pygame screen
        """
        screen.blit(self.icon,(self.x,self.y))
        self.bullet_display(screen)

    def bullet_display(self,screen):
        """The function displays bullets on the screen.

        Parameter:
            screen: displaying bullets on the screen
        Return: NONE
        """
        for i in range(len(self.bullet_list)):
            screen.blit(self.bullet_icon,(self.bullet_list[i]['x'],self.bullet_list[i]['y']))
        self.bullet_move()
        
    def bullet_move(self):
        """The function defines the move of bullets.
        Parameter: self 
        Return: NONE
        """
        for i in range(len(self.bullet_list)):
            self.bullet_list[i]['y']-=self.bullet_velocity
            
    def lose_bullet(self,index):
        """The function defines the bullet lose.

        Parameter:
            index (int): the index of the bullet in the list
        """
        del self.bullet_list[index]
    def shoot(self):
        """The function defines the shooting technique.
        Paramter: NONE
        Return: NONE
        """
        x=self.x+self.icon.get_width()/2-self.bullet_icon.get_width()/2
        y=self.y
        self.bullet_list.append({'x':x,'y':y})
    def add_score(self,add):
        """The function adds the score for the plane.

        Parameter:
            add (int): the scores added
        """
        self.score+=add