import pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Заголовок окна
pygame.display.set_caption("Harvest & Heart - Создание мира")

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение экрана цветом (например, зеленым)
    screen.fill((100, 200, 100))  # RGB: Зеленый цвет

    # Обновление экрана
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
