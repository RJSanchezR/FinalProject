import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 120

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_BRICK = os.path.join(os.getcwd(), "./fish-run/assets/brick-2.png")
IMAGE_FISH = os.path.join(os.getcwd(), "./fish-run/assets/60x50.png")
IMAGE_BALL = os.path.join(os.getcwd(), "./fish-run/assets/ball.png")
IMAGE_GAME_OVER = os.path.join(os.getcwd(), "./fish-run/assets/game_over_yellow.png")

SOUND_START = os.path.join(os.getcwd(), "./fish-run/assets/start.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./fish-run/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./fish-run/assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX * -1

FISH_X = MAX_X / 2
FISH_Y = MAX_Y - 25

BRICK_WIDTH = 48
BRICK_HEIGHT = 24

BRICK_SPACE = 5

FISH_SPEED = 15

FISH_WIDTH = 96
FISH_HEIGHT = 78

BALL_WIDTH = 24
BALL_HEIGHT = 24

GAME_OVER_WIDTH = 236
GAME_OVER_HEIGHT = 236
