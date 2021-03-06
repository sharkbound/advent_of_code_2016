from itertools import permutations

import numpy as np


def solve(data: np.ndarray):
    print(
        sum(
            1
            for i in range(3)
            for lengths in data[..., i].reshape((-1, 3))
            if all(x + y > z for x, y, z in permutations(lengths))
        )
    )


def main():
    data = np.fromfile('data.txt', dtype=int, sep='\n').reshape((-1, 3))
    solve(data)


if __name__ == '__main__':
    main()
