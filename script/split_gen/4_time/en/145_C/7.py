def main():
    import sys
    from itertools import permutations
    import math
    N = int(input())
    towns = []
    for i in range(N):
        x, y = map(int, input().split())
        towns.append((x, y))
    paths = permutations(towns)
    total = 0
    for path in paths:
        for i in range(N - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]
            total += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    print(total / math.factorial(N))
