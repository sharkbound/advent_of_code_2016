import numpy as np

from read import read_lines

move_offsets = {
    'L': (-1, 0),
    'R': (1, 0),
    'U': (0, -1),
    'D': (0, 1),
}

keys = np.array([
    list('123'),
    list('456'),
    list('789'),
])


def is_valid(x, y):
    return all(i in range(3) for i in (x, y))


def solve(lines):
    ans = []
    x, y = 1, 1
    for line in lines:
        for char in line:
            if is_valid(x + (xoff := move_offsets[char][0]), y):
                x += xoff
            if is_valid(x, y + (yoff := move_offsets[char][1])):
                y += yoff
        ans.append(keys[y, x])
    print(''.join(ans))


def main():
    data = read_lines()
    solve(data)


if __name__ == '__main__':
    main()
