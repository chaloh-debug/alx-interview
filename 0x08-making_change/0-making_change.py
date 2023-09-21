#!/usr/bin/python3
""" Least amount of Coins needed
"""

# sort list
# set coins counter
# set list index increment
# check coin is less than total
# remainder = total - val
# recurse through if newTotal not equal to total
# return count


def makeChange(coins, total):
    """ Determines least amount of coins needed to meet a given amount.
    """
    temp = total
    coins.sort(reverse=1)  # sort from largest
    count = 0
    if total < 1:
        return 0
    n = len(coins)
    idx = 0  # coins index
    while temp > 0:
        if idx >= n:
            return -1
        if temp - coins[idx] >= 0:
            temp -= coins[idx]
            count += 1
        else:
            idx += 1
    return count
