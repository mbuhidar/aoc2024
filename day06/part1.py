from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    # Split input into lines
    rows = s.splitlines()
    # Create a grid from the input
    grid = [list(row) for row in rows]
    rows = len(grid)
    cols = len(grid[0])
    # Find starting position for the guard
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '^':
                break
        else:
            continue
        break
    # Initialize the travel direction
    dr = -1
    dc = 0
    # Initialize the positions seen as a set
    seen = set()
    # Traverse the grid
    while True:
        seen.add((r, c))
        # Check if the guard has exited the grid
        if r + dr >= rows or r + dr < 0 or c + dc >= cols or c + dc < 0:
            break
        # Check if the guard has hit an obstacle
        if grid[r + dr][c + dc] == '#':
            # Change direction guard is moving by rotating 90 degrees clockwise
            # dc, dr: (0, -1) -> (1, 0) -> (0, 1) -> (-1, 0) -> (0, -1)
            dc, dr = -dr, dc
        else:  # Move the guard
            r += dr
            c += dc
    # Return the number of positions seen
    return len(seen)

INPUT_S = '''\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''
EXPECTED = 41


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
