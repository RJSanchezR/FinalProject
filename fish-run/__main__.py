import os
os.environ['RAYLIB_BIN_PATH'] = '.'

import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.input_service import InputService
from game.output_service import OutputService
from game.physics_service import PhysicsService
from game.audio_service import AudioService
from game.background import Background
from game.hook import Hook
from game.fish import Fish
from game.lives import Lives
from game.score import ScoreBoard
from game.game_over import GameOver
from game.draw_actors_action import DrawActorsAction
from game.control_actors_action import ControlActorsAction
from game.move_actors_action import MoveActorsAction
from game.gravity_action import GravityAction
from game.handle_collisions_action import HandleCollisionsAction
from game.handle_off_screen_action import HandleOffScreenAction

def main():

    # Create the cast {key: tag, value: list}
    cast = {}


    cast["background"] = []

    background = Background()
    background.set_image(constants.IMAGE_BACKGROUND)
    background.set_width(constants.BACKGROUND_WIDTH)
    background.set_height(constants.BACKGROUND_HEIGHT)
    background.set_position(Point(1, 1))
    background.set_gravity(False)
    cast["background"].append(background)


    cast["hooks"] = []

    hook = Hook()
    cast["hooks"].extend(hook.create_hook())


    cast["fish"] = []

    fish = Fish()
    fish.set_position(Point((constants.MAX_X / 2) - 40, (constants.MAX_Y / 2) + 50))
    fish.set_gravity(False)
    cast["fish"].append(fish)


    cast["lives"] = []
    
    life = Lives()
    cast["lives"].append(life)

    cast["score"] = []

    score = ScoreBoard()
    cast["score"].append(score)


    cast["game_over"] = []

    game_over = GameOver()
    game_over.set_position(Point(282, 182))
    game_over.set_gravity(False)
    cast["game_over"].append(game_over)


    # The script {key: tag, value: list}
    script = {}

    input_service = InputService()
    output_service = OutputService()
    physics_service = PhysicsService()
    audio_service = AudioService()
    draw_actors_action = DrawActorsAction(output_service)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    gravity_action = GravityAction()
    handle_collisions_action = HandleCollisionsAction(physics_service)
    handle_off_screen_action = HandleOffScreenAction()

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_off_screen_action, handle_collisions_action, gravity_action]
    script["output"] = [draw_actors_action]


    # Start the game
    output_service.open_window("Fish Run")
    audio_service.start_audio()
    audio_service.play_sound(constants.SOUND_START)
    
    director = Director(cast, script)
    director.start_game(cast, script)

    # audio_service.stop_audio()

if __name__ == "__main__":
    main()
