# =================================================================
# 3. player.py
# プレイヤークラスを定義するファイルです。（Sprite非依存に変更）
# =================================================================
# ファイル名: player.py

import pygame as pg
from config import *
from bullet import Bullet

class Player: # pg.sprite.Spriteを継承しない
    """プレイヤーを管理するクラス"""
    def __init__(self):
        """プレイヤーの初期化"""
        self.image = pg.image.load("images/ninja.png")
        self.image = pg.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image = pg.transform.flip(self.image, True, False)
        # プレイヤーの位置と速度を設定
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0
        self.fRight = True  # 右を向いているかどうかのフラグ

    def update(self):
        """プレイヤーの位置を更新する"""
        self.speed_x = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
          if(self.fRight == True):
            # 右向きなら、右向きから左向きに変更
            self.image = pg.transform.flip(self.image, True, False)
            self.fRight = False
          self.speed_x = -PLAYER_SPEED
        if keys[pg.K_RIGHT]:
          if(self.fRight == False):
            # 右向きでなければ、左向きから右向きに変更
            self.image = pg.transform.flip(self.image, True, False)
            self.fRight = True
          self.speed_x = PLAYER_SPEED
        
        self.rect.x += self.speed_x

        # 画面の境界チェック
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        """弾を生成して返す"""
        return Bullet(self.rect.centerx, self.rect.top)

    def draw(self, screen):
        """プレイヤーを描画する"""
        screen.blit(self.image, self.rect)
