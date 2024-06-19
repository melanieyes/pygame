"""
This program imports pygame to build the game background with screen set-up,
game components and figures import and 
other different keys to play the game.
Author: Ho Bui My Duyen
Time: 30 minutes
"""
import pygame
# global
THEME='arcade'
# load button images
start_img="Image/button/start.png"
arcade_img="Image/button/arcade.png"
xmas_img="Image/button/xmas.png"
guide_img="Image/button/guide.png"
back_img ="Image/button/back.png"
quit_img ="Image/button/quit.png"
title_img ="Image/button/title.png"
# Background
SCREEN_WIDTH= 800
SCREEN_HEIGHT= 600
arcade_bg ='Image/Background/stars_galaxyx4.png'
xmas_bg='Image/Background/stars_galaxyx4.png'
bg_blurred_img='Image/Background/SpaceBackground.jpg'
arcade_plane='Image/Object/rsz_ship5.png'
xmas_plane='Image/Object/1rsz_shipgreen.png'
chicken_img=['Image/Object/chicken1.png','Image/Object/chicken2.png','Image/Object/chicken3.png','Image/Object/chicken4.png','Image/Object/chicken5.png','Image/Object/chicken6.png','Image/Object/chicken7.png','Image/Object/chicken8.png']
arcade_bullet=['Image/Object/bullet1.png','Image/Object/bullet2.png','Image/Object/bullet3.png','Image/Object/bullet4.png','Image/Object/bullet5.png']
xmas_bullet=['Image/Object/bulletx1.png','Image/Object/bulletx2.png','Image/Object/bulletx3.png','Image/Object/bulletx4.png','Image/Object/bulletx5.png']
planeboom_img='Image/Object/boom2.png'
chicboom_img='Image/Object/boom1.png'
win_img='Image/Object/vict.png'
lose_img='Image/Object/game_over.png'
# screen
menu_screen=pygame.image.load(bg_blurred_img)
#Size
CHICKEN_SIZE=(110,78)
# Music
lose='Sound/Sound_GameOver.wav'
win='Sound/Sound_Victory.wav'
arcade_music='Sound/arcade.mp3'
xmas_music='Sound/Theme.mp3'
menu_music='Sound/menu.mp3'
enter='Sound/enter.wav'
button='Sound/button.wav'
bg_music='Sound/theme.wav'
shoot='Sound/gunshot.wav'
boom='Sound/boom2.wav'
# Clock
FPS=60
color={'WHITE' : (255, 255, 255),
'RED'   : (255,   0,   0),
'GREEN' : (  0, 255,   0),
'BLUE'  : (  0,   0, 255)
}
# color={'BLACK' : (0,   0,   0),
# 'WHITE' : (255, 255, 255),
# 'RED'   : (255,   0,   0),
# 'GREEN' : (  0, 255,   0),
# 'BLUE'  : (  0,   0, 255)
# }
key = {"space": pygame.K_SPACE, "esc": pygame.K_ESCAPE, "up": pygame.K_UP, "down": pygame.K_DOWN,
           "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "return": pygame.K_RETURN,
           "a": pygame.K_a,
           "b": pygame.K_b,
           "c": pygame.K_c,
           "d": pygame.K_d,
           "e": pygame.K_e,
           "f": pygame.K_f,
           "g": pygame.K_g,
           "h": pygame.K_h,
           "i": pygame.K_i,
           "j": pygame.K_j,
           "k": pygame.K_k,
           "l": pygame.K_l,
           "m": pygame.K_m,
           "n": pygame.K_n,
           "o": pygame.K_o,
           "p": pygame.K_p,
           "q": pygame.K_q,
           "r": pygame.K_r,
           "s": pygame.K_s,
           "t": pygame.K_t,
           "u": pygame.K_u,
           "v": pygame.K_v,
           "w": pygame.K_w,
           "x": pygame.K_x,
           "y": pygame.K_y,
           "z": pygame.K_z,
           "1": pygame.K_1,
           "2": pygame.K_2,
           "3": pygame.K_3,
           "4": pygame.K_4,
           "5": pygame.K_5,
           "6": pygame.K_6,
           "7": pygame.K_7,
           "8": pygame.K_8,
           "9": pygame.K_9,
           "0": pygame.K_0}
