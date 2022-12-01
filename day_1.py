""" Day 1: Calorie Counting """

import sys

max_callories = 0
elf = 0

for line in sys.stdin:
    if line.strip().isdigit():
        elf += int(line)
    else:
        if elf > max_callories:
            max_callories = elf
        elf = 0

print(max_callories)
