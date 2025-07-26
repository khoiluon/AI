from ucs import best_search

def euclidean_distance(A, B):
    return sum((a-b) for (a, b) in zip(A, B))**0.5


def greedy_search(problem, h=None):
    h = h or problem.h
    return best_search(problem, fun=h)