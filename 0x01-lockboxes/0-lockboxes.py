#!/usr/bin/python3
""" Lockboxes """
def canUnlockAll(boxes):
    """ Lockboxes """
    if len(boxes) == 0 or boxes is None:
        return False
    temp_keys = [0]

    for box in range(len(boxes)):
        for key in boxes[box]:
            if key not in temp_keys:
                temp_keys.append(key)
            else:
                continue
        temp_keys.sort()
    print(temp_keys)
    if len(temp_keys) == len(boxes):
        return True
    return False