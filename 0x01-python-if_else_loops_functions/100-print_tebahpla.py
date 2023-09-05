#!/usr/bin/python3

""""Print the alphabet in reverse order alternating upper- and lower-case."""
for c in range(alpha('z'), alpha('a') - 1, -1):
    print("{:c}".format((c - (alpha('a') - alpha('A'))) if c % 2 else c), end='')
