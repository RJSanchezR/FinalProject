from time import sleep
from game.point import Point
from game import constants
from game.action import Action
from game.audio_service import AudioService
from game.hook import Hook
from game.score import ScoreBoard

class HandleOffScreenAction(Action):

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        fish = cast["fish"][0]
        lives = cast["lives"]
        hooks = cast["hooks"]
        score = cast["score"][0]

        i = 0
        
        for obstacle in hooks:
            if i % 2 == 0:

                if fish.get_position().get_x() == obstacle.get_right_edge():
                    score.add_points(1)

                if obstacle.get_position().get_x() == constants.MAX_X / 2:
                    hook = Hook()
                    cast["hooks"].extend(hook.create_hook())

            if obstacle.get_position().get_x() <= 5:
                cast["hooks"].remove(obstacle)

            i += 1

        # Limits of the screen
        if fish.get_position().get_x() >= constants.MAX_X - 96:
            fish.set_position(Point(constants.MAX_X - 96, fish.get_position().get_y()))

        if fish.get_position().get_x() <= 5:
            fish.set_position(Point(10, fish.get_position().get_y()))
        

        

        # Limit on the bottom and losing a life condition
        for life in lives:
            if fish.get_position().is_bottom():
                
                cast["lives"].remove(life)