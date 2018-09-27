from Node import Node
from math import inf

start_node = None
end_node = None

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


def generate_value(element):
    if element == 'A':
        global start_node
        this_node = Node(1, True, False)
        start_node = this_node
    elif element == 'B':
        global end_node
        this_node = Node(1, False, True)
        end_node = this_node
    else:
        this_node = Node(values.get(element, 1), False, False)
    node_list.append(this_node.weight)
    return this_node


def make_board(filename):
    with open(filename) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = list(lines[i].strip())
        for j in range(len(lines[i])):
            lines[i][j] = generate_value(lines[i][j])
            lines[i][j].set_position(i, j)
    return lines, start_node, end_node
