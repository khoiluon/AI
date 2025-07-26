from trees import *
from utils import *


def g(n):
    return n.path_cost


def best_search(problem, fun):
    node = Node(problem.initial)
    fringe = PriorityQueue([node], key=fun)
    visited = {problem.initial: node}

    while fringe:
        node = fringe.pop()
        if problem.is_goal(node.state):
            return node
        for child in expand(problem, node):
            s = child.state
            if s not in visited:
                visited[s] = child
                fringe.add(child)
    return failure

def uniform_cost_search(problem):
    return best_search(problem, fun=g)
