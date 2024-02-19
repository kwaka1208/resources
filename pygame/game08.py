import pygame as pg
import sys
import random

#
#  プレイヤーのダメージ処理
#
def player_damage(_player, _player_rect):
  # 表示の更新を10回繰り返す
  for i in range(10):
    # プレイヤーを左右反転
    _player = pg.transform.flip(_player, True, False)
    # プレイヤーキャラを展開
    screen.blit(_player, _player_rect)
    # 画面を更新
    pg.display.update()
    # 100ミリ秒待つ
    pg.time.wait(100)
    # 画面全体を塗りつぶす
    screen.fill(pg.Color("GRAY")) 

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
bullet_rect = pg.rect.Rect(0, -10, 30, 30)

# 敵追加
enemy = pg.image.load("images/enemy.png")
enemy = pg.transform.scale(enemy, (100, 100))
enemy_rect = pg.rect.Rect(random.randint(0, 800), 0, 100, 100)

# 右を向いているかどうかのフラグ
# 右向き：True 左向き：False（右向きじゃない）
fRight = True

# 弾が敵にあたったかどうかのフラグ
# 当たった：True 当たっない：False
hit = False


while True:
    # 画面を白で塗りつぶす
    screen.fill(pg.Color("GRAY")) 

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

    # fire = pg.mouse.get_pressed()
    # スペースキーが押された時に、弾が発射されていなかったら
    if key[pg.K_SPACE] and bullet_rect.y < 0:
        # 弾の初期位置を設定
        bullet_rect.x = player_rect.x + 50 - 15
        bullet_rect.y = player_rect.y
        pg.mixer.Sound("sounds/maou_se_battle17.mp3").play()
    if bullet_rect.y >= 0:
        # 弾を上に移動
        bullet_rect.y -= 10
        if bullet_rect.y > 600:
            
            # 弾が画面外に出たら、初期位置に戻す
            bullet_rect.y = -10
        screen.blit(bullet, bullet_rect)

    ## 敵の処理
    enemy_rect.y += 10

    # 敵が画面外に出たら、初期位置に戻す
    if enemy_rect.y > 600:
        if hit == True:
            # 敵が弾に当たったら、敵の向きを元に戻す
            enemy = pg.transform.flip(enemy, False, True)
            # 当たったフラグをFalseに戻す
            hit = False
        # 座標をランダムに決定
        enemy_rect.x = random.randint(0, 800)
        enemy_rect.y = 0
    # 敵の表示位置を更新
    screen.blit(enemy, enemy_rect)

    # 敵と弾の当たり判定
    if enemy_rect.colliderect(bullet_rect) and hit == False:
      enemy = pg.transform.flip(enemy, False, True)
      screen.blit(enemy, enemy_rect)
      hit = True
      bullet_rect.y = -10
      screen.blit(bullet, bullet_rect)

    # 敵とプレイヤーの当たり判定
    if enemy_rect.colliderect(player_rect):
      # 撃って落ちてきた敵とは当たらない
      if hit != True:
        # 敵キャラを画面の外に移動
        enemy_rect.y = 601
        # ダメージ表示処理を呼び出す
        player_damage(player, player_rect)
        # 繰り返し処理の先頭に戻る
        continue

    # 画面を更新
    pg.display.update()

    pg.time.Clock().tick(60)

    # イベントをチェック
    for event in pg.event.get():
        # 閉じるボタンが押されたら終了
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
