from parks import *

class BlindDog(Agent):
    location = 1

    def movedown(self):
        ##############################################################################
        # TODO: increase location (our solution is 1 line of code, but don't worry if
        #  you deviate from this)
        ##############################################################################
        #                            BEGIN OF YOUR CODE                              #
        ##############################################################################
        self.location += 1
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
        return isinstance(Thing, Food)
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
        return isinstance(Thing, Water)
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
    ##############################################################################
    #                            BEGIN OF YOUR CODE                              #
    ##############################################################################
    park = Park()
    dog = BlindDog(program)
    dogfood = Food()
    water = Water()

    park.add_thing(dog, 1)
    park.add_thing(dogfood, 5)
    park.add_thing(water, 7)

    park.run(10)

    ##############################################################################
    #                             END OF YOUR CODE                               #
    ##############################################################################
