import heapq

class PriorityQueue:
    def __init__(self, list=(), key=lambda x:x):
        self.key = key
        self.nodes = []

        for node in list:
            self.add(node)

    def add(self, node):
        pair = (self.key(node), node)
        heapq.heappush(self.nodes, pair)

    def pop(self):
        return heapq.heappop(self.nodes)[1]

def board8(board, my_format = (3* '{} {} {}\n')):
    return my_format.format(*board).replace('0', '_')