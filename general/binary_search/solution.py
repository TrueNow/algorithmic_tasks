from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def main():
    example_list = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66]
    targets = [0, 3, 21, 34, 56, 66]
    for target in targets:
        print(search(nums=example_list, target=target))


if __name__ == '__main__':
    main()
