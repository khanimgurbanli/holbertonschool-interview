#!/usr/bin/python3

canUnlockAll = __import__("0-lockboxes").canUnlockAll

# Test Cases
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # return False

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))  # return True

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))  # return False
