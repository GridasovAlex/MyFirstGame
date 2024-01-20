import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управленяи снарядами выпущенными кораблем"""

    def __init__(self, ai_game):
        """создает объект снарядов в текцщей позиции корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #создание снаряда в позиции (0,0) и назначение правильнйо позиции
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #позиция снаряда хранистя в вещественном формате
        self.y = float(self.rect.y)

    def update(self):
        """Перемещает снаряд вверх по экрану"""
        #обновление позиции снаряда в вещественном формате
        self.y -= self.settings.bullet_speed
        #обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """Вывод снаряда на экран"""
        pygame.draw.rect(self.screen, self.color, self.rect)
