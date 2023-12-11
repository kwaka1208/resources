import pygame as pg
import sys

# pygame初期化
pg.init()

screen_w = 800
screen_h = 600

player_x = screen_w / 2 # プレイヤーのx座標
player_y = 600 - 100    # プレイヤーのy座標
player_h = 100          # プレイヤーの高さ
player_w = 100          # プレイヤーの幅

# 画面設定
screen = pg.display.set_mode((screen_w, screen_h)) 
player = pg.image.load("images/blue_ninja.png")
player = pg.transform.scale(player, (player_h, player_w))
player = pg.transform.flip(player, True, False)
player_rect = pg.rect.Rect(player_x, player_y, player_h, player_w)
move = 10

while True:
    # 画面を白で塗りつぶす
    screen.fill(pg.Color("WHITE")) 

    player_x += move         # プレイヤーのx座標
    if player_x > 800:
        player_x = 800
        move = move * -1
        player = pg.transform.flip(player, False, False)
    if player_x < 0:
        player_x = 0
        player = pg.transform.flip(player, True, False)
        move = move * -1

    player_rect = pg.rect.Rect(player_x, player_y, player_h, player_w)
    # 画像を描画
    screen.blit(player, player_rect)

    # 画面を更新
    pg.display.update()

    # イベントをチェック
    for event in pg.event.get():
        # 閉じるボタンが押されたら終了
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
