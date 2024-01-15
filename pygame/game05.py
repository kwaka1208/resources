import pygame as pg
import sys

# pygame初期化
pg.init()

# 画面設定
screen = pg.display.set_mode((800, 600)) 

# キャラクター追加
player = pg.image.load("images/ninja.png")
player = pg.transform.scale(player, (100, 100))
player = pg.transform.flip(player, True, False)
player_rect = pg.rect.Rect(0, 480, 100, 100)

# 弾追加
bullet = pg.image.load("images/bullet.png")
bullet = pg.transform.scale(bullet, (30, 30))
bullet_rect = pg.rect.Rect(0, -10, 100, 100)


# 右を向いているかどうかのフラグ
# 右向き：True 左向き：False（右向きじゃない）
fRight = True

while True:
    # 画面を白で塗りつぶす
    screen.fill(pg.Color("WHITE")) 

    # キー入力の情報を取得
    key = pg.key.get_pressed()
    if(key[pg.K_RIGHT]):
        # 右向きキーが押された時、X座標を増やす
        player_rect.x += 10
        if(fRight == False):
            # 右向きでなければ、左向きから右向きに変更
            player = pg.transform.flip(player, True, False)
            fRight = True
    if(key[pg.K_LEFT]):
        # 左向きキーが押された時、X座標を減らす
        player_rect.x -= 10
        if(fRight == True):
            # 右向きなら、右向きから左向きに変更
            player = pg.transform.flip(player, True, False)
            fRight = False

    # キャラクターを表示
    screen.blit(player, player_rect)

    fire = pg.mouse.get_pressed()
    # マウスの左ボタンが押された時に、弾が発射されていなかったら
    if fire[0] and bullet_rect.y < 0:
        # 弾の初期位置を設定
        bullet_rect.x = player_rect.x + 50 - 15
        bullet_rect.y = player_rect.y
        pg.mixer.Sound("sounds/maou_se_battle17.mp3").play()
    if bullet_rect.y >= 0:
        # 弾を上に移動
        bullet_rect.y -= 10
        screen.blit(bullet, bullet_rect)

    # 画面を更新
    pg.display.update()

    pg.time.Clock().tick(60)

    # イベントをチェック
    for event in pg.event.get():
        # 閉じるボタンが押されたら終了
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
