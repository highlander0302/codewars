"""
You are given two sorted lists.
Write a function to merge these two sorted lists into a single sorted list.

Example:
merge_sorted_lists([1, 3, 5], [2, 4, 6])  # Expected output: [1, 2, 3, 4, 5, 6]
merge_sorted_lists([1, 2], [3, 4, 5])  # Expected output: [1, 2, 3, 4, 5]
merge_sorted_lists([], [1, 2, 3])  # Expected output: [1, 2, 3]
merge_sorted_lists([5, 10], [])  # Expected output: [5, 10]
"""


def merge_sorted_lists(l1, l2):
    return sorted(l1 + l2)


def merge_differently(l1: list[int], l2: list[int]) -> list[int]:
    l1.extend(l2)
    l1.sort()
    return l1


print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))
print(merge_differently([1, 3, 5], [2, 4, 6]))
