from itertools import permutations

from read import read_lines


def solve(data):
    print(
        sum(
            all(x + y > z for x, y, z in permutations(lengths))
            for lengths in data
        )
    )


def main():
    data = [list(map(int, line.split())) for line in read_lines()]
    solve(data)


if __name__ == '__main__':
    main()
