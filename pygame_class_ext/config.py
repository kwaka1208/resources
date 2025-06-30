# =================================================================
# 1. config.py
# ゲーム全体の設定を保存するファイルです。
# =================================================================
# ファイル名: config.py

# 画面設定
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "SHOOTING GAME (Class)"
START_TITLE = "PRESS 's' TO START"
FPS = 60

# プレイヤー設定
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 5

# 弾の設定
BULLET_WIDTH = 15
BULLET_HEIGHT = 15
BULLET_SPEED = 10

# 敵の設定
ENEMY_WIDTH = 20
ENEMY_HEIGHT = 20
ENEMY_SPEED = 3
ENEMY_SPAWN_RATE = 100 # 敵が生成される間隔（小さいほど頻繁）
ENEMY_COUNT = 10

# 画面の色
STAGE_COLOR = (135, 206, 250)  # 白
FORE_COLOR = (0, 0, 0)  # 黒