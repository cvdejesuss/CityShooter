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
        self.is_active = True  # Flag para controlar se a explosão continua ativa

        self.scale_factor = 0.5  # Fator de escala para ajustar o tamanho da explosão
        self.rect = pygame.Rect(x, y, 0, 0)  # Inicializando o retângulo com a posição correta
        self.load_explosion_frame()  # Carregar o primeiro quadro com o tamanho adequado

    def load_explosion_frame(self):
        """Carrega e redimensiona o quadro da explosão."""
        # Carregar a imagem da explosão
        original_image = pygame.image.load(f'./asset/Explosion_{self.animation_frame + 1}.png').convert_alpha()

        # Redimensionar a imagem da explosão conforme o fator de escala
        new_width = int(original_image.get_width() * self.scale_factor)
        new_height = int(original_image.get_height() * self.scale_factor)

        # Aplicar o redimensionamento
        self.surf = pygame.transform.scale(original_image, (new_width, new_height))
        self.rect = self.surf.get_rect(center=self.rect.center)  # Usando o centro da explosão

    def move(self):
        pass  # A explosão não se move, apenas exibe a animação

    def update(self):
        # Atualiza a animação da explosão
        if time.time() - self.timer > 0.1:  # Ajuste o intervalo de tempo entre os quadros
            self.animation_frame += 1
            if self.animation_frame >= 10:  # Limite o número de quadros da animação
                self.is_active = False  # Quando a animação acabar, desativa a explosão
                return False  # Retorna falso para indicar que a explosão deve ser removida
            # Carregar o próximo quadro da animação e redimensioná-lo
            self.load_explosion_frame()
            self.timer = time.time()
        return True
