import itertools
from typing import List


# fast solution
def powerful_integers(x: int, y: int, bound: int) -> List[int]:
    X, Y, results = [1], [1], []
    while X[-1] < bound and x != 1:
        X.append(X[-1] * x)
    while Y[-1] < bound and y != 1:
        Y.append(Y[-1] * y)

    combinations = itertools.product(X, Y)
    for i, j in combinations:
        result = i + j
        if result <= bound:
            results.append(result)
    return list(set(results))


# slow solution
def powerful_integers_2(x: int, y: int, bound: int) -> List[int]:
    results = []
    i = 1
    while i <= bound:
        j = 1
        while i + j <= bound:
            results.append(i + j)
            j *= y
        i *= x
    return list(set(results))


def main():
    RESULT = [2, 3, 4, 5, 7, 9, 10]
    result = powerful_integers(2, 3, 10)
    assert result == RESULT, f'Неверное решение {result} != {RESULT}'
    result = powerful_integers_2(2, 3, 10)
    assert result == RESULT, f'Неверное решение {result} != {RESULT}'


if __name__ == '__main__':
    main()
