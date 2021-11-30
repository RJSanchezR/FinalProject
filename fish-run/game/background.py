from game.actor import Actor
from game import constants
class Background(Actor):
    def __init__(self):
        super().__init__()
        self._width = constants.BACKGROUND_WIDTH
        self._height = constants.BACKGROUND_HEIGHT
        self._image = constants.IMAGE_BACKGROUND