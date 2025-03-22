    # level.py
import pygame
import pytmx

class Level:
    def __init__(self, filename):
        self.tilemap = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = self.tilemap.width * self.tilemap.tilewidth
        self.height = self.tilemap.height * self.tilemap.tileheight

    def update(self):
        pass

    def draw(self, screen, camera):
        for layer in self.tilemap.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = self.tilemap.get_tile_image_by_gid(gid)
                    if tile:
                        screen.blit(tile, (x * self.tilemap.tilewidth - camera.x, y * self.tilemap.tileheight - camera.y))
    
