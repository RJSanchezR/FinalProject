from game import brick
from game.point import Point
from game import constants
from game.action import Action
from game.audio_service import AudioService

class HandleCollisionsAction(Action):
    def __init__(self, physics_service):
        super().__init__()
        self._physics_service = physics_service

    def execute(self, cast):
        ball = cast["balls"][0]
        paddle = cast["paddle"][0]
        bricks = cast["bricks"]

        if self._physics_service.is_collision(ball, paddle):
            ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1))

            audio_service = AudioService()
            audio_service.play_sound(constants.SOUND_BOUNCE)

        for brick in bricks:
            if self._physics_service.is_collision(ball, brick):
                ball.set_velocity(Point(ball.get_velocity().get_x(), ball.get_velocity().get_y() * -1)) 

                audio_service = AudioService()
                audio_service.play_sound(constants.SOUND_BOUNCE)

                cast["bricks"].remove(brick)