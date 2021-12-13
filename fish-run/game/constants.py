import os

MAX_X = 800
MAX_Y = 600
FRAME_RATE = 120

GRAVITY = 1

DEFAULT_SQUARE_SIZE = 20
DEFAULT_FONT_SIZE = 20
DEFAULT_TEXT_OFFSET = 4

IMAGE_HOOK_300 = os.path.join(os.getcwd(), "./fish-run/assets/hook-300.png")
IMAGE_HOOK_250 = os.path.join(os.getcwd(), "./fish-run/assets/hook-250.png")
IMAGE_HOOK_200 = os.path.join(os.getcwd(), "./fish-run/assets/hook-200.png")
IMAGE_HOOK_150 = os.path.join(os.getcwd(), "./fish-run/assets/hook-150.png")
IMAGE_WEED_300 = os.path.join(os.getcwd(), "./fish-run/assets/weed-300.png")
IMAGE_WEED_250 = os.path.join(os.getcwd(), "./fish-run/assets/weed-250.png")
IMAGE_WEED_200 = os.path.join(os.getcwd(), "./fish-run/assets/weed-200.png")
IMAGE_WEED_150 = os.path.join(os.getcwd(), "./fish-run/assets/weed-150.png")
IMAGE_FISH = os.path.join(os.getcwd(), "./fish-run/assets/fish.png")
IMAGE_LIFE = os.path.join(os.getcwd(), "./fish-run/assets/ball.png")
IMAGE_GAME_OVER = os.path.join(os.getcwd(), "./fish-run/assets/game_over.png")
IMAGE_BACKGROUND = os.path.join(os.getcwd(), "./fish-run/assets/background.png")

SOUND_START = os.path.join(os.getcwd(), "./fish-run/assets/background-music.wav")
SOUND_BOUNCE = os.path.join(os.getcwd(), "./fish-run/assets/boing.wav")
SOUND_OVER = os.path.join(os.getcwd(), "./fish-run/assets/over.wav")

BALL_X = MAX_X / 2
BALL_Y = MAX_Y - 125

BALL_DX = 8
BALL_DY = BALL_DX * -1

FISH_X = MAX_X / 2
FISH_Y = MAX_Y - 25

HOOK_300_WIDTH = 80
HOOK_300_HEIGHT = 300
HOOK_250_WIDTH = 72
HOOK_250_HEIGHT = 250
HOOK_200_WIDTH = 69
HOOK_200_HEIGHT = 200
HOOK_150_WIDTH = 100
HOOK_150_HEIGHT = 150

WEED_300_WIDTH = 80
WEED_300_HEIGHT = 300
WEED_250_WIDTH = 80
WEED_250_HEIGHT = 250
WEED_200_WIDTH = 80
WEED_200_HEIGHT = 200
WEED_150_WIDTH = 80
WEED_150_HEIGHT = 150

HOOK_SPACE = 1

FISH_SPEED = 5

FISH_WIDTH = 86
FISH_HEIGHT = 68

LIFE_WIDTH = 24
LIFE_HEIGHT = 24

GAME_OVER_WIDTH = 236
GAME_OVER_HEIGHT = 236

BACKGROUND_WIDTH = 800
BACKGROUND_HEIGHT = 600
