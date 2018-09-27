from Node import Node
from math import inf

startNode = None
endNode = None


def generateValue(element):
    if(element == '#'):
        return Node(inf, False, False)
    elif (element == '.'):
        return Node(1, False, False)
    elif (element == 'A'):
        global startNode
        startNode = Node(0, True, False)
        return startNode
    elif(element == 'B'):
        global endNode
        endNode = Node(0, False, True)
        return endNode
    return Node(element, False, False)


def makeBoard(filename):
    with open(filename) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = list(lines[i].strip())
        for j in range(len(lines[i])):
            lines[i][j] = generateValue(lines[i][j])
            lines[i][j].setPosition(i, j)
    return lines, startNode, endNode

makeBoard("boards/board-2-1.txt")

