from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot
from code.Explosion import Explosion

class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        # Se a entidade passar da borda da tela, a saúde deve ser zerada
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:  # Se o inimigo saiu pela borda esquerda
                ent.health = 0
        elif isinstance(ent, PlayerShot):
            if ent.rect.left > WIN_WIDTH:  # Se o tiro do jogador saiu pela borda direita
                ent.health = 0
        elif isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:  # Se o tiro inimigo saiu pela borda esquerda
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        to_remove = []  # Lista para armazenar entidades que devem ser removidas

        for i in range(len(entity_list)):
            entity1 = entity_list[i]

            # Verificação de colisões com o jogador
            if isinstance(entity1, Player):
                for other in entity_list:
                    if isinstance(other, EnemyShot):
                        if entity1.rect.colliderect(other.rect):
                            entity1.health -= 30  # Subtrai saúde do jogador
                            other.health = 0  # O tiro do inimigo desaparece
                            to_remove.append(other)  # Marca o tiro para remoção
                            break  # Impede múltiplas colisões com o mesmo tiro

                    elif isinstance(other, Enemy):
                        if entity1.rect.colliderect(other.rect):
                            entity1.health -= 50  # Subtrai saúde do jogador
                            other.health = 0  # O inimigo desaparece após a colisão
                            to_remove.append(other)  # Marca o inimigo para remoção
                            break  # Impede múltiplas colisões com o mesmo inimigo

            # Verificação de colisões com o tiro do jogador
            if isinstance(entity1, PlayerShot):
                for other in entity_list:
                    if isinstance(other, Enemy):
                        if entity1.rect.colliderect(other.rect):
                            other.health -= 10  # Reduzir saúde do inimigo
                            entity1.health = 0  # O tiro desaparece
                            to_remove.append(entity1)  # Marca o tiro para remoção
                            break  # Impede múltiplas colisões com o mesmo tiro

        # Remove as entidades marcadas para remoção
        for entity in to_remove:
            if entity in entity_list:
                entity_list.remove(entity)

    @staticmethod
    def verify_health(entity_list: list[Entity], explosion_sound):
        to_remove = []

        # Verificar as entidades e adicionar explosões quando necessário
        for entity in entity_list[:]:
            if entity.health <= 0:
                # Se a entidade é um Player ou Enemy, geramos uma explosão
                if isinstance(entity, (Player, Enemy)):
                    # Cria a explosão na posição da entidade
                    explosion = Explosion(entity.rect.centerx, entity.rect.centery)
                    entity_list.append(explosion)  # Adiciona a explosão à lista
                    explosion_sound.play()  # Toca o som da explosão

                    # Marca a entidade para remoção
                    to_remove.append(entity)

        # Remover entidades e explosões
        for entity in to_remove:
            if entity in entity_list:
                entity_list.remove(entity)

        # Verificar as explosões para remoção
        for explosion in entity_list[:]:
            if isinstance(explosion, Explosion):
                if not explosion.update():  # Se a explosão terminou sua animação
                    entity_list.remove(explosion)  # Remove a explosão da lista
