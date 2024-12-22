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

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == 'A':
                valid = False
                # Gather letters to the upper right, lower right, lower left, and upper left of A
                letters = []
                letters.append(grid[i - 1][j - 1])
                letters.append(grid[i - 1][j + 1])
                letters.append(grid[i + 1][j + 1])
                letters.append(grid[i + 1][j - 1])
                # Check for M and S in alternating pattern
                if letters[0] == 'M' and letters[1] == 'S' and letters[2] == 'S' and letters[3] == 'M':
                    valid = True
                elif letters[0] == 'S' and letters[1] == 'M' and letters[2] == 'M' and letters[3] == 'S':
                    valid = True
                elif letters[0] == 'M' and letters[1] == 'M' and letters[2] == 'S' and letters[3] == 'S':
                    valid = True
                elif letters[0] == 'S' and letters[1] == 'S' and letters[2] == 'M' and letters[3] == 'M':
                    valid = True

                if valid:
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
EXPECTED = 9


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
