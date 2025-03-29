from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left > WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

            # Colisões entre Player e Inimigo
            if isinstance(test_entity, Player):
                for other in entity_list:
                    if isinstance(other, EnemyShot):
                        if test_entity.rect.colliderect(other.rect):
                            test_entity.health -= 10  # Subtrai 10 de saúde do Player quando atingido por um tiro inimigo
                            other.health = 0  # O tiro do inimigo desaparece após atingir o Player
                    if isinstance(other, Enemy):
                        if test_entity.rect.colliderect(other.rect):
                            test_entity.health -= 20  # Subtrai 20 de saúde do Player quando colide com um inimigo
                            other.health = 0  # O inimigo desaparece após colidir com o Player

            # Colisões entre Tiro e Inimigo
            if isinstance(test_entity, PlayerShot):
                for other in entity_list:
                    if isinstance(other, Enemy):
                        if test_entity.rect.colliderect(other.rect):
                            other.health -= 10  # Diminui a saúde do inimigo ao ser atingido pelo tiro
                            test_entity.health = 0  # O tiro desaparece após atingir o inimigo

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        # Verificar e remover entidades cuja saúde é igual ou inferior a 0
        for entity in entity_list[:]:
            if entity.health <= 0:
                if isinstance(entity, (Enemy, Player)):
                    print(f"{entity.name} foi destruído!")
                entity_list.remove(entity)
