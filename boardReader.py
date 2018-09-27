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

node_list = []


def get_node_list():
    return node_list


def generateValue(element):
    if (element == 'A'):
        global startNode
        this_node = Node(1, True, False)
        startNode = this_node
    elif(element == 'B'):
        global endNode
        this_node = Node(1, False, True)
        endNode = this_node
    else:
        this_node = Node(values.get(element, 1), False, False)
    node_list.append(this_node.weight)
    return this_node


def makeBoard(filename):
    with open(filename) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = list(lines[i].strip())
        for j in range(len(lines[i])):
            lines[i][j] = generateValue(lines[i][j])
            lines[i][j].setPosition(i, j)
    return lines, startNode, endNode
