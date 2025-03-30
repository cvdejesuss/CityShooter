# Entity.py

from abc import ABC, abstractmethod
import pygame
from code.Const import ENTITY_HEALTH  # Importando o dicionário ENTITY_HEALTH

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH.get(name, 0)  # Atribuindo a saúde baseada no nome da entidade

    @abstractmethod
    def move(self):
        pass
