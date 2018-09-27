class Node:

    def __init__(self, weight, isStartNode, isEndNode):
        self.weight = weight
        self.isStartNode = isStartNode
        self.isEndNode = isEndNode
        self.closed = False
        self.neighbours = []

    def setNeighbours(self, neighbours):
        self.neighbours = neighbours

    def __cmp__(self, other):
        return(self.weight, other.weight)

    def __repr__(self):
        return str(self.weight)
