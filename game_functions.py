import sys
import pygame
from bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, bullets)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        print('right')
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        print('left')
        ship.moving_left = True
    if event.key == pygame.K_UP:
        print('top')
        ship.moving_top = True
    if event.key == pygame.K_DOWN:
        print('bottom')
        ship.moving_bottom = True
    if event.key == pygame.K_SPACE:
        print('bullets')
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        # print('right')
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # print('left')
        ship.moving_left = False
    if event.key == pygame.K_UP:
        # print('up')
        ship.moving_top = False
    if event.key == pygame.K_DOWN:
        # print('down')
        ship.moving_bottom = False


def update_screen(ai_settings, screen, ship, bullets):
    """
    更新屏幕对象，并切换到新屏幕
    每次循环都重新绘制
    :return:
    """
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullet(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
