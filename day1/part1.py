import re
from enum import Enum, auto

from read import read


class Turn(Enum):
    L = 0
    R = 1


"""
    N
W       E
    S

"""


class Rotation(Enum):
    WEST = auto()
    EAST = auto()
    NORTH = auto()
    SOUTH = auto()

    def turn(self, turn: Turn) -> 'Rotation':
        return rotation_turn[self][turn]

    @property
    def offset(self):
        return rotation_offset[self]


rotation_offset = {
    Rotation.NORTH: (0, 1),
    Rotation.SOUTH: (0, -1),
    Rotation.EAST: (1, 0),
    Rotation.WEST: (-1, 0)
}

rotation_turn = {
    Rotation.NORTH: {Turn.L: Rotation.WEST, Turn.R: Rotation.EAST},
    Rotation.SOUTH: {Turn.L: Rotation.EAST, Turn.R: Rotation.WEST},
    Rotation.EAST: {Turn.L: Rotation.NORTH, Turn.R: Rotation.SOUTH},
    Rotation.WEST: {Turn.L: Rotation.SOUTH, Turn.R: Rotation.NORTH}
}


def solve(data):
    rot = Rotation.NORTH
    seen = set()
    found_first_repeat = False
    x = y = 0
    first = 0, 0

    for turn, steps in data:
        rot = rot.turn(turn)

        for _ in range(steps):
            x += rot.offset[0]
            y += rot.offset[1]
            location = x, y

            if not found_first_repeat and location in seen:
                first = location
                found_first_repeat = True

            seen.add(location)

    print(abs(first[0]) + abs(first[1]))


def main():
    data = [(Turn[dir], int(steps)) for dir, steps in re.findall(r'(\w)(\d+)', read())]
    solve(data)


if __name__ == '__main__':
    main()
