class Node:
    
    def __init__(self,weight,isStartNode,isEndNode):
        self.weight = weight
        self.isStartNode=isStartNode
        self.isEndNode=isEndNode
    def __repr__(self):
        return str(self.weight)