from typing import List


def bubble_sort(nums: List[int]) -> List[int]:
    """Return a new list sorted in ascending order using bubble sort."""
    arr = nums.copy()
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    print("helloworld")
    sample = [5, 1, 4, 2, 8]
    print("原始数组:", sample)
    print("排序结果:", bubble_sort(sample))
