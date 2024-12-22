from __future__ import annotations

import argparse
import os.path

import pytest

import support
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    grid = [list(line) for line in lines]

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'X':
                # Check the row forward
                if j + 3 < len(grid[i]) and \
                    grid[i][j + 1] == 'M' and \
                    grid[i][j + 2] == 'A' and \
                    grid[i][j + 3] == 'S':
                    count += 1
                # Check the row backward
                if j - 3 >= 0 and \
                    grid[i][j - 1] == 'M' and \
                    grid[i][j - 2] == 'A' and \
                    grid[i][j - 3] == 'S':
                    count += 1
                # Check the column downward
                if i + 3 < len(grid) and \
                    grid[i + 1][j] == 'M' and \
                    grid[i + 2][j] == 'A' and \
                    grid[i + 3][j] == 'S':
                    count += 1
                # Check the column upward
                if i - 3 >= 0 and \
                    grid[i - 1][j] == 'M' and \
                    grid[i - 2][j] == 'A' and \
                    grid[i - 3][j] == 'S':
                    count += 1
                # Check the diagonal downward right
                if i + 3 < len(grid) and j + 3 < len(grid[i]) and \
                    grid[i + 1][j + 1] == 'M' and \
                    grid[i + 2][j + 2] == 'A' and \
                    grid[i + 3][j + 3] == 'S':
                    count += 1
                # Check the diagonal downward left
                if i + 3 < len(grid) and j - 3 >= 0 and \
                    grid[i + 1][j - 1] == 'M' and \
                    grid[i + 2][j - 2] == 'A' and \
                    grid[i + 3][j - 3] == 'S':
                    count += 1
                # Check the diagonal upward right
                if i - 3 >= 0 and j + 3 < len(grid[i]) and \
                    grid[i - 1][j + 1] == 'M' and \
                    grid[i - 2][j + 2] == 'A' and \
                    grid[i - 3][j + 3] == 'S':
                    count += 1
                # Check the diagonal upward left
                if i - 3 >= 0 and j - 3 >= 0 and \
                    grid[i - 1][j - 1] == 'M' and \
                    grid[i - 2][j - 2] == 'A' and \
                    grid[i - 3][j - 3] == 'S':
                    count += 1

    return count


INPUT_S = '''\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''
EXPECTED = 18


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

    return 0  # 2662


if __name__ == '__main__':
    raise SystemExit(main())
