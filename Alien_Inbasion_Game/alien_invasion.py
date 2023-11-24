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
            #отслеживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #при каждом проходе цикла перерисовывается экран
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #отображение прорисованного экрана
            pygame.display.flip()

if __name__ == '__main__':
    #создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
