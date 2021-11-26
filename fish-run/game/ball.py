from game.actor import Actor
from game import constants
class Ball(Actor):
    def __init__(self):
        super().__init__()
        self._width = constants.BALL_WIDTH
        self._height = constants.BALL_HEIGHT
        self._image = constants.IMAGE_BALL