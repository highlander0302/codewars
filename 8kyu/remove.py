"""
Take an array and remove every second element from the array.
Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]
"""

ARRAY = [
    "Keep",
    "Remove",
    "Keep",
    "Remove",
    "Keep",
    "Keep",
    "Remove",
    "Keep",
    "Remove",
    "Keep",
]


def remove(raw_array: list[str]) -> list[str]:
    return [word for word in raw_array if word != "Remove"]


RESULT = remove(ARRAY)
print(RESULT)
