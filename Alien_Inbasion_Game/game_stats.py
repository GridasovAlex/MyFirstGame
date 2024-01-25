class Game_stats():
    """Отслеживанеи статистика для игры"""

    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

        #рекорд не сбрасывается
        self.high_score = 0

        #игра запускается в неактивном состоянии
        self.game_active = False

    def reset_stats(self):
        """инициализирует изминяющуюся в ходе игры статистику"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
