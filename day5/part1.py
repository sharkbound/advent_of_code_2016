from _md5 import md5

from read import read, read_lines


def hash_value(value):
    hash = md5()
    hash.update(bytes(value))
    return hash.hexdigest()


def solve(data):
    pass


def main():
    data = read()
    solve(data)


if __name__ == '__main__':
    main()
