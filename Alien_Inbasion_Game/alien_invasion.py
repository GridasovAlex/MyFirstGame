import sys
from time import sleep

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import Game_stats
from button import Button

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
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        #экземпляр для хранения игровой статистики
        self.stats = Game_stats(self)

    def run_game(self):
        """Запуск основнова цикла игры"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update_rect()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """реагируент на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        """Запускаем новую игру при зажатии кнопки Play"""
        button_clicket = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicket and not self.stats.game_active:
            #сброс игровых настроек
            self.settings.initialize_dynamic_settings()

            #сброс игровой статистики
            self.stats.reset_stats()
            self.stats.game_active = True

            #очистка списков пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()

            #создание нового флота и размещение корабля в центре
            self._create_fleet()
            self.ship.center_ship()

            #cкрываем указатель мыши
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """обновляет позицию снарядов и уничтожает старые снаряды"""
        # Обновление позиции снарядов
        self.bullets.update()

        #удаление снарядов вышедших за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """обработака коллизий снарядов с пришельцами"""
        #удаление снарядов и пришельуев учавствующих в коллизии
        collision = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            # уничтожение существующих снаряжов и создание нового флота
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _create_fleet(self):
        """созданеи флота вторжения"""
        # создание пришельца и вычисление прищельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avaliable_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avaliable_space_x //(2 * alien_width)

        # определяем кол-во рядов помещающихся на экране
        ship_height = self.ship.rect.height
        avaliable_space_y = (self.settings.screen_height -
                             (3* alien_height) - ship_height)
        num_rows = avaliable_space_y // (2 * alien_height) - 1

        # создание флота пришельцев
        for row_number in range(num_rows):
            for alien_number in range(number_aliens_x):
                # создание пришельца, размещение его в ряду
                self._create_alien(alien_number, alien_width, alien_height, row_number)

        # создание кнопки Play
        self.play_button = Button(self,'Play')

    def _create_alien(self, alien_number, alien_width, alien_height, row_number):
        """создание пришельца и размещение его в ряду"""
        alien = Alien(self)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """обновляет позицию всех пришельцев во флоте"""
        self._check_fleet_edges()
        self.aliens.update()

        # проверка коллизий пришелец-корабль
        if pygame.sprite.spritecollide(self.ship, self.aliens, True):
            self._ship_hit()

        # проверить добрались ли пришельцы до нижнего края экрана
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """реакция на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """опускает флот и меняет направление"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_derection *= -1

    def _ship_hit(self):
        """обработка столкновеняи корабля с пришельцем"""
        if self.stats.ship_left > 0:
            # уменьшение ship_left
            self.stats.ship_left -= 1

            # очистка списков пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()

            # созданери нового флота и размещенеи корабля в центре
            self._create_fleet()
            self.ship.center_ship()

            #пауза
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """проверяет добрались ли пришельцы до левого края экрана"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # происходит тоже что и при столкновении с кораблем
                self._ship_hit()
                break

    def _update_screen(self):
        """Обновляет изображение на экране и отображает новый экран"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
                bullet.draw_bullet()
        self.aliens.draw(self.screen)

        #отоброженеи Play в случае если игра не активна
        if not self.stats.game_active:
            self.play_button.draw_button()

        #отображение прорисованного экрана
        pygame.display.flip()


if __name__ == '__main__':
    #создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()
