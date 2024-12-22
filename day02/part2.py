from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()

    lines_increasing = []
    for line in lines:
        # split line into individual items
        items = line.split()
        # convert each item to the desired type
        items = [int(item) for item in items]

        increasing = True
        free_pass = True
        remove = 0
        i = 0

        while i < len(items) - 1:
            if items[i + 1] <= items[i] and free_pass is True:
                remove = i + 1
                free_pass = False
            elif items[i + 1] <= items[i]:
                increasing = False
            i += 1

        if increasing is True:
            items = items[:remove] + items[remove + 1:]
            lines_increasing.append(items)

    lines_decreasing = []
    for line in lines:
        # split line into individual items
        items = line.split()
        # convert each item to the desired type
        items = [int(item) for item in items]

        decreasing = True
        free_pass = True
        remove = 0
        i = 0

        while i < len(items) - 1:
            if items[i + 1] >= items[i] and free_pass is True:
                remove = i + 1
                free_pass = False
            elif items[i + 1] >= items[i]:
                decreasing = False
            i += 1

        if decreasing is True:
            items = items[:remove] + items[remove + 1:]
            lines_decreasing.append(items)

    count = 0
    for line in lines_increasing:
        i = 0
        valid_flag = True
        while i < len(line) - 1:
            incr = line[i + 1] - line[i]
            if valid_flag is False:
                break
            if incr < 1 or incr > 3:
                valid_flag = False
            i += 1
        if valid_flag == True:
            count += 1

    for line in lines_decreasing:
        i = 0
        valid_flag = True
        while i < len(line) - 1:
            decr = line[i] - line[i + 1]
            if valid_flag is False:
                break
            if decr < 1 or decr > 3:
                valid_flag = False
            i += 1
        if valid_flag == True:
            count += 1
        
    return count  # more than 312 and not 320


INPUT_S = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
EXPECTED = 4


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
