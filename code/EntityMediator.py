from code.Const import WIN_WIDTH, ENTITY_DAMAGE, ENTITY_HEALTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot
from code.Explosion import Explosion

class EntityMediator:
    @staticmethod
    def __verify_collision_window(ent: Entity):
        # If the entity passes the screen edge, health should be set to zero
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:  # If the enemy went off the left edge
                ent.health = 0
        elif isinstance(ent, PlayerShot):
            if ent.rect.left > WIN_WIDTH:  # If the player's shot went off the right edge
                ent.health = 0
        elif isinstance(ent, EnemyShot):
            if ent.rect.right <= 0:  # If the enemy's shot went off the left edge
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity], explosion_sound):
        to_remove = []  # List to mark entities to be removed

        for i in range(len(entity_list)):
            entity1 = entity_list[i]

            # Collision detection
            if isinstance(entity1, Player):
                for other in entity_list:
                    if isinstance(other, EnemyShot):
                        if entity1.rect.colliderect(other.rect):
                            # Apply the enemy's shot damage to the player
                            entity1.health -= ENTITY_DAMAGE[other.name]
                            other.health = 0  # The enemy's shot disappears
                            to_remove.append(other)  # Marks the shot for removal
                    elif isinstance(other, Enemy):
                        if entity1.rect.colliderect(other.rect):
                            # Apply the enemy's damage to the player
                            entity1.health -= ENTITY_DAMAGE[other.name]
                            other.health = 0  # The enemy disappears after the collision
                            # Create the explosion when the ships collide
                            explosion = Explosion(other.rect.centerx, other.rect.centery)
                            entity_list.append(explosion)  # Adds the explosion to the list
                            explosion_sound.play()  # Plays the explosion sound
                            to_remove.append(other)  # Marks the enemy for removal

            # Collisions between Player's Shot and Enemies
            if isinstance(entity1, PlayerShot):
                for other in entity_list:
                    if isinstance(other, Enemy):
                        if entity1.rect.colliderect(other.rect):
                            # Apply the player's shot damage to the enemy
                            other.health -= ENTITY_DAMAGE[entity1.name]
                            entity1.health = 0  # The shot disappears

                            # If the enemy's health is zero after damage, create the explosion
                            if other.health <= 0:
                                explosion = Explosion(other.rect.centerx, other.rect.centery)
                                entity_list.append(explosion)  # Adds the explosion to the list
                                explosion_sound.play()  # Plays the explosion sound
                            to_remove.append(entity1)  # Marks the shot for removal

        # Remove entities marked for removal
        for entity in to_remove:
            if entity in entity_list:
                entity_list.remove(entity)

    @staticmethod
    def verify_health(entity_list: list[Entity], explosion_sound):
        to_remove = []  # List for entities that need to be removed

        # Check entities and add explosions when necessary
        for entity in entity_list[:]:
            if entity.health <= 0:
                # If the entity is a Player or Enemy, generate an explosion
                if isinstance(entity, (Player, Enemy)):
                    # Create the explosion at the entity's position
                    explosion = Explosion(entity.rect.centerx, entity.rect.centery)
                    entity_list.append(explosion)  # Adds the explosion to the list
                    explosion_sound.play()  # Plays the explosion sound

                    # Marks the entity for removal
                    to_remove.append(entity)

                # Add explosion for the player
                if isinstance(entity, Player) and entity.health <= 0:
                    # Create the player's ship explosion
                    explosion = Explosion(entity.rect.centerx, entity.rect.centery)
                    entity_list.append(explosion)  # Adds the explosion to the list
                    explosion_sound.play()  # Plays the explosion sound
                    to_remove.append(entity)  # Marks the player's ship for removal

        # Remove entities and explosions
        for entity in to_remove:
            if entity in entity_list:
                entity_list.remove(entity)

        # Check explosions for removal
        for explosion in entity_list[:]:
            if isinstance(explosion, Explosion):
                if not explosion.update():  # If the explosion finished its animation
                    entity_list.remove(explosion)  # Removes the explosion from the list



