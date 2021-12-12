import random
from game import constants
from game.point import Point
from game.actor import Actor

class Hook(Actor):
    def __init__(self):
        super().__init__()

    def create_hook(self):

        hooks = {constants.IMAGE_HOOK_150:constants.IMAGE_WEED_300, constants.IMAGE_HOOK_200:constants.IMAGE_WEED_250, constants.IMAGE_HOOK_200:constants.IMAGE_WEED_200, constants.IMAGE_HOOK_300:constants.IMAGE_WEED_150}                                                                         
        image1, image2 = random.choice(list(hooks.items()))

        hook = Hook()

        if image1 == constants.IMAGE_HOOK_150:

            hook.set_image(constants.IMAGE_HOOK_150)
            hook.set_position(Point((constants.MAX_X - 100), 0))
            hook.set_velocity(Point(-1, 0))
            hook.set_width(constants.HOOK_150_WIDTH)
            hook.set_height(constants.HOOK_150_HEIGHT)
            hook.set_gravity(False)

        elif image1 == constants.IMAGE_HOOK_200:

            hook.set_image(constants.IMAGE_HOOK_200)
            hook.set_position(Point((constants.MAX_X - 100), 0))
            hook.set_velocity(Point(-1, 0))
            hook.set_width(constants.HOOK_200_WIDTH)
            hook.set_height(constants.HOOK_200_HEIGHT)
            hook.set_gravity(False)

        if image1 == constants.IMAGE_HOOK_250:

            hook.set_image(constants.IMAGE_HOOK_250)
            hook.set_position(Point((constants.MAX_X - 100), 0))
            hook.set_velocity(Point(-1, 0))
            hook.set_width(constants.HOOK_250_WIDTH)
            hook.set_height(constants.HOOK_250_HEIGHT)
            hook.set_gravity(False)

        if image1 == constants.IMAGE_HOOK_300:

            hook.set_image(constants.IMAGE_HOOK_300)
            hook.set_position(Point((constants.MAX_X - 100), 0))
            hook.set_velocity(Point(-1, 0))
            hook.set_width(constants.HOOK_300_WIDTH)
            hook.set_height(constants.HOOK_300_HEIGHT)
            hook.set_gravity(False)

        weed = Hook()

        if image1 == constants.IMAGE_HOOK_150:

            weed.set_image(constants.IMAGE_WEED_300)
            weed.set_position(Point((constants.MAX_X - 100), (constants.MAX_Y - constants.WEED_300_HEIGHT)))
            weed.set_velocity(Point(-1, 0))
            weed.set_width(constants.WEED_300_WIDTH)
            weed.set_height(constants.WEED_300_HEIGHT)
            weed.set_gravity(False)

        elif image1 == constants.IMAGE_HOOK_200:

            weed.set_image(constants.IMAGE_WEED_250)
            weed.set_position(Point((constants.MAX_X - 100), (constants.MAX_Y - constants.WEED_250_HEIGHT)))
            weed.set_velocity(Point(-1, 0))
            weed.set_width(constants.WEED_250_WIDTH)
            weed.set_height(constants.WEED_250_HEIGHT)
            weed.set_gravity(False)

        elif image1 == constants.IMAGE_HOOK_250:

            weed.set_image(constants.IMAGE_WEED_200)
            weed.set_position(Point((constants.MAX_X - 100), (constants.MAX_Y - constants.WEED_200_HEIGHT)))
            weed.set_velocity(Point(-1, 0))
            weed.set_width(constants.WEED_200_WIDTH)
            weed.set_height(constants.WEED_200_HEIGHT)
            weed.set_gravity(False)

        elif image1 == constants.IMAGE_HOOK_300:

            weed.set_image(constants.IMAGE_WEED_150)
            weed.set_position(Point((constants.MAX_X - 100), (constants.MAX_Y - constants.WEED_150_HEIGHT)))
            weed.set_velocity(Point(-1, 0))
            weed.set_width(constants.WEED_150_WIDTH)
            weed.set_height(constants.WEED_150_HEIGHT)
            weed.set_gravity(False)


        return hook,weed
