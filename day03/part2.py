from __future__ import annotations

import argparse
import os.path

import pytest

import support
import re

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def remove_between_tokens(s: str, start_token: str, end_token: str = '') -> str:
    # Regex pattern to match the part between start_token and end_token
    if end_token != '':
        pattern = re.escape(start_token) + r'.*?' + re.escape(end_token)
    else:
        pattern = re.escape(start_token) + r'.*?$'
    
    # Replace the matched part with an empty string
    result = re.sub(pattern, '', s)
    
    return result


def compute(s: str) -> int:
    lines = s.splitlines()
    result = 0

    all_lines = ''

    for line in lines:
        all_lines += line

    start_token = "don't()"
    end_token = "do()"
    s = remove_between_tokens(all_lines, start_token, end_token)
    start_token = "don't()"
    line = remove_between_tokens(s, start_token)
    # Regex pattern to find "mul(int,int)"
    pattern = r"mul\(\d+,\d+\)"
    # Find all matches
    matches = re.findall(pattern, line)
    for match in matches:
        int1, int2 = map(int, re.findall(r"\d+", match))
        result += int1 * int2

    return result


INPUT_S = '''\
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
'''
EXPECTED = 48


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

    return 0  # 77055967


if __name__ == '__main__':
    raise SystemExit(main())
