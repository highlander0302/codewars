"""
Create a function that accepts a string and a single character,
and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

("Hello", 'o')  =>  1
("Hello", 'l')  =>  2
("", 'z')       =>  0
"""

MY_STRING = "aaaaaaaaacccttttcacacacacact"
MY_LETTER = "a"


def letter_count(s, l):
    return s.count(l)


RESULT = letter_count(MY_STRING, MY_LETTER)
print(RESULT)
