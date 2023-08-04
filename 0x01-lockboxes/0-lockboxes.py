#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ determines if all the boxes can be opened. """
    if len(boxes) == 0:
        return False
    temp_keys = [0]

    for key in temp_keys:
        for box in boxes[key]:
            if box not in temp_keys:
                temp_keys.append(box)
    if len(temp_keys) == len(boxes):
        return True
    else:
        return False
