# Entity.py

from abc import ABC, abstractmethod
import pygame
from code.Const import ENTITY_HEALTH, ENTITY_DAMAGE  # Importando o dicionário ENTITY_HEALTH

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]  # Atribuindo a saúde baseada no nome da entidade
        self.damage = ENTITY_DAMAGE[self.name]

    @abstractmethod
    def move(self):
        pass
