""" Day 6: Tuning Trouble """

from collections import deque

def part_one(marker_length) -> int:
    queue = deque()
    counter = 0
    for c in input():
        if len(queue) >= marker_length:
            queue.popleft()
        queue.append(c)
        counter += 1
        if len(set(queue)) == marker_length:
            return counter

def part_two(marker_length) -> int:
    queue = deque()
    counter = 0
    for c in input():
        if len(queue) >= marker_length:
            queue.popleft()
        queue.append(c)
        counter += 1
        if len(set(queue)) == marker_length:
            return counter

# print(part_one(4))
print(part_two(14))
