from boardReader import makeBoard
from heapq import heappush, heappop


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def aStar(board, start, endNode):
    heap = []
    heappush(heap, start)
    start.costSoFar = 0

    while(heap):
        current = heappop(heap)

        if(current.isEndNode):
            break
        for x, y in current.getNeighbours():
            try:
                next = board[x][y]
                new_cost = current.costSoFar + next.weight
                if(new_cost < next.costSoFar):
                    next.costSoFar = new_cost
                    # Remember to put end node as second parameter
                    next.priority = new_cost + heuristic((x, y), (endNode.x, endNode.y)) 
                    heappush(heap, next)
                    next.cameFrom = current
            except(IndexError):
                continue
    return current


def main(filename):
    board, startNode, endNode = makeBoard(filename)
    endNode = aStar(board, startNode, endNode)
    while(True):
        print(endNode.x, endNode.y)
        endNode = endNode.cameFrom

main('boards/board-1-1.txt')