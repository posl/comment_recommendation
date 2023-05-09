def main():
    from sys import stdin
    from itertools import product
    from collections import defaultdict
    from bisect import bisect_left
    readline = stdin.readline
    N, C = map(int, readline().split())
    D = [list(map(int, readline().split())) for _ in range(C)]
    c = [list(map(int, readline().split())) for _ in range(N)]
    cost = [[0] * C for _ in range(3)]
    for i, j, k in product(range(N), range(N), range(C)):
        cost[(i + j) % 3][k] += D[c[i][j] - 1][k]
    dp = [[float('inf')] * C for _ in range(3)]
    for i in range(C):
        dp[0][i] = cost[0][i]
    for i in range(1, 3):
        for j, k in product(range(C), range(C)):
            if j != k:
                dp[i][k] = min(dp[i][k], dp[i - 1][j] + cost[i][k])
    print(min(dp[2]))
