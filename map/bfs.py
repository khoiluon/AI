import math
from collections import deque

def breadth_first_search(problem):
    print("Result BFS:")
    queue = deque([problem.initial])
    exlpored = [problem.initial]
    while queue:
        v = queue.popleft()
        print(v)
        if problem.is_goal(v):
            print("-----------")
            return
        for e in problem.actions(v):
            if(e not in exlpored):
                exlpored.append(e)
                queue.append(e)
