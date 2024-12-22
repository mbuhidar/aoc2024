from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()

    lines_increasing = []
    lines_decreasing = []

    for line in lines:
        # split line into individual items
        items = line.split()
        # convert each item to the desired type
        items = [int(item) for item in items] 

        increasing = True

        for i in range(len(items) - 1):
            if items[i + 1] <= items[i]:
                increasing = False
        if increasing is True:
            lines_increasing.append(items)

        decreasing = True

        for i in range(len(items) - 1):
            if items[i + 1] >= items[i]:
                decreasing = False
        if decreasing is True:
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
                break   
            i += 1
        if valid_flag == True:
            count += 1
        
    return count  # 279


INPUT_S = '''\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''
EXPECTED = 2


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
