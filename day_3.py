""" Day 3: Rucksack Reorganization """

import sys
from functools import reduce
from string import ascii_letters

LETTERS = ascii_letters


def part_one() -> int:
    total = 0
    for line in sys.stdin:
        length = len(line)
        fail = set(line[:length // 2]) & set(line[length // 2:])
        total += LETTERS.find(fail.pop()) + 1
    return total


def part_two(quantity=3) -> int:
    total = 0
    elves = []
    for line in sys.stdin:
        elves.append(set(line.strip()))
        if len(elves) == quantity:
            fail = reduce(lambda x, y: x & y, elves)
            total += LETTERS.find(fail.pop()) + 1
            elves.clear()
    return total


# print(part_one())
print(part_two())
