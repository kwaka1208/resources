import pygame as pg
import sys

# pygame初期化
pg.init()

# 画面設定
screen = pg.display.set_mode((800, 600)) 

# >> ここから追加
# キャラクター追加
player = pg.image.load("images/ninja.png")
player = pg.transform.scale(player, (100, 100))
player = pg.transform.flip(player, True, False)
player_rect = pg.rect.Rect(0, 480, 100, 100)
# <<>> ここまで追加

while True:
    # 画面を白で塗りつぶす
    screen.fill(pg.Color("WHITE")) 

    # 赤い四角形を描画
    # pg.draw.rect(screen, pg.Color("RED"), pg.Rect(10, 20, 100, 150))

# >> ここから追加
    # キャラクターを表示
    screen.blit(player, player_rect)
# <<>> ここまで追加

    # 画面を更新
    pg.display.update()

    # イベントをチェック
    for event in pg.event.get():
        # 閉じるボタンが押されたら終了
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
