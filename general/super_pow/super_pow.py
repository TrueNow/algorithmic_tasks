from typing import List

MOD = 1337


def super_pow(a: int, b: List[int]) -> int:
    number = ''
    for digit in b:
        number += str(digit)
    number = int(number)
    return pow(a, number, mod=MOD)


def main():
    a, b = 1, [4, 3, 3, 8, 5, 2]
    print(super_pow(a, b))
    a, b = 4, [1, 0]
    print(super_pow(a, b))


if __name__ == '__main__':
    main()
