import pygame
import pytmx

class Map:
    def __init__(self, filename):
        tm = pytmx.load_pygame(filename, pixelalpha=True)  # pixelalpha сохраняет прозрачность
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmx_data = tm

    def render(self, surface):
        ti = self.tmx_data.get_tile_image_by_gid
        for layer in self.tmx_data.visible_layers:  # Перебираем все видимые слои
            if isinstance(layer, pytmx.TiledTileLayer): # Если это слой с тайлами
                for x, y, gid in layer:
                    tile = ti(gid)
                if tile:
                    surface.blit(tile, (x * self.tmx_data.tilewidth, y * self.tmx_data.tileheight))

    def make_map(self): # Возвращает поверхность с отрисованной картой
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface
