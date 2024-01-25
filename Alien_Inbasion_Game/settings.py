"""Создаем класс с настройками"""

class Settings():
    """Класс для хранения всех натсроек игры"""

    def __init__(self):
        """Инициализируем статические настройки игры"""

        #парампетры экрана
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        #параметры снаряда
        self.bullet_width = 6
        self.bullet_height = 12
        self.bullet_color = (90,90,90)
        self.bullet_allowed = 4

        #параметры корабя
        self.ship_limit = 2

        #настройки пришельцев
        self.fleet_drop_speed = 15
        #fleet_derection = 1 - движение вправо, -1 - влево
        self.fleet_derection = 1

        #пдсчет очков
        self.alien_points = 50

        #Темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """инициализируем настройки изменяющие ход игры"""
        self.ship_speed_factor = 1
        self.alien_speed_factor = 0.6
        self.bullet_speed_factor = 1.2

        # fleet_derection = 1 - дыижение вправо, -1 - движение влево
        self.fleet_derection = 1

    def increase_speed(self):
        """Уведичивает настройки скорости"""
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
