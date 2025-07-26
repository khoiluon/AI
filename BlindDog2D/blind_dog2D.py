from agents import *
from environments import Direction
from parks import Park2D


class BlindDog(Agent):
    location = [0 ,1] # change location to a 2d value
    direction = Direction("down") # variable to store the direction our dog is facing

    def movedown(self):
        ##############################################################################
        # TODO: increase location (our solution is 1 line of code, but don't worry if
        #  you deviate from this)
        ##############################################################################
        #                            BEGIN OF YOUR CODE                              #
        ##############################################################################
        pass
        ##############################################################################
        #                             END OF YOUR CODE                               #
        ##############################################################################

    def eat(self, thing):
        ##############################################################################
        # TODO: return True if thing is food for dog (our solution is 3 lines of code,
        #  but don't worry if you deviate from this)
        ##############################################################################
        #                            BEGIN OF YOUR CODE                              #
        ##############################################################################
        pass
        ##############################################################################
        #                             END OF YOUR CODE                               #
        ##############################################################################

    def drink(self, thing):
        ##############################################################################
        # TODO: return True if thing is water (our solution is 3 lines of code,
        #  but don't worry if you deviate from this)
        ##############################################################################
        #                            BEGIN OF YOUR CODE                              #
        ##############################################################################
        pass
        ##############################################################################
        #                             END OF YOUR CODE                               #
        ##############################################################################


def program(percepts):
    '''Returns an action based on the dog's percepts'''
    for p in percepts:
        if isinstance(p, Food):
            return 'eat'
        elif isinstance(p, Water):
            return 'drink'
    return 'move down'


if __name__ == "__main__":
    park = Park2D(5, 20, color={'BlindDog': (200, 0, 0),
                                'Water': (0, 200, 200),
                                'Food': (230, 115, 40)})  # park width is set to 5, and height to 20

    ##############################################################################
    #                            BEGIN OF YOUR CODE                              #
    ##############################################################################
    pass
    ##############################################################################
    #                             END OF YOUR CODE                               #
    ##############################################################################