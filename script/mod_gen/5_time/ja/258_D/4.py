def solve():
    #n, x = map(int, input().split())
    #a, b = [0] * n, [0] * n
    #for i in range(n):
    #    a[i], b[i] = map(int, input().split())
    n, x = 3, 4
    a, b = [3, 2, 4], [4, 3, 2]
    import numpy as np
    import sys
    sys.setrecursionlimit(10 ** 7)
    #dp = np.full((n, x + 1), np.inf)
    #def f(i, j):
    #    if j == 0:
    #        return 0
    #    if i == 0:
    #        return a[0] * j
    #    if dp[i][j] != np.inf:
    #        return dp[i][j]
    #    dp[i][j] = min(f(i - 1, j - 1) + a[i], f(i - 1, j) + b[i])
    #    return dp[i][j]
    #print(f(n - 1, x))
    dp = np.full((x + 1), np.inf)
    dp[0] = 0
    for i in range(n):
        for j in range(x, -1, -1):
            if j == 0:
                continue
            dp[j] = min(dp[j - 1] + a[i], dp[j] + b[i])
    print(int(dp[x]))

if __name__ == '__main__':
    solve()