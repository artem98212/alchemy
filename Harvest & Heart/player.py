import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()

        # Загрузка изображения игрока
        self.image = pygame.image.load(image_path).convert_alpha() # convert_alpha сохраняет прозрачность
        self.rect = self.image.get_rect()  # Получаем прямоугольник для позиционирования

        # Начальная позиция игрока
        self.rect.x = x
        self.rect.y = y

        # Скорость игрока
        self.speed = 5

    def update(self):
        # Обработка ввода и перемещение игрока
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Ограничение движения игрока в пределах экрана (пока без столкновений)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:  # Замените 800 на SCREEN_WIDTH
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600: # Замените 600 на SCREEN_HEIGHT
            self.rect.bottom = 600

    def draw(self, surface):
        # Отрисовка игрока на экране
        surface.blit(self.image, self.rect)

