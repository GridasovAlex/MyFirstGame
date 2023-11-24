import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion():
    """Класс для управленяи ресурсами и поведением игры"""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption('Alien Invision')
        self.ship = Ship(self)

    def run_game(self):
        """Запуск основнова цикла игры"""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update_rect()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                #ставим флаг перемещения
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                #убираем флаг перемещения
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
            """Обновляет изображение на экране и отображает новый экран"""
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #отображение прорисованного экрана
            pygame.display.flip()


if __name__ == '__main__':
    #создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
