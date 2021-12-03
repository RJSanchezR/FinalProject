import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 30

GRAVITY = 1

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_HOOK = os.path.join(os.getcwd(), "./fish-run/assets/hook.png")
IMAGE_FISH = os.path.join(os.getcwd(), "./fish-run/assets/60x50.png")
IMAGE_LIFE = os.path.join(os.getcwd(), "./fish-run/assets/ball.png")
IMAGE_GAME_OVER = os.path.join(os.getcwd(), "./fish-run/assets/game_over.png")
IMAGE_BACKGROUND = os.path.join(os.getcwd(), "./fish-run/assets/background.png")
IMAGE_BACKGROUND1 = os.path.join(os.getcwd(), "./fish-run/assets/background-bottom.png")

SOUND_START = os.path.join(os.getcwd(), "./fish-run/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./fish-run/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./fish-run/assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX * -1

FISH_X = MAX_X / 2
FISH_Y = MAX_Y - 25

HOOK_WIDTH = 50
HOOK_HEIGHT = 300

HOOK_SPACE = 1

FISH_SPEED = 1

FISH_WIDTH = 96
FISH_HEIGHT = 78

LIFE_WIDTH = 24
LIFE_HEIGHT = 24

GAME_OVER_WIDTH = 236
GAME_OVER_HEIGHT = 236

BACKGROUND_WIDTH = 800
BACKGROUND_HEIGHT = 600

BACKGROUND1_WIDTH = 800
BACKGROUND1_HEIGHT = 200
