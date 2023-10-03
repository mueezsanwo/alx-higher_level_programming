#!/usr/bin/python3
"""prints a square with the character #"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for square in range(size):
        [print("#", end="") for a in range(size)]
        print("")

