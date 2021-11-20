from game.point import Point
from game import constants
from game.action import Action

class HandleOffScreenAction(Action):

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]

        if ball.get_position().equals_side_wall():
            ball.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))
        
        if ball.get_position().is_top():
            ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))
        
        if ball.get_position().is_bottom():
            cast["balls"].remove(ball)
        
        # if paddle.get_position().equals_side_wall():
        #     paddle.set_velocity(Point(ball.get_velocity().get_x() * -1, ball.get_velocity().get_y()))