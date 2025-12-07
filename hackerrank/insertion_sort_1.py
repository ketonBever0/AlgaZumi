#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

# START
def insertionSort1(n, arr):
    # beszuro rendezes - visszafele keri a feladat
    for i in reversed(range(1, len(arr))):
        key = arr[i]
        j = i - 1
        # helyet csinalunk a beszurashoz tolassal
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(*arr)
        # beszurjuk
        arr[j + 1] = key
    print(*arr)
# END


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
