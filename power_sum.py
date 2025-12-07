#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#


# START
def powerSum(X: int, N: int, num=1):
    # num, mint plusz egy parameter hozzaadva, ami az aktualis szam

    # az X lehet egy csokkentgetett modositott ertek a megoldas miatt
    if X == 0:
        return 1
    if X < 0 or num ** N > X:
        return 0

    # bevesszuk az aktualis szamot az X-be
    include = powerSum(X - num ** N, N, num + 1)
    # kihagyjuk
    exclude = powerSum(X, N, num + 1)

    return include + exclude
# END


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
