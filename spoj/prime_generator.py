import math

count = input()

for i in range(int(count)):
    inp = input().split(" ")
    primes = []
    for j in range(int(inp[0]), int(inp[1]) + 1):
        if j <= 1:
            continue
        if j == 2 or j == 3:
            primes.append(2)
        if j % 2 == 0 or j % 3 == 0:
            continue

    print(*primes, sep="\n")
