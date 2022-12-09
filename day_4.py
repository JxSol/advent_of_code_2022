""" Day 4: Camp Cleanup """

import sys


def part_one() -> int:
    counter = 0
    for line in sys.stdin:
        elf_1, elf_2 = line.strip().split(',')
        elf_1_start, elf_1_end = (int(x) for x in elf_1.split('-'))
        elf_2_start, elf_2_end = (int(x) for x in elf_2.split('-'))
        if elf_1_start >= elf_2_start and elf_1_end <= elf_2_end:
            counter += 1
        elif elf_1_start <= elf_2_start and elf_1_end >= elf_2_end:
            counter += 1
    return counter


def part_two() -> int:
    counter = 0
    for line in sys.stdin:
        elf_1, elf_2 = line.strip().split(',')
        elf_1_start, elf_1_end = (int(x) for x in elf_1.split('-'))
        elf_2_start, elf_2_end = (int(x) for x in elf_2.split('-'))
        if elf_1_end < elf_2_start or elf_1_start > elf_2_end:
            pass
        else:
            counter += 1
    return counter


# print(part_one())
print(part_two())
