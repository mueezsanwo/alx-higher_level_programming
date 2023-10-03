#!/usr/bin/python3
"""
prints a text with 2 new lines after
each of these characters: ., ? and :
"""


def text_indentation(text):
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    i = 0
    chars = ".?:"
    while (i < len(text)):
        if text[i] in chars:
            print(text[i], end="\n\n")
            if i < (len(text) - 1) and text[i + 1] == " ":
                i += 2
            else:
                i += 1
        else:
            print(text[i], end="")
            i += 1
