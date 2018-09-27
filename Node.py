from math import inf


class Node:

    def __init__(self, weight, isStartNode, isEndNode):
        self.weight = weight
        self.isStartNode = isStartNode
        self.isEndNode = isEndNode
        self.costSoFar = inf 
        self.cameFrom = None
        self.priority = inf
 
    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def getNeighbours(self):
        x = self.x
        y = self.y
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

    def __cmp__(self, other):
        return(self.priority < other.priority)
    
    def __lt__(self, other):
        return self.priority < other.priority


    def __repr__(self):
        return str(self.__dict__)
