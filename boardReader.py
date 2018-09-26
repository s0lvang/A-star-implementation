from Node import Node
from math import inf


def generateValue(element):
    if(element == '#'):
        return Node(inf, False, False)
    elif (element == '.'):
        return Node(1, False, False)
    elif (element == 'A'):
        return Node(0, True, False)
    elif(element == 'B'):
        return Node(0, False, True)
    return Node(element, False, False)


def makeBoard(filename):
    board = None
    with open(filename) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = list(lines[i].strip())
        lines[i] = list(map(lambda x: generateValue(x), lines[i]))
    return lines

makeBoard("boards/board-1-1.txt")
