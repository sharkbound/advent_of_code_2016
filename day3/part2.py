import numpy as np


def solve(data: np.ndarray):
    pass


def main():
    # data = np.reshape([tuple(map(int, line.split())) for line in read_lines()], (-1, 3))
    data = np.fromfile('data.txt', dtype=int, sep='\n').reshape((-1, 3))
    solve(data)


if __name__ == '__main__':
    main()
