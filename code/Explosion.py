import pygame
import time

from code.Entity import Entity


class Explosion(Entity):
    def __init__(self, x, y):
        name = 'Explosion_1'  # Nome da imagem de explosão
        position = (x, y)
        super().__init__(name, position)

        self.animation_frame = 0
        self.animation_speed = 3  # Velocidade da animação (em quadros)
        self.timer = time.time()  # Temporizador para controlar a animação
        self.is_active = True  # Flag para controlar se a explosão ainda está ativa

    def move(self):
        pass  # Não se move, apenas exibe a animação

    def update(self):
        # Atualiza a animação da explosão
        if time.time() - self.timer > 0.1:  # Ajuste o intervalo de tempo entre os quadros
            self.animation_frame += 1
            if self.animation_frame >= 10:  # Limite o número de quadros da animação
                self.is_active = False  # Quando a animação acabar, desativa a explosão
                return False  # Retorna falso para indicar que a explosão deve ser removida
            # Carregar o próximo quadro da animação
            self.surf = pygame.image.load(f'./asset/Explosion_{self.animation_frame + 1}.png').convert_alpha()
            self.timer = time.time()
        return True
