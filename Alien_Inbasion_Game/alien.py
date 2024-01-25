from typing import Any
import pygame
from pygame.sprite import Sprite

DEFAULT_IMAGE_SIZE = (60,40)

class Alien(Sprite):
    """класс, представляющий оного пришельца"""

    def __init__(self, ai_game):
        """инициаоизируем пришельца и задаем его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('Alien_Inbasion_Game\images\lien.bmp')
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()

        # каждый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной горизонатльной позиции пришельца
        self.x = float(self.rect.x)

    def check_edges(self):
        """возвращает True если пишелец находистя у края экрана"""
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right - 50) or self.rect.left <= 0:
            return True

    def update(self):
        """перемещенеи пришельца влево и вправо"""
        self.x += (self.settings.alien_speed_factor
                   * self.settings.fleet_derection)
        self.rect.x = self.x
