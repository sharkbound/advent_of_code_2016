from itertools import permutations

import numpy as np


def solve(data):
    def is_valid(lengths):
        return all(x + y > z for x, y, z in permutations(lengths))

    print(sum(map(is_valid, data)))


def main():
    data = np.fromfile('data.txt', dtype=int, sep='\n').reshape((-1, 3))
    solve(data)


if __name__ == '__main__':
    main()
