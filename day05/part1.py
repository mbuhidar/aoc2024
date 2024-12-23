from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    # split input on blank line
    input = s.split('\n\n')
    rules = input[0].splitlines()
    pages = input[1].splitlines()

    middle_page = 0

    # check if each page follows the rules
    for page in pages:
        valid = True
        check = False
        # split page into individual items
        page = page.split(',')
        for rule in rules:
            rule = rule.split('|')
            if (rule[0]) in page and (rule[1]) in page:
                check = True
                # find index of rule in page
                index_rule1 = int(page.index(rule[0]))
                index_rule2 = int(page.index(rule[1]))
                if index_rule1 > index_rule2:
                    valid = False
                    break

        if valid and check:
            middle_page += int(page[len(page) // 2])

    return middle_page  # 4609


INPUT_S = '''\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
'''
EXPECTED = 143


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
