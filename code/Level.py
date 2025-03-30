import sys
import random
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 60000  # 60 seconds
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        self.explosion_sound = pygame.mixer.Sound('./asset/ExplosionEnemy.wav')

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(30)

            # Decrease timeout every frame
            self.timeout -= clock.get_time()

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(['Enemy1', 'Enemy2'])
                    self.entity_list.append(EntityFactory.get_entity(choice))

            # Printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            #self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            #self.level_text(14, f'Entities: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            # Display health of Player1 and Player2
            self.display_health()

            # Check for end of level if timeout reaches zero
            if self.timeout <= 0:
                # Proceed to next level or end game
                print("Next level or game over!")
                break

            pygame.display.flip()

            # Collisions - Passing explosion_sound to verify_collision
            EntityMediator.verify_collision(entity_list=self.entity_list, explosion_sound=self.explosion_sound)
            EntityMediator.verify_health(entity_list=self.entity_list, explosion_sound=self.explosion_sound)

    def display_health(self):
        y_offset = WIN_HEIGHT - 35  # Initial position for the first player
        spacing = 20  # Space between texts

        for ent in self.entity_list:
            if isinstance(ent, Player):
                health_text = f'{ent.name} Health: {ent.health}'
                self.level_text(14, health_text, COLOR_WHITE, (10, y_offset))
                y_offset += spacing  # Move the position for the next player

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)





