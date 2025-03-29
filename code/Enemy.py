import pygame
import random
from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.last_shot_time = 0  # Marca o tempo do último disparo
        self.min_shoot_interval = 5000  # Intervalo mínimo entre disparos em milissegundos (5 segundos)
        self.max_shoot_interval = 8000  # Intervalo máximo entre disparos em milissegundos (8 segundos)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        current_time = pygame.time.get_ticks()  # Obtém o tempo atual em milissegundos

        # Gera um intervalo aleatório entre 5s e 8s (3 e 4 segundos)
        shoot_interval = random.randint(self.min_shoot_interval, self.max_shoot_interval)

        # Verifica se o tempo passado é maior ou igual ao intervalo aleatório
        if current_time - self.last_shot_time >= shoot_interval:
            self.last_shot_time = current_time  # Atualiza o tempo do último disparo
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx - 50, self.rect.centery))

        return None  # Retorna None se o intervalo aleatório não foi alcançado

