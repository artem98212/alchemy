import pygame
import sys
from game import Game  # Импортируем класс Game

# Инициализация Pygame
pygame.init()
# Настройки экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Harvest & Heart")
# Создание экземпляра игры
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

# Игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Обновление и отрисовка игрs
    game.update()
    game.draw(screen)

    # Обновление экрана
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
sys.exit()
