import math
from collections import deque

def deep_first_search(problem):
    print("Result DFS:")
    stack = deque([problem.initial])
    exlpored = []
    while stack:
        current = stack.pop()
        if (current not in exlpored):
            print(current)
            exlpored.append(current)
            for e in problem.actions(current):
                stack.append(e)


