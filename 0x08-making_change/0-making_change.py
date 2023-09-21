#!/usr/bin/python3

# check list
# sort list
# check totals
# check largest denomination is less than total
# remainder = total - val
# recurse through if newTotal not equal to total
# remainder

def makeChange(coins, total):
    coins.sort(reverse=1)

    if total < 1:
        return 0
    for i in coins:
        if i < total:
            remainder = total - i
            print(remainder)

    print(coins)

makeChange([1, 2, 25], 37)