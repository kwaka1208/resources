# =================================================================
# 5. main.py
# ゲームのメイン処理を行うファイルです。（Sprite非依存に変更）
# =================================================================
# ファイル名: main.py

import pygame as pg
import sys
from config import *
from player import Player
from enemy import Enemy

class Game:
    """ゲーム全体を管理するクラス"""
    def __init__(self):
        """ゲームの初期化"""
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(SCREEN_TITLE)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font('arial')
        self.running = True
        self.score = 0

    def new(self):
        """新しいゲームを開始する"""
        # オブジェクト管理をリストで行う
        self.enemies = []
        self.bullets = []

        # プレイヤーインスタンスの作成
        self.player = Player()
        
        # 最初に複数の敵を生成
        for _ in range(ENEMY_COUNT):
            self.enemies.append(Enemy())
        
        self.enemy_spawn_counter = 0
        self.score = 0
        self.run()

    def run(self):
        """ゲームループ"""
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        """ゲームの状態を更新（手動処理）"""
        # 各オブジェクトの更新
        self.player.update()
        for enemy in self.enemies:
            enemy.update()
        # リストをコピーしてループしないと、ループ中の削除で問題が起きる
        for bullet in self.bullets[:]:
            bullet.update()
            # 画面外に出た弾を削除
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        
        # 敵の生成を制御
        self.enemy_spawn_counter += 1
        if self.enemy_spawn_counter >= ENEMY_SPAWN_RATE:
            self.enemy_spawn_counter = 0
            self.enemies.append(Enemy())
            
        # 当たり判定: 弾と敵
        # ループ中にリストから要素を削除するとインデックスがずれるため、
        # 衝突したものを一旦別のリストに保存し、後でまとめて削除する
        bullets_to_remove = []
        enemies_to_remove = []
        for bullet in self.bullets:
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    # 衝突した弾と敵を削除リストに追加
                    if bullet not in bullets_to_remove:
                        bullets_to_remove.append(bullet)
                    if enemy not in enemies_to_remove:
                        enemies_to_remove.append(enemy)
        
        # 衝突したオブジェクトを削除し、スコアを加算
        if enemies_to_remove:
            self.score += len(enemies_to_remove) * 10
            for bullet in bullets_to_remove:
                if bullet in self.bullets: # 既に削除されている可能性を考慮
                    self.bullets.remove(bullet)
            for enemy in enemies_to_remove:
                if enemy in self.enemies:
                    self.enemies.remove(enemy)
                    # 敵を倒したら新しい敵を補充する
                    self.enemies.append(Enemy())

        # 当たり判定: プレイヤーと敵
        for enemy in self.enemies:
            if self.player.rect.colliderect(enemy.rect):
                self.playing = False
                break

    def events(self):
        """イベント処理（キー入力など）"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.bullets.append(self.player.shoot())

    def draw(self):
        """描画処理（手動処理）"""
        self.screen.fill(STAGE_COLOR)
        # 各オブジェクトの描画
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
            
        self.draw_text(f"Score: {self.score}", 22, FORE_COLOR, SCREEN_WIDTH / 2, 10)
        pg.display.flip()
        
    def draw_text(self, text, size, color, x, y):
        """画面にテキストを描画するヘルパー関数"""
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        """ゲーム開始画面"""
        self.screen.fill(STAGE_COLOR)
        self.draw_text(SCREEN_TITLE, 48, FORE_COLOR, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text(START_TITLE, 36, FORE_COLOR, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4 + 100)
        pg.display.flip()
        self.wait_for_key()

    def show_game_over_screen(self):
        """ゲームオーバー画面"""
        if not self.running:
            return
        self.screen.fill(STAGE_COLOR)
        self.draw_text("GAME OVER", 48, FORE_COLOR, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.draw_text(f"Score: {self.score}", 36, FORE_COLOR, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.draw_text(START_TITLE, 36, FORE_COLOR, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        """キー入力を待つ"""
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP and event.key == pg.K_s:
                    waiting = False

# ゲームインスタンスの作成と実行
if __name__ == '__main__':
    g = Game()
    g.show_start_screen()
    while g.running:
      g.new()
      g.show_game_over_screen()

    pg.quit()
    sys.exit()

