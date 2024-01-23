"""Создаем класс с настройками"""

class Settings():
    """Класс для хранения всех натсроек игры"""

    def __init__(self):
        """Инициализируем настройки игры"""

        #парампетры экрана
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        #параметры снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 300
        self.bullet_height = 8
        self.bullet_color = (90,90,90)
        self.bullet_allowed = 4

        #скорость перемещения корабя
        self.move_speed = 1
        self.ship_limit = 3

        #настройки пришельцев
        self.alien_speed = 0.6
        self.fleet_drop_speed = 5
        #fleet_derection = 1 - движение вправо, -1 - влево
        self.fleet_derection = 1

        #
