# C
import pygame

COLOR_PINK = (255, 182, 193)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# E
ENTITY_SPEED = {
    'Level1Bg0': 1,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Player1': 3,
    'Player1Shot': 2,
    'Player2': 3,
    'Player2Shot': 2,
    'Enemy1': 2,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 2,
}
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 30,
    'Enemy1Shot': 1,
    'Enemy2': 30,
    'Enemy2Shot': 1,
    'Explosion_1': 0,
    'Explosion_2': 0,
    'Explosion_3': 0,
    'Explosion_4': 0,
    'Explosion_5': 0,
    'Explosion_6': 0,
    'Explosion_7': 0,
    'Explosion_8': 0,
    'Explosion_9': 0,
    'Explosion_10': 0,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Player1': 5,
    'Player1Shot': 10,
    'Player2': 5,
    'Player2Shot': 10,
    'Enemy1': 50,
    'Enemy1Shot': 30,
    'Enemy2': 50,
    'Enemy2Shot': 30,
    'Explosion_1': 0,
    'Explosion_2': 0,
    'Explosion_3': 0,
    'Explosion_4': 0,
    'Explosion_5': 0,
    'Explosion_6': 0,
    'Explosion_7': 0,
    'Explosion_8': 0,
    'Explosion_9': 0,
    'Explosion_10': 0,
}

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 20,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_w,
                 'Player2': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_s,
                   'Player2': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_a,
                   'Player2': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_d,
                    'Player2': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_b,
                    'Player2': pygame.K_RCTRL}

# S
SPAWN_TIME = 4000
# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
