import pygame
from pygame.sprite import _Group, Sprite

class Alien(Sprite):
    """класс, представляющий оного пришельца"""

    def __init__(self, ai_game):
        """инициаоизируем пришельца и задаем его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('images\lien.bmp')
        self.rect = self.image.get_rect()

        # каждый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной горизонатльной позиции пришельца
        self.x = float(self.rect.x)
