def dfs(a, b, c, mp, l):
    if a == 0 and b == 0 and c == 0:
        return mp
    if a < 0 or b < 0 or c < 0:
        return 10 ** 9
    if l == n:
        return 10 ** 9
    if dp[a][b][c][l] != -1:
        return dp[a][b][c][l]
    dp[a][b][c][l] = min(dfs(a - L[l], b, c, mp + 1, l), dfs(a, b - L[l], c, mp + 1, l), dfs(a, b, c - L[l], mp + 1, l), dfs(a + L[l], b + L[l], c, mp + 10, l + 1), dfs(a, b + L[l], c + L[l], mp + 10, l + 1), dfs(a + L[l], b, c + L[l], mp + 10, l + 1), dfs(a + L[l], b + L[l], c + L[l], mp + 10, l + 1))
    return dp[a][b][c][l]
n, a, b, c = map(int, input().split())
L = [int(input()) for _ in range(n)]
dp = [[[[0] * (n + 1) for _ in range(101)] for _ in range(101)] for _ in range(101)]
for i in range(101):
    for j in range(101):
        for k in range(101):
            for l in range(n + 1):
                dp[i][j][k][l] = -1
ans = dfs(a, b, c, 0, 0)
print(ans if ans != 10 ** 9 else -1)
