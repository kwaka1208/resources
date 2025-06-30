# =================================================================
# 2. bullet.py
# 弾クラスを定義するファイルです。
# =================================================================
# ファイル名: bullet.py

import pygame as pg
from config import *

class Bullet:
    """弾を管理するクラス"""
    def __init__(self, x, y):
        """
        弾の初期化
        Args:
            x (int): 弾が発射されるx座標
            y (int): 弾が発射されるy座標
        """
        # super().__init__() は不要
        # 弾の形状と色を設定
        self.image = pg.image.load("images/bullet.png")
        self.image = pg.transform.scale(self.image, (BULLET_WIDTH, BULLET_HEIGHT))
        # 弾の位置と速度を設定
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed_y = -BULLET_SPEED
        pg.mixer.Sound("sounds/maou_se_battle17.mp3").play()

    def update(self):
        """弾の位置を更新する"""
        self.rect.y += self.speed_y
        
    def draw(self, screen):
        """弾を描画する"""
        screen.blit(self.image, self.rect)
