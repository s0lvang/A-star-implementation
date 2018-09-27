from boardReader import make_board
from heapq import heappush, heappop


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(board, start, end_node):
    heap = []
    heappush(heap, start)
    start.cost_so_far = 0

    while heap:
        current = heappop(heap)

        if current.is_end_node:
            break
        for x, y in current.get_neighbours():
            try:
                if x < 0 or y < 0:
                    raise IndexError
                next = board[x][y]
                new_cost = current.cost_so_far + next.weight
                if new_cost < next.cost_so_far:
                    next.cost_so_far = new_cost
                    next.priority = new_cost + heuristic((x, y), (end_node.x, end_node.y))
                    next.came_from = current
                    heappush(heap, next)
            except IndexError:
                continue
    return current


def main(filename):
    board, start_node, end_node = make_board(filename)
    end_node = a_star(board, start_node, end_node)
    while end_node:
        path.append((end_node.x, end_node.y))
        end_node = end_node.came_from


def get_path():
    return path


path = []
