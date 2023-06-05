def solve():
    n = int(input())
    x, y = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    dp = [[[0 for _ in range(300 * 300 + 1)] for _ in range(300 + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, 300 + 1):
            for k in range(300 * 300 + 1):
                if k - a[i - 1] >= 0 and j - 1 >= 0:
                    dp[i][j][k] |= dp[i - 1][j - 1][k - a[i - 1]]
                if k - b[i - 1] >= 0:
                    dp[i][j][k] |= dp[i - 1][j][k - b[i - 1]]
    ans = -1
    for i in range(1, n + 1):
        for j in range(1, 300 * 300 + 1):
            if dp[i][x][j] and dp[i][y][j]:
                ans = max(ans, j)
    print(ans)
solve()
