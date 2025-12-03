#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

# def shortest_neighbor_distances():


# START
def roadsAndLibraries(n, c_lib, c_road, cities):
    # Ha a konyvtar megerosebb, nem epitunk utat...
    if c_lib <= c_road:
        # ...hanem minden varosba konyvtarat
        return n * c_lib
    # Egyebb esetben utak epulnek

    # Szomszedsagi graf
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in cities:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    # Melysegi bejaras
    def deep_search(node):
        stack = [node]
        size = 0
        while stack:
            # Legegyszerubb modja a stack hasznalata
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                size += 1
                stack.extend(graph[current])

        return size

    # Vegso koltsegszamolas
    total = 0
    for city in range(1, n + 1):
        if city not in visited:
            comp_size = deep_search(city)
            total += c_lib + (comp_size - 1) * c_road

    return total


# END


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
