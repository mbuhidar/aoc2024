from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    # Parse the input, s, consisting of two columns of integers separated by whitespace
    list1 = []
    list2 = []
    for line in s.splitlines():
        list1.append(list(map(int, line.split()))[0])
        list2.append(list(map(int, line.split()))[1])

    # sort each list
    list1.sort()
    list2.sort()

    # bucket sort the list2
    max_val = max(list2)
    bucket = [0] * (max_val + 1)
    for val in list2:
        bucket[val] += 1

    # calculate the similarity score by multiplying the number of occurrences of each list1 value in list2 
    simliarity_list = []
    for i in range(len(list1)):
        if list1[i] < max_val:
            simliarity_list.append(list1[i] * bucket[list1[i]])

    return sum(simliarity_list)  # 29379307


INPUT_S = '''\
3   4
4   3
2   5
1   3
3   9
3   3
'''
EXPECTED = 31


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
