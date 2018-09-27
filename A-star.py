from boardReader import makeBoard
from heapq import heappush, heappop


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def aStar(board, start):
    heap = []
    heappush(heap, start)

    while(heap):
        current = heappop(heap)

        if(current.isEndNode):
            break
        for x, y in current.neighbours:
            try:
                next = board[x][y]
            except(IndexError):
                continue
            
    


def main(filename):
    board, startNode = makeBoard(filename)
    aStar(board, startNode)

main('boards/board-1-1.txt')