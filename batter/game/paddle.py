from game.actor import Actor
from game import constants
class Paddle(Actor):
    def __init__(self):
        super().__init__()
        self._width = constants.PADDLE_WIDTH
        self._height = constants.PADDLE_HEIGHT
        self._image = constants.IMAGE_PADDLE