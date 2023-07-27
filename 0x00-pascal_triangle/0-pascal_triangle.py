#!/usr/bin/python3
""" pascal triangle challenge """


"""
def pascal_triangle(n):
    rs = []
    if n <= 0:
        print(rs)
        return rs
    else:
        for i in range(n):
            rs.append([int(j) for j in str(11**i)])
    return rs


pascal_triangle(5)
"""

def pascal_triangle(n):
    """ Pascal triangle using binomial coefficients """
    all = []
    if n <= 0:
        return []
    else:
        for i in range(n):
            row = [1] #initialize the row with 1
            for j in range(i):
                row.append(row[j] * (i - j) // (j + 1))  #binomial coefficient
            all.append(row) #append the row to the triangle
        return all #return the triangle
