n = max(1, min(int(input()), 200_000))
sticks: list[int] = [int(num) for num in input().split(' ')]

# sticks.sort()

costs: list[int] = []

for i in range(n):
    cost = 0
    for j in range(n):
        if i != j:
            cost += abs(sticks[i] - sticks[j])
    costs.append(cost)

print(min(costs))
