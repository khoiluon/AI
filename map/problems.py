
from greedy import euclidean_distance

class Problem(object):
    def __init__(self, initial = None, goal = None, **kwargs):
        self.__dict__.update(initial = initial, goal = goal, **kwargs)

    def actions(self, state):
        raise NotImplementedError

    def result(self, state, action):
        raise NotImplementedError

    def is_goal(self, state):
        return state == self.goal

    def action_cost(self, s, state, s1):
        return 1
    def h(self, node):
        return 0

class RouteProblem(Problem):
    def actions(self, state):
        return self.map.neighbors[state]

    def result(self, state, action):
        return action if action in self.map.neighbors[state] else state
    def action_cost(self, s, action, s1):
        return self.map.distances[s, s1]


class Puzzle(Problem):
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        moves = (
            (1,3), (0,2,4), (1,5),
            (0,4,6), (1,3,5,7), (2,4,8),
            (3,7), (6,4,8), (7,5)
        )
        blank = state.index(0)
        return moves[blank]

    def result(self, state, action):
        s = list(state)
        blank = state.index(0)
        s[action], s[blank] = s[blank], s[action]
        return tuple(s)

    def h(self, node):
        X = (0,1,2,
             0,1,2,
             0,1,2)

        Y = (0,0,0,
             1,1,1,
             2,2,2,)

        return sum(abs(X[s]-X[g])+ abs(Y[s]-Y[g])
        for(s,g) in zip(node.state, self.goal) if s != 0)







