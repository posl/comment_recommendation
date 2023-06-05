def dfs(i, j, k):
    if i == n:
        return 1
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    res = 0
    for l in range(3):
        if j != l and k != l:
            res += dfs(i + 1, k, l)
    dp[i][j][k] = res
    return res
n, m = map(int, input().split())
dp = [[[-1] * 3 for _ in range(3)] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    dp[a - 1][b - 1][0] = 0
    dp[a - 1][b - 1][1] = 0
    dp[a - 1][b - 1][2] = 0
    dp[b - 1][a - 1][0] = 0
    dp[b - 1][a - 1][1] = 0
    dp[b - 1][a - 1][2] = 0
res = 0
for i in range(3):
    for j in range(3):
        res += dfs(1, i, j)
print(res)

if __name__ == '__main__':
    dfs()