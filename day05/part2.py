from __future__ import annotations

import argparse
import os.path
from collections import defaultdict
import pytest
import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


# Class to represent a graph using adjacency list representation
class Graph:
    """
    Class to represent a graph.
    """

    def __init__(self, vertices):
        """
        Initialize the graph with a given number of vertices.
        """
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.num_vertices = vertices  # No. of vertices

    def add_edge(self, u, v):
        """
        Function to add an edge to the graph.
        """
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        """
        A recursive function used by topological_sort.
        """
        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] is False:
                self.topological_sort_util(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.insert(0, v)

    def topological_sort(self):
        """
        The function to do Topological Sort. It uses recursive topological_sort_util.
        """
        # Mark all the vertices as not visited
        visited = [False] * self.num_vertices
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.num_vertices):
            if visited[i] is False:
                self.topological_sort_util(i, visited, stack)

        # Return contents of stack
        return stack


def compute(s: str) -> int:
    # split input on blank line
    input1 = s.split('\n\n')
    rules = input1[0].splitlines()
    pages = input1[1].splitlines()

    middle_page = 0
    bad_pages = []

    # check if each page follows the rules
    for page in pages:
        flag = False
        # split page into individual items
        page_lst = page.split(',')
        for rule in rules:
            rule = rule.split('|')
            if (rule[0]) in page_lst and (rule[1]) in page_lst:
                # find index of rule in page
                index_rule1 = int(page_lst.index(rule[0]))
                index_rule2 = int(page_lst.index(rule[1]))
                if index_rule1 > index_rule2:
                    flag = True
                    break
        if flag:
            bad_pages.append(page)

    for page in bad_pages:
        flag = False
        page = page.split(',')
        g = Graph(len(page))
        for rule in rules:
            rule = rule.split('|')
            if (rule[0]) in page and (rule[1]) in page:
                index_rule1 = int(page.index(rule[0]))
                index_rule2 = int(page.index(rule[1]))
                g.add_edge(index_rule1, index_rule2)
                flag = True

        if flag:
            order = g.topological_sort()
            page_ordered = [page[i] for i in order]
            middle_page += int(page_ordered[len(page) // 2])

    return middle_page  # 5723


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
EXPECTED = 123


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
