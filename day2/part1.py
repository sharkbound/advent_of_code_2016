from enum import Enum, auto

from read import read, read_lines


class Direction(Enum):
    U = auto()
    D = auto()
    L = auto()
    R = auto()


move_offsets = {
    Direction.L: (-1, 0),
    Direction.R: (1, 0),
    Direction.U: (0, 1),
    Direction.D: (0, -1),
}


def solve(lines):
    pass


def main():
    data = read_lines('sample1.txt')
    solve(data)


if __name__ == '__main__':
    main()
