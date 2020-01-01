import pygame


class Bee():
    def __init__(self, ai_settings, screen):
        """初始化小蜜蜂，并设置其初始位置"""
        self.screen = screen
        # 加载飞船图像，并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        # 将每搜飞船放在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        print('screen bottom is {}'.format(self.screen_rect.bottom))
        print('screen top is {}'.format(self.screen_rect.top))
        print('rect top is {}'.format(self.rect.top))
        print('rect bottom is {}'.format(self.rect.bottom))

        # 在飞船的属性center中存储小数
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
            print('right')
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
            print('left')
        if self.moving_top and self.rect.top > 0:
            print(self.screen_rect.top)
            self.centery -= self.ai_settings.ship_speed_factor
            print('up')
        # 屏幕左上角为坐标原点
        if self.moving_bottom and \
                self.rect.bottom > 0 and \
                self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
            print('down')

        # 根据self.center更新rect对象
        if self.moving_top or self.moving_bottom:
            self.rect.centery = self.centery
        if self.moving_left or self.moving_right:
            self.rect.centerx = self.centerx

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
