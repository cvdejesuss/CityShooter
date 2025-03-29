import pygame.key

from code.Entity import Entity



class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP]:
            self.rect.centery -= 1
        pass