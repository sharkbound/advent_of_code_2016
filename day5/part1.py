from _md5 import md5
from functools import lru_cache

from read import read


@lru_cache
def hash_value(value):
    hash = md5()
    hash.update(value.encode())
    return hash.hexdigest()


def solve(value):
    i = 0
    ans = ''
    while len(ans) != 8:
        hash = hash_value(f'{value}{i}')
        if hash[:5] == '00000':
            ans += hash[5]
            print(ans)
        i += 1


def main():
    data = read()
    solve(data)


if __name__ == '__main__':
    main()
