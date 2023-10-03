0-add_integer
=============

    >>> add_integer = __import__('0-add_integer').add_integer

    >>> add_integer(1, 1)
    2

    >>> add_integer(2.5, 3)
    5

    >>> add_integer(1)
    99

    >>> [add_integer(i, i ** 2) for i in range(9)]
    [0, 2, 6, 12, 20, 30, 42, 56, 72]

    >>> add_integer(-3, 3)
    0

    >>> add_integer(True)
    99

    >>> add_integer(False)
    98

    >>> add_integer(True, True)
    2

    >>> add_integer(-True, 4)
    3

    >>> add_integer(-True)
    97

    >>> add_integer(True, 5)
    6

    >>> add_integer()
    Traceback (most recent call last):
        ...
    TypeError: add_integer() missing 1 required positional argument: 'a'

    >>> add_integer('a', 3)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    >>> add_integer(1, 2, 3)
    Traceback (most recent call last):
        ...
    TypeError: add_integer() takes from 1 to 2 positional arguments but 3 were given

    >>> add_integer(1, float('inf'))
    Traceback (most recent call last):
        ...
    OverflowError: cannot convert float infinity to integer

    >>> add_integer([1], 4)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    >>> add_integer(5, float('nan'))
    Traceback (most recent call last):
        ...
    ValueError: cannot convert float NaN to integer
