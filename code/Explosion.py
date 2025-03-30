import pygame
import time

from code.Entity import Entity


class Explosion(Entity):
    def __init__(self, x, y):
        name = 'Explosion_1'  # Name of the explosion image
        position = (x, y)
        super().__init__(name, position)

        self.animation_frame = 0
        self.animation_speed = 3  # Animation speed (in frames)
        self.timer = time.time()  # Timer to control the animation
        self.is_active = True  # Flag to control if the explosion is still active

        self.scale_factor = 0.5  # Scale factor to adjust the explosion size
        self.rect = pygame.Rect(x, y, 0, 0)  # Initializing the rectangle with the correct position
        self.load_explosion_frame()  # Load the first frame with the correct size

    def load_explosion_frame(self):
        """Loads and resizes the explosion frame."""
        # Load the explosion image
        original_image = pygame.image.load(f'./asset/Explosion_{self.animation_frame + 1}.png').convert_alpha()

        # Resize the explosion image according to the scale factor
        new_width = int(original_image.get_width() * self.scale_factor)
        new_height = int(original_image.get_height() * self.scale_factor)

        # Apply resizing
        self.surf = pygame.transform.scale(original_image, (new_width, new_height))
        self.rect = self.surf.get_rect(center=self.rect.center)  # Using the explosion's center

    def move(self):
        pass  # The explosion does not move, it just displays the animation

    def update(self):
        # Updates the explosion animation
        if time.time() - self.timer > 0.1:  # Adjust the time interval between frames
            self.animation_frame += 1
            if self.animation_frame >= 10:  # Limit the number of frames in the animation
                self.is_active = False  # When the animation ends, deactivate the explosion
                return False  # Returns False to indicate that the explosion should be removed
            # Load the next frame of the animation and resize it
            self.load_explosion_frame()
            self.timer = time.time()
        return True

