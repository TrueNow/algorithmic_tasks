from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    checked = {}
    for i, num in enumerate(nums):
        any_num = target - num
        if any_num in checked:
            return [checked[any_num], i]
        else:
            checked[num] = i
    return [-1, -1]


def main():
    example_list = [1, 5, 3, 4, 8, 6, 7]
    targets = [0, 3, 8, 4, 6, 21]
    for target in targets:
        print(two_sum(nums=example_list, target=target))


if __name__ == '__main__':
    main()
