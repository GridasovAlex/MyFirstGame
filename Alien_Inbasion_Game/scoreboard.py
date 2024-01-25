import pygame.font

class Scoreboard():
    """Класс для вывода игровой информации"""

    def __init__(self, ai_game):
        """инициализирует атрибуты подсчета очков"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #настройки шрифта для вывода счета
        self.text_color = (138,43,226)
        self.font = pygame.font.SysFont(None, 40)
        self.lvl_color = (138,43,226)

        #подготовка изображений счетов
        self.prep_score()
        self.prep_high_score()
        self.prepr_lvl()

    def prep_score(self):
        """преобразует текущий счет в графическое изображение"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                        self.text_color, self.settings.bg_color)

        #вывод счета в парвой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """преобразует рекордный счет в графическое изображение"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                        self.text_color, self.settings.bg_color)

        #рекорд выравнивается по центру верхней стороны
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """выводит счет, рекорд и уровень на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image , self.level_rect)


    def check_high_score(self):
        """проверяет появился ли новый рекорд"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prepr_lvl(self):
        """преобразовать уровень в графическое изображение"""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                            self.lvl_color, self.settings.bg_color)

        #уровень выводится под счетом
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
