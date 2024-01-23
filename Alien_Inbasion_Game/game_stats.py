class Game_stats():
    """Отслеживанеи статистика для игры"""

    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """инициализирует изминяющуюся в ходе игыр статистику"""
        self.ship_left = self.settings.ship_limit
