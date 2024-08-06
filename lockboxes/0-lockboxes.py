#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
and each box may contain keys to the other boxes

More informations:
- Prototype: def canUnlockAll(boxes)
- A key with the same number as a box opens that box
- You can assume all keys will be positive integers
- Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    n = len(boxes)  # Number of boxes
    visited = [False] * n  # Keep track of visited boxes
    visited[0] = True  # The first box is always open
    queue = [0]  # Start with the first box in the queue

    while queue:
        current = queue.pop(0)  # Get the next box to process
        for key in boxes[current]:  # Check all keys in the current box
            if (
                key < n and not visited[key]
            ):  # If the key is valid and the box is not visited
                visited[key] = True  # Mark the box as visited
                queue.append(key)  # Add the box to the queue for further exploration

    return all(visited)  # Return True if all boxes are visited, else False
