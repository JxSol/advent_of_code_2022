""" Day 2: Rock Paper Scissors """

import sys

"""
Rock - A X
Paper - B Y
Scissors - C Z
"""
elf_value = ('A', 'B', 'C')
my_value = ('X', 'Y', 'Z')


def part_one() -> int:
    score = 0
    for line in sys.stdin:
        elf, me = line.strip().split()
        elf_i = elf_value.index(elf)
        me_i = my_value.index(me)
        if elf_i == me_i:
            score += 3  # draw
        elif (elf_i + 1) % 3 == me_i:
            score += 6  # win
        score += me_i + 1
    return score


def part_two() -> int:
    score = 0
    for line in sys.stdin:
        elf, me = line.strip().split()
        elf_i = elf_value.index(elf)
        if me == 'Y':
            score += 3  # draw
            score += elf_i + 1
        elif me == 'Z':
            score += 6  # win
            score += (elf_i + 1) % 3 + 1
        else:
            score += (elf_i - 1) % 3 + 1
    return score


# print(part_one())
print(part_two())
