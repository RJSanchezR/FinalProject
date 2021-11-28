import os
os.environ['RAYLIB_BIN_PATH'] = '.'

import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.draw_actors_action import DrawActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService

# TODO: Add imports similar to the following when you create these classes
from game.brick import Brick
from game.ball import Ball
from game.fish import Fish
from game.lives import Lives
from game.game_over import GameOver
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    # create the cast {key: tag, value: list}
    cast = {}
    
    # cast["bricks"] = []
    # for x in range(55, 700, 55):
    #     for y in range(60, 180, 30):
    #         brick = Brick()
    #         brick.set_image(constants.IMAGE_BRICK)
    #         brick.set_position(Point(x, y))
    #         brick.set_velocity(Point(2, 0))
    #         brick.set_width(constants.BRICK_WIDTH)
    #         brick.set_height(constants.BRICK_HEIGHT)
    #         cast["bricks"].append(brick)

    cast["bricks"] = []
    bricks = []
    num = 0
    x = 0
    y = 0

    for brick in range(0, 112):
        brick = Brick()
        num += 1
        if x > 800:
            x = 1
            y += 40
            # brick.set_velocity(Point(-2,0))
        if x < 200 and (y == 20 or 60 or 100 or 140):
            brick.set_image(constants.IMAGE_BRICK)
            brick.set_velocity(Point(-2,0))
        if x > 200 or y ==180:
            brick.set_image(constants.IMAGE_BRICK_1)
            brick.set_velocity(Point(-2,0))
        if y ==60 and x > 200:
            brick.set_image(constants.IMAGE_BRICK)
            brick.set_velocity(Point(-2,0))
        if y ==140:
            brick.set_image(constants.IMAGE_BRICK_1)
            brick.set_velocity(Point(-2,0))
        if y ==220:
            brick.set_image(constants.IMAGE_BRICK)
            brick.set_velocity(Point(-2,0))
        if y ==260:
            brick.set_image(constants.IMAGE_BRICK_1)
        brick.set_position(Point(x, y))
        x += 50
        bricks.append(brick)
    cast["bricks"] = bricks


    cast["balls"] = []
    ball = Ball()
    ball.set_position(Point(constants.MAX_X / 2, constants.MAX_Y / 2))
    ball.set_velocity(Point(3, -3))
    cast["balls"].append(ball)

    cast["fish"] = []
    fish = Fish()
    fish.set_position(Point(constants.MAX_X / 2, constants.MAX_Y - 40))
    cast["fish"].append(fish)

    cast["lives"] = []
    axis_y = constants.MAX_Y - 90
    for x in range(1, 2):
        for y in range(1, 4):
            life = Lives()
            life.set_image(constants.IMAGE_BALL)
            life.set_position(Point(1, axis_y))
            life.set_width(constants.BALL_WIDTH)
            life.set_height(constants.BALL_HEIGHT)
            cast["lives"].append(life)
            axis_y = axis_y + 30

    cast["game_over"] = []
    game_over = GameOver()
    game_over.set_position(Point(282, 182))
    cast["game_over"].append(game_over)


    # The script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    draw_actors_action = DrawActorsAction(output_service)
    move_actors_action = MoveActorsAction()
    handle_off_screen_action = HandleOffScreenAction()
    control_actors_action = ControlActorsAction(input_service)
    handle_collisions_action = HandleCollisionsAction(physics_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action]
    script["output"] = [draw_actors_action]


    # Start the game
    output_service.open_window("Batter")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game(cast)

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
