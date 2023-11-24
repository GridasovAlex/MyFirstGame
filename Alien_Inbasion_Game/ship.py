import pygame

DEFAULT_IMAGE_SIZE = (40, 60)

class Ship():
    """Класс для управления кораблем"""

    def __init__(self, ai_game):
        """Инициализируем корабль и задаем его начальное положение"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #загружает изображение корабля и добавляет прямоугольник
        self.image = pygame.image.load('D:\MyFirstGame\Alien_Inbasion_Game\images\ship.bmp')
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()

        #каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисуем корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
