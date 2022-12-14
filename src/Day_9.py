from collections import namedtuple

from utils import read_file
from typing import NamedTuple

values = read_file(9, str, False)


class Step(NamedTuple):
    direction: str
    distance: int


class Position:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def change_x(self, val):
        self.x += val

    def change_y(self, val):
        self.y += val

    def set_x(self, val):
        self.x = val

    def set_y(self, val):
        self.y = val

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f'({self.x}, {self.y})'
def next_too(_head, _tail):
    return abs(_head.x - _tail.x) <= 1 and abs(_head.y - _tail.y) <= 1


steps = []

for value in values:
    line = value.split()
    steps.append(Step(line[0], int(line[1])))

head = Position(0, 0)
tail = Position(0, 0)
tail_visited = set()

for step in steps:
    for i in range(step.distance):
        match step.direction:
            case 'U':
                head.change_y(1)
                if not next_too(head, tail):
                    tail.set_x(head.x)
                    tail.change_y(1)
            case 'D':
                head.change_y(-1)
                if not next_too(head, tail):
                    tail.set_x(head.x)
                    tail.change_y(-1)
            case 'L':
                head.change_x(-1)
                if not next_too(head, tail):
                    tail.set_y(head.y)
                    tail.change_x(-1)
            case 'R':
                head.change_x(1)
                if not next_too(head, tail):
                    tail.set_y(head.y)
                    tail.change_x(1)
        tail_visited.add(Position(tail.x, tail.y))

print(f'Part 1: {len(tail_visited)}')
# Part 1: 6354
