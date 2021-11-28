from time import sleep
from game.point import Point
from game import constants
from game.action import Action
from game.audio_service import AudioService

class HandleOffScreenAction(Action):

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # ball = cast["balls"][0]
        fish = cast["fish"][0]
        lives = cast["lives"]

        # if fish.get_position().over_side_wall():
        #     ball.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))
        
        # if ball.get_position().is_top():
        #     ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))

        # Limits of the screen side
        if fish.get_position().get_x() >= constants.MAX_X - 96:
            fish.set_position(Point(constants.MAX_X - 96, fish.get_position().get_y()))

        if fish.get_position().get_x() <= 1:
            fish.set_position(Point(10, fish.get_position().get_y()))
        
        # Limit on the bottom and losing a life condition
        for life in lives:
            if fish.get_position().is_bottom():
                
                sleep(1)
                # Set the "new" fish at the starting position
                fish.set_position(Point((constants.MAX_X / 2) - 40, (constants.MAX_Y / 2) + 50))
                
                audio_service = AudioService()
                audio_service.play_sound(constants.SOUND_START)
                
                cast["lives"].remove(life)