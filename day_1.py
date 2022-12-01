""" Day 1: Calorie Counting """

import sys


def part_one() -> int:
    max_calories = 0
    elf = 0
    for line in sys.stdin:
        if line.strip().isdigit():
            elf += int(line)
        else:
            if elf > max_calories:
                max_calories = elf
            elf = 0
    return max_calories


def part_two(top: int) -> int:
    elves = []
    elf = 0
    for line in sys.stdin:
        if line.strip().isdigit():
            elf += int(line)
        else:
            elves.append(elf)
            elf = 0
    return sum(sorted(elves)[-top:])


# print(part_one())
print(part_two(3))
