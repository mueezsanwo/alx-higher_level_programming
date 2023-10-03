3-say_my_name.py
================

    >>> say_my_name = __import__('3-say_my_name').say_my_name

    >>> say_my_name(None, "Novoa")
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string

    >>> say_my_name("Daniel", None)
    Traceback (most recent call last):
        ...
    TypeError: last_name must be a string

    >>> say_my_name("Daniel", 1)
    Traceback (most recent call last):
        ...
    TypeError: last_name must be a string

    >>> say_my_name("Daniel", "Novoa", "24")
    Traceback (most recent call last):
        ...
    TypeError: say_my_name() takes from 1 to 2 positional arguments but 3 were given

    >>> say_my_name("Daniel", "Novoa")
    My name is Daniel Novoa

    >>> say_my_name("Daniel")
    My name is Daniel 
