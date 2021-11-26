from game.actor import Actor
from game import constants
class Fish(Actor):
    def __init__(self):
        super().__init__()
        self._width = constants.FISH_WIDTH
        self._height = constants.FISH_HEIGHT
        self._image = constants.IMAGE_FISH