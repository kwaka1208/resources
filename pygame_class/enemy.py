# =================================================================
# 4. enemy.py
# 敵クラスを定義するファイルです。（Sprite非依存に変更）
# =================================================================
# ファイル名: enemy.py

import pygame as pg
import random
from config import *

class Enemy: # pg.sprite.Spriteを継承しない
    """敵を管理するクラス"""
    def __init__(self):
        """敵の初期化"""
        # super().__init__() は不要
        # 敵の形状と色を設定
        self.image = pg.image.load("images/enemy.png")
        self.image = pg.transform.scale(self.image, (ENEMY_WIDTH, ENEMY_HEIGHT))
        # 敵の初期位置と速度を設定
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40) # 画面の上から出現
        self.speed_y = ENEMY_SPEED

    def update(self):
        """敵の位置を更新する"""
        self.rect.y += self.speed_y
        # 敵が画面下を通り過ぎたら、新しい敵として再配置する
        if self.rect.top > SCREEN_HEIGHT + 10:
            self.rect.x = random.randrange(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)

    def draw(self, screen):
        """敵を描画する"""
        screen.blit(self.image, self.rect)
