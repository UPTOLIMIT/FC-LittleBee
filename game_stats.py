import game_functions as gf

class GameStats():
    """
    跟踪游戏统计信息
    """

    def __init__(self, ai_settings):
        """
        初始化统计信息
        :param ai_settings:
        """
        self.game_active = False
        self.ai_settings = ai_settings

        self.reset_stats()

    def reset_stats(self):
        """
        初始化在运行期间可能变化的统计信息
        :return:
        """
        self.ships_left = self.ai_settings.ship_limit

