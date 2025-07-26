from agents import *
from environments import *

class Park(Environment):
    def percept(self, agent):
        ##############################################################################
        # TODO: return a list of things that are in our agent's location (our solution
        #  is 2 lines of code, but don't worry if you deviate from this)
        ##############################################################################
        #                            BEGIN OF YOUR CODE                              #
        ##############################################################################
        super().list_things_at(agent.location)
        ##############################################################################
        #                             END OF YOUR CODE                               #
        ##############################################################################

    def execute_action(self, agent, action):
        ##############################################################################
        # TODO: changes the state of the environment based on what the agent does.
        #  (our solution is 15 lines of code, but don't worry if you deviate from this)
        ##############################################################################
        #                            BEGIN OF YOUR CODE                              #
        ##############################################################################
        if action == "move down":
            print("BlindDog decided to move down at location: ", agent.location)
            agent.move_down()
        elif action == "eat":
            print("BlindDog ate Food at location: ", agent.location)
        elif action == "drink":
            print("BlindDog drank Water at location: ", agent.location)

        ##############################################################################
        #                             END OF YOUR CODE                               #
        ##############################################################################

    def is_done(self):
        ##############################################################################
        # TODO: By default, we're done when we can't find a live agent, but to prevent
        #  killing our cute dog, we will stop before itself - when there is no more
        #  food or water. (our solution is 3 lines of code, but don't worry if you
        #  deviate from this)
        ##############################################################################
        #                            BEGIN OF YOUR CODE                              #
        ##############################################################################
        pass
        ##############################################################################
        #                             END OF YOUR CODE                               #
        ##############################################################################


class Park2D(GraphicEnvironment):
    def percept(self, agent):
        ##############################################################################
        # TODO: return a list of things that are in our agent's location (our solution
        #  is 2 lines of code, but don't worry if you deviate from this)
        ##############################################################################
        #                            BEGIN OF YOUR CODE                              #
        ##############################################################################
        pass
        ##############################################################################
        #                             END OF YOUR CODE                               #
        ##############################################################################

    def execute_action(self, agent, action):
        ##############################################################################
        # TODO: changes the state of the environment based on what the agent does.
        #  (our solution is 15 lines of code, but don't worry if you deviate from this)
        ##############################################################################
        #                            BEGIN OF YOUR CODE                              #
        ##############################################################################
        pass
        ##############################################################################
        #                             END OF YOUR CODE                               #
        ##############################################################################

    def is_done(self):
        ##############################################################################
        # TODO: By default, we're done when we can't find a live agent, but to prevent
        #  killing our cute dog, we will stop before itself - when there is no more
        #  food or water. (our solution is 3 lines of code, but don't worry if you
        #  deviate from this)
        ##############################################################################
        #                            BEGIN OF YOUR CODE                              #
        ##############################################################################
        pass
        ##############################################################################
        #                             END OF YOUR CODE                               #
        ##############################################################################