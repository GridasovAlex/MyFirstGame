import pygame

DEFAULT_IMAGE_SIZE = (40, 60)

class Ship():
    """Класс для управления кораблем"""

    def __init__(self, ai_game):
        """Инициализируем корабль и задаем его начальное положение"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #загружает изображение корабля и добавляет прямоугольник
        self.image = pygame.image.load('D:\MyFirstGame\Alien_Inbasion_Game\images\ship.bmp')
        self.image = pygame.transform.scale(self.image, DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect()

        #каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom

        #сохранение вещественной координатыцентра корабля
        self.x = float(self.rect.x)

        #флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update_rect(self):
        """обновляем позицию корабля с учетом флагов"""
        #обновляем по иксу
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.move_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.move_speed

        #обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        """Рисуем корабль в текущей позиции"""
        self.screen.blit(self.image, self.rect)
