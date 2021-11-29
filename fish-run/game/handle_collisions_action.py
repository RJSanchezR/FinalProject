from time import sleep
from game.point import Point
from game import constants
from game.action import Action
from game.audio_service import AudioService

class HandleCollisionsAction(Action):

    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        fish = cast["fish"][0]
        hooks = cast["hooks"]
        lives = cast["lives"]

        for hook in hooks:
            if self._physics_service.is_collision(fish, hook):
                
                fish.set_position(Point((constants.MAX_X / 2) - 40, (constants.MAX_Y / 2) + 50))

                audio_service = AudioService()
                audio_service.play_sound(constants.SOUND_BOUNCE)

                for life in lives:
                    cast["lives"].remove(life)