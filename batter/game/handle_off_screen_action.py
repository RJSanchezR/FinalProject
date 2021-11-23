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
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        lives = cast["lives"]

        if ball.get_position().over_side_wall():
            ball.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))
        
        if ball.get_position().is_top():
            ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))
        
        for life in lives:
            if ball.get_position().is_bottom():
                
                # Set the "new" ball at the starting position
                ball.set_position(Point(constants.MAX_X / 2, constants.MAX_Y - 80))
                ball.set_velocity(Point(3, -3))
                
                audio_service = AudioService()
                audio_service.play_sound(constants.SOUND_OVER)
                
                cast["lives"].remove(life)