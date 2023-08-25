#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    if type(data) is not list:
        return False
    for i in data:
        if type(i) is not int:
            return False
    try:
        bytes(i & 0xFF for i in data).decode()
        return True
    except UnicodeDecodeError:
        return False
