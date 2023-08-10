#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """
    Calculate minimum number of operations needed to result in exactly
    n characters in a file. Limited operations are (copy all) and (paste).
    """
    count = 0
    val = 1
    carrier = 0

    while val < n:
        if n % val == 0:
            carrier = val
            val *= 2
            count += 1
        else:
            val += carrier
        count += 1

    return count
