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
        self.bullet_speed = 1
        self.bullet_width = 6
        self.bullet_height = 12
        self.bullet_color = (90,90,90)
        self.bullet_allowed = 4

        #скорость перемещения корабя
        self.move_speed = 1

        #настройки пришельцев
        self.alien_speed = 0.9
