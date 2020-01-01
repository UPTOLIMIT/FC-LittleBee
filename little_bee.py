import sys
import pygame
from settings import Settings
from Bee import Bee
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("LittleBee")

    # 创建一艘飞船
    ship = Bee(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = pygame.sprite.Group()

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        # 每次循环都重绘屏幕
        gf.update_bullet(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
