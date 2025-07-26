from problems import Problem
from ucs import best_search

def astar_search(problem, f=None):
    f = f or (lambda node: node.path_cost + problem.h(node))
    return best_search(problem, f)