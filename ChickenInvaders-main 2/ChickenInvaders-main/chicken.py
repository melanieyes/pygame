"""
The program defines class Chicken.
Author: Ho Bui My Duyen
Time spent (day): 1
"""
import pygame
import config 
import random
class Chicken:
    def __init__(self) -> None:
        """The function defines the number of chickens and 
        their features in the game.
        Parameter: NONE
        Return: NONE
        """
        self.velocity=1
        self.level=1
        self.icon=pygame.transform.scale(pygame.image.load(config.chicken_img[0]),config.CHICKEN_SIZE)
        self.first_row_y=10
        self.chicken_list={}
        self.chic_per_row=5
        self.allocate(self.level)

    def lose_chicken(self,index_chic):
        """The function defines losing chicken.

        Parameter:
            index_chic (int): the index of chicken
        Return: NONE
        """
        del self.chicken_list[index_chic]
    def allocate(self,level):
        """The function allocates chickens.

        Parameter:
            level (int): level of the game
        Return: NONE
        """
        num_of_chic=self.chic_per_row*level
        x=10
        y=self.first_row_y
        row=0
        for i in range(1,num_of_chic+1):
            icon=pygame.transform.scale(pygame.image.load(config.chicken_img[random.randint(0,7)]),config.CHICKEN_SIZE)
            self.chicken_list[i]={'x':x,'y':y,'icon':icon}
            x+=config.SCREEN_WIDTH//self.chic_per_row
            if i%self.chic_per_row==0:
                y+=50
                if row%2==0:
                    x=(config.SCREEN_WIDTH//self.chic_per_row)/2
                else:
                    x=10
                row+=1
    

    
    def display(self,screen):
        """The function displays chickens on the screen.

        Parameter:
            screen: display chickens on the screen
        Return: NONE
        """
        for chic in self.chicken_list:
            
            screen.blit(self.chicken_list[chic]['icon'],(self.chicken_list[chic]['x'],self.chicken_list[chic]['y']))
        self.move()
    def move (self):
        """The function defines the chicken's move.
        Parameter: NONE
        Return: NONE
        """
        self.first_row_y+=self.velocity
        for i in self.chicken_list:
            self.chicken_list[i]['y']+=self.velocity