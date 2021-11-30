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
from game.hook import Hook
from game.fish import Fish
from game.lives import Lives
from game.game_over import GameOver
from game.background import Background
from game.control_actors_action import ControlActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction
from game.move_actors_action import MoveActorsAction

def main():

    # Create the cast {key: tag, value: list}
    cast = {}

    cast["background"] = []

    background = Background()
    background.set_position(Point(1, 1))
    cast["background"].append(background)

    cast["hooks"] = []

    x = constants.MAX_X - 50
    y = 1

    for hook in range(0, 200):
        hook = Hook()
        hook.set_image(constants.IMAGE_HOOK)
        hook.set_position(Point(x, y))
        hook.set_velocity(Point(-1,0))
        hook.set_width(constants.HOOK_WIDTH)
        hook.set_height(constants.HOOK_HEIGHT)
        cast["hooks"].append(hook)

    cast["fish"] = []

    fish = Fish()
    fish.set_position(Point((constants.MAX_X / 2) - 40, (constants.MAX_Y / 2) + 50))
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
    output_service.open_window("Fish Run")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game(cast)

    audio_service.stop_audio()

if __name__ == "__main__":
    main()
