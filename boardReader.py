from Node import Node
from math import inf

startNode = None
endNode = None

values = {
    "#": inf,
    ".": 1,
    "w": 100,
    "m": 50,
    "f": 10,
    "g": 5,
    "r": 1,
}


def generateValue(element):
    if (element == 'A'):
        global startNode
        startNode = Node(1, True, False)
        return startNode
    elif(element == 'B'):
        global endNode
        endNode = Node(1, False, True)
        return endNode
    return Node(values.get(element, 1), False, False)


def makeBoard(filename):
    with open(filename) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = list(lines[i].strip())
        for j in range(len(lines[i])):
            lines[i][j] = generateValue(lines[i][j])
            lines[i][j].setPosition(i, j)
    return lines, startNode, endNode
