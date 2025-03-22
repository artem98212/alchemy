# game.py
import pygame
from settings import *
from player import Player
from level import Level
from camera import Camera  # Если вы используете камеру

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True

        self.level = Level("levels/level1.tmx")  # Загрузка уровня

        # Получаем точку появления игрока из уровня
        player_x, player_y = self.level.get_player_spawn_point()
        self.player = Player((player_x, player_y), self.level)  # Начальная позиция игрока

        # Инициализируем камеру, если она используется
        self.camera = Camera(0, 0) #Создаем камеру
        self.camera.update(self.player)

    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000  # Дельта-время в секундах
            self.update(dt)
            self.draw()

    def update(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # TODO: Обработка ввода игрока
            input_state = {
                "move_left": False,
                "move_right": False,
                "jump": False
            }
            self.player.handle_input(input_state)
            self.player.update(dt)
            self.camera.update(self.player) #Обновляем положение камеры

    def draw(self):
        self.screen.fill((0, 0, 0))  # Очищаем экран
        self.level.draw(self.screen, self.camera)  # Рисуем уровень
        self.player.draw(self.screen, self.camera)  # Рисуем игрока
        pygame.display.flip()
