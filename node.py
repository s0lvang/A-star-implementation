from math import inf


class Node:

    def __init__(self, weight, is_start_node, is_end_node):
        self.weight = weight
        self.is_start_node = is_start_node
        self.is_end_node = is_end_node
        self.cost_so_far = inf
        self.came_from = None
        self.priority = inf
        
    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_neighbours(self):
        x = self.x
        y = self.y
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def __cmp__(self, other):
        return self.priority < other.priority
    
    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return str(self.__dict__)
