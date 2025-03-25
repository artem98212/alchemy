import pygame
from player import Player
from map import Map

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = Player(100, 100, "assets/NPC/player.png")
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        # Загрузка TMX-карты
        self.map = Map("assets/map/map.tmx")
        self.map_image = self.map.make_map()  # Создаем поверхность с картой
        self.map_rect = self.map_image.get_rect() # Получаем прямоугольник карты

    def update(self):
        self.player.update()

    def draw(self, surface):
        surface.fill((0, 0, 0))
        surface.blit(self.map_image, (0, 0)) # Рисуем карту
        self.all_sprites.draw(surface)
