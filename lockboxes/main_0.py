#!/usr/bin/python3

canUnlockAll = __import__("0-lockboxes").canUnlockAll
# Example test cases
boxes1 = [[1], [2], [3], [4], []]
boxes2 = [[1, 2, 3], [0], [4], [2], [1, 5], [6], []]
boxes3 = [[1, 3], [3, 0, 1], [2], [0]]

print(canUnlockAll(boxes1))  # Should return True
print(canUnlockAll(boxes2))  # Should return False
print(canUnlockAll(boxes3))  # Should return False
