#!/usr/bin/python3
""" pascal triangle challenge """


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the
    Pascal’s triangle of n
    """
    rs = []
    if n <= 0:
        print(rs)
        return rs
    else:
        for i in range(n):
            """
            use power method.
            convert integer to string.
            split integer to digits.
            convert back to integer.
            append to list
            """
            rs.append([int(j) for j in str(11**i)])
    return rs
