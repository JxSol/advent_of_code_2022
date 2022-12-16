""" --- Day 5: Supply Stacks --- """

import sys
from collections import deque

COLUMN_WIDTH = 4
START_INDEX = 1


def part_one() -> str:
    crates_map = {}
    # сбор карты контейнеров
    for line in sys.stdin:
        if line.strip() == '':
            break
        target = START_INDEX
        for i, c in enumerate(line):
            if i == target:
                if c.isalpha():
                    crates_map.setdefault((i + START_INDEX) // COLUMN_WIDTH + 1,
                                          deque()).appendleft(c)
                target += COLUMN_WIDTH

    # перемещение контейнеров
    for line in sys.stdin:
        data = line.split()
        for _ in range(int(data[1])):
            crates_map[int(data[5])].append(crates_map[int(data[3])].pop())

    # получение строки из последних элементов
    sorted_crates = sorted(crates_map.items(), key=lambda x: x[0])
    return ''.join(item[1].pop() for item in sorted_crates)


def part_two() -> str:
    crates_map = {}
    # сбор карты контейнеров
    for line in sys.stdin:
        if line.strip() == '':
            break
        target = START_INDEX
        for i, c in enumerate(line):
            if i == target:
                if c.isalpha():
                    crates_map.setdefault((i + START_INDEX) // COLUMN_WIDTH + 1, []).insert(0, c)
                target += COLUMN_WIDTH

    # перемещение контейнеров
    for line in sys.stdin:
        data = line.split()
        number = int(data[1])
        crates_map[int(data[5])].extend(crates_map[int(data[3])][-number:])
        del crates_map[int(data[3])][-number:]

    # получение строки из последних элементов
    sorted_crates = sorted(crates_map.items(), key=lambda x: x[0])
    return ''.join(item[1].pop() for item in sorted_crates)


# print(part_one())
print(part_two())
