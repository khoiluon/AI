from problems import Puzzle
from trees import path_states
from utils import *
from astar import *


if __name__ == "__main__":
    initial = (1,4,2,0,7,5,3,6,8)
    goal = (0,1,2,3,4,5,6,7,8)

    puzzle_problem = Puzzle(initial= initial, goal= goal)


    for s in path_states(astar_search(puzzle_problem)):
        print(board8(s))

