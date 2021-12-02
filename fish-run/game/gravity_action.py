from game.point import Point
from game.action import Action
from game import constants


class GravityAction(Action):

    def execute(self, cast):

        for group in cast.values():        
            for actor in group:
                if actor.get_gravity():
                    
                    dx = actor.get_velocity().get_x()
                    dy = actor.get_velocity().get_y() + constants.GRAVITY

                    actor.set_velocity(Point(dx, dy))           
        