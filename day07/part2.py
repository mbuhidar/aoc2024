from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def can_make(target, values):
    # Base case
    if len(values) == 1:
        # Return True if target is equal to the last remaining value
        return target == values[0]
    if target % values[-1] == 0 and can_make(target // values[-1], values[:-1]):
        return True
    if target > values[-1] and can_make(target - values[-1], values[:-1]):
        return True
    if len(str(target)) > len(str(values[-1])) and str(target).endswith(str(values[-1])) \
            and can_make(int(str(target)[:-len(str(values[-1]))]), values[:-1]):
        return True
    return False


def compute(s: str) -> int:
    lines = s.splitlines()
    total = 0
    for line in lines:
        result, values = line.split(': ')
        target = int(result)
        values = list(map(int, values.split()))
        if can_make(target, values):
            total += target

    return total


INPUT_S = '''\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''
EXPECTED = 11387


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
