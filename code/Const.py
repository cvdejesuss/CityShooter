# C
import pygame

COLOR_PINK = (255, 182, 193)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# E
ENTITY_SPEED = {
    'Level1Bg0':1,
    'Level1Bg1':1,
    'Level1Bg2':2,
    'Level1Bg3':3,
    'Level1Bg4':4,
    'Level1Bg5':5,
    'Player1' :3,
    'Player2' :3,
}




# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1':pygame.K_w,
                 'Player2':pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1':pygame.K_s,
                 'Player2':pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1':pygame.K_a,
                 'Player2':pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1':pygame.K_d,
                 'Player2':pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1':pygame.K_LCTRL,
                 'Player2':pygame.K_RCTRL}



# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
