import pygame

# Инициализация Pygame
pygame.init()

# Размеры окна
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Заголовок окна
pygame.display.set_caption("Harvest & Heart - Создание мира")

# Размеры тайлов
TILE_SIZE = 32  # Размер одного квадратика карты

# Карта мира (0 - трава, 1 - вода, 2 - гора)
WORLD_MAP = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
]

# Цвета для разных типов местности
GRASS_COLOR = (100, 200, 100)  # Зеленый
WATER_COLOR = (50, 150, 255)  # Синий
MOUNTAIN_COLOR = (150, 100, 50)  # Коричневый

# Функция отрисовки карты
def draw_map(map_data):
    for row_index, row in enumerate(map_data):
        for col_index, tile_type in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            if tile_type == 0:  # Трава
                pygame.draw.rect(screen, GRASS_COLOR, (x, y, TILE_SIZE, TILE_SIZE))
            elif tile_type == 1:  # Вода
                pygame.draw.rect(screen, WATER_COLOR, (x, y, TILE_SIZE, TILE_SIZE))
            elif tile_type == 2:  # Гора
                pygame.draw.rect(screen, MOUNTAIN_COLOR, (x, y, TILE_SIZE, TILE_SIZE))

# Класс игрока
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = TILE_SIZE  # Размер игрока (совпадает с тайлом)
        self.color = (255, 255, 255)  # Белый цвет

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

# Находим первую позицию с травой
def find_grass_spawn_point(map_data):
    for row_index, row in enumerate(map_data):
        for col_index, tile_type in enumerate(row):
            if tile_type == 0: # Трава
                return col_index * TILE_SIZE, row_index * TILE_SIZE  # Возвращаем координаты в пикселях
    return 0, 0 # Если трава не найдена, возвращаем (0, 0)

# Получаем координаты для появления игрока
player_x, player_y = find_grass_spawn_point(WORLD_MAP)

# Создание игрока в начальной позиции
player = Player(player_x, player_y)

# Основной игровой цикл
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Очистка экрана (важно перед каждой отрисовкой)
    screen.fill((0, 0, 0)) # Черный цвет

    # Отрисовка карты
    draw_map(WORLD_MAP)

    # Отрисовка игрока
    player.draw(screen)

    # Обновление экрана
    pygame.display.flip()

# Выход из Pygame
pygame.quit()
