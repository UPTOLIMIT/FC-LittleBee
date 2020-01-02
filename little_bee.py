import sys
import pygame
from settings import Settings
from Bee import Bee
from Alien import Alien
import game_functions as gf
from game_stats import GameStats


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("LittleBee")
    stats=GameStats(ai_settings)

    # 创建一艘飞船
    ship = Bee(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = pygame.sprite.Group()
    # 创建一个外星人
    alien = Alien(ai_settings, screen)
    aliens = pygame.sprite.Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()

            # 每次循环都重绘屏幕
            gf.update_bullet(ai_settings, screen, ship, bullets, aliens)

            gf.update_aliens(ai_settings, screen,stats,ship, aliens,bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
