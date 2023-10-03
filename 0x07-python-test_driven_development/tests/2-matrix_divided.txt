2-matrix_divided.py
===================

    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided

    >>> matrix_divided(None, 5)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = [[5, 10], [20, 50]]
    >>> matrix_divided(matrix, None)
    Traceback (most recent call last):
        ...
    TypeError: div must be a number

    >>> matrix = "holberton"
    >>> matrix_divided(matrix, 5)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = [["a", "b"], [3, 4]]
    >>> matrix_divided(matrix, 2)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix = [[5, 10], [20, 50, 60, 75]]
    >>> matrix_divided(matrix, 5)
    Traceback (most recent call last):
        ...
    TypeError: Each row of the matrix must have the same size

    >>> matrix = [[5, 10], [20, 50]]
    >>> matrix_divided(matrix, "a")
    Traceback (most recent call last):
        ...
    TypeError: div must be a number

    >>> matrix = [[5, 10], [20, 50]]
    >>> matrix_divided(matrix, None)
    Traceback (most recent call last):
        ...
    TypeError: div must be a number

    >>> matrix = [[5, 10], [20, 50]]
    >>> matrix_divided(matrix, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero

    >>> matrix  = [[1.3, 9.4, 7.2], [1.5, 5.1, 1.2]]
    >>> matrix_divided(matrix, -1)
    [[-1.3, -9.4, -7.2], [-1.5, -5.1, -1.2]]

    >>> matrix = [[1, 2, 3], [1, 2, 3]]
    >>> matrix_divided(matrix, 1.2)
    [[0.83, 1.67, 2.5], [0.83, 1.67, 2.5]]

    >>> matrix = [[float('inf'), 1.3, 1.3], [1.3, 1.3, 1.3]]
    >>> matrix_divided(matrix, float('inf'))
    [[nan, 0.0, 0.0], [0.0, 0.0, 0.0]]

    >>> matrix = [[1, 2, 3], [1, 2, 3]]
    >>> matrix_divided(matrix, 1.2)
    [[0.83, 1.67, 2.5], [0.83, 1.67, 2.5]]

    >>> matrix = [[5.2, 5.5, 6.3], [1, 2, 3]]
    >>> matrix_divided(matrix, float('inf'))
    [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]

    >>> matrix = [[1.1, 1.1, 1.1], [1.2, 1.2, 1.2]]
    >>> matrix_divided(matrix, True)
    [[1.1, 1.1, 1.1], [1.2, 1.2, 1.2]]
