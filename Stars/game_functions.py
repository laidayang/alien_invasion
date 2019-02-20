# -*-coding:UTF-8-*-
import sys
import pygame
from Stars.bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应案件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_lift = True
    elif event.key == pygame.K_SPACE:
         fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_lift = False

def check_event(ai_settings,screen,ship,bullets):
    """响应案件和鼠标事件"""
    # 如果判断为QUIT健就退出系统
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_screen(ai_setting,screen,ship,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_setting.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并且删除已消失的子弹"""
    # 更新子弹位置
    bullets.update()

    # 删除已经消失的子弹(超出屏幕的子弹，应该删除)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    print(len(bullets))


def fire_bullet(ai_settings,screen,ship,bullets):
    """如果没有达到上线就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)