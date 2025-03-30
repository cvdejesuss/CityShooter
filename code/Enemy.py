import pygame
import random
from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.last_shot_time = 0  # Marks the time of the last shot
        self.min_shoot_interval = 5000  # Minimum interval between shots in milliseconds (5 seconds)
        self.max_shoot_interval = 8000  # Maximum interval between shots in milliseconds (8 seconds)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        self.rect.centery += random.choice([-1, 0, 1])  # Small variation in the Y axis

    def shoot(self):
        current_time = pygame.time.get_ticks()  # Gets the current time in milliseconds

        # Generates a random interval between 5s and 8s
        shoot_interval = random.randint(self.min_shoot_interval, self.max_shoot_interval)

        # Checks if the elapsed time is greater than or equal to the random interval
        if current_time - self.last_shot_time >= shoot_interval:
            self.last_shot_time = current_time  # Updates the time of the last shot
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx - 50, self.rect.centery))

        return None  # Returns None if the random interval has not been reached


