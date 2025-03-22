    # player.py
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position, level):
        super().__init__()
        # Создаем поверхность и заполняем ее красным цветом (для отладки)
        self.image = pygame.Surface((32, 64))  # Создаем поверхность размером 32x64 пикселя
        self.image.fill((255, 0, 0))  # Заполняем поверхность красным цветом

        self.rect = self.image.get_rect(topleft=position)
        self.x = position[0]
        self.y = position[1]
        self.level = level

    def handle_input(self, input_state):
        pass

    def update(self, dt):
        pass

    def draw(self, screen, camera):
        screen.blit(self.image, (self.rect.x, self.rect.y))
