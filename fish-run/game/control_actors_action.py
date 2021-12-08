from game import constants
from game.action import Action
from game.point import Point

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # direction = self._input_service.get_direction()
        # direction = direction.scale(constants.FISH_SPEED)
        # fish = cast["fish"][0]
        # dx = fish.get_velocity().get_x()
        # dy = fish.get_velocity().get_y()


        # dx = dx + direction.get_x()
        # dy = dy + direction.get_y()

        # fish.set_velocity(Point(dx, dy))

        direction = self._input_service.get_direction()
        fish = cast["fish"][0] # there's only one in the cast
        fish.set_velocity(direction.scale(constants.FISH_SPEED))   