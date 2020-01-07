from _md5 import md5
from functools import lru_cache

from read import read


@lru_cache
def hash_value(value):
    hash = md5()
    hash.update(value.encode())
    return hash.hexdigest()


def solve(value):
    RANGE = set(range(8))
    found = set()
    i = 0
    ans = ['0'] * 8
    matches = 0
    while matches < 8:
        if (hash := hash_value(f'{value}{i}'))[:5] == '00000':
            if (index := int(hash[5], 16)) in RANGE and index not in found:
                ans[index] = hash[6]
                matches += 1
                found.add(index)
                print(''.join(ans))
        i += 1


def main():
    data = read()
    solve(data)


if __name__ == '__main__':
    main()
