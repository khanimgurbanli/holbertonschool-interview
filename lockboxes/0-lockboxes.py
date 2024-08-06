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

    # To track which boxes have been visited
    visited = [False] * n  #  mean is  visited = [False, False, False]
    visited[0] = True  #  mean is  visited = [True, False, False]

    # Queue for Breadth-First Search (BFS)
    queue = [0]  # Start with the first box

    # Breadth-First Search (BFS)
    while queue:
        current = queue.pop(0)  # Get the next box to process

        # Check each key in the current box
        for box in boxes[current]:
            if box < n and not visited[box]:  # Check if box index is valid
                visited[box] = True  # Mark it as visited
                queue.append(box)  # Add it to the queue for next exploration

    return all(visited)
