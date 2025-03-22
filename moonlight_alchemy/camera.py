#camera.py
class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, player):
        # Просто следим за игроком
        self.x = -player.rect.centerx + settings.WIDTH // 2
        self.y = -player.rect.centery + settings.HEIGHT // 2
