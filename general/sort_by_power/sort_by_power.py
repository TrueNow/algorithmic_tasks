def get_kth(lo: int, hi: int, k: int):
    lst = []
    for i in range(lo, hi + 1):
        lst.append((i, calc_steps(i)))
    result = sorted(lst, key=lambda item: item[1])
    return result[k - 1][0]


def calc_steps(x):
    step_count = 0
    while x != 1:
        if x % 2:
            x = 3 * x + 1
        else:
            x /= 2
        step_count += 1
    return step_count


def main():
    print(get_kth(12, 15, 2))
    print(get_kth(7, 11, 4))


if __name__ == '__main__':
    main()
