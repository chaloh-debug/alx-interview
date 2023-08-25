#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    if type(data) is not list: # data is a list of integers
        return False
    for i in data:
        if type(i) is not int: # each integer represents 1 byte of data
            return False
    try:
        bytes(i & 0xFF for i in data).decode() # decode bytes to string
        return True
    except UnicodeDecodeError: # if data is not valid UTF-8
        return False
