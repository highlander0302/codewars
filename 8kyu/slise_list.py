"""
Take an array and remove every second element from the array.
Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
"""

MY_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def remove_every_other(l: list[int]) -> list[int]:
    l = l[::2]  # slise every second element.
    return l


RESULT = remove_every_other(MY_LIST)
print(RESULT)
