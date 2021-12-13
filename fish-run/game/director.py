from time import sleep
from game import constants
from game.point import Point
from game.audio_service import AudioService
from game.output_service import OutputService
import raylibpy

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
    """

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        self._keep_playing = True
        
    def start_game(self, cast, script):
        """Starts the game loop to control the sequence of play."""
        while self._keep_playing:
            
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")

            game_over = cast["game_over"][0]
            hooks = cast["hooks"]
            fish = cast["fish"][0]
            # control = script["input"][0]

            
            if len(self._cast["lives"]) == 0:

                script["input"] = []

                # Game over screen
                game_over.set_image(constants.IMAGE_GAME_OVER)
                
                # Stop actors
                for hook in hooks:
                    hook.set_velocity(Point(0,0))

                fish.set_velocity(Point(0, 1))


                # Option to clear screen
                # for hook in hooks:
                    # cast["hooks"].remove(hook)
                # fish.set_image(" ")

            if raylibpy.window_should_close():
                self._keep_playing = False


    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)