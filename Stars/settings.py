# -*-coding:UTF-8-*-

class Settings():
    """储存《外星人入侵》的所有设置的类"""
    bg_color = None

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # 飞船的设置
        self.ship_speed_factor = 10 

        # 子弹设计
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 300

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1