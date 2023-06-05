def mod(x):
    return x % (10**9 + 7)
n, k = map(int, input().split())
dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0][0] = 1
for i in range(k):
    for j in range(n + 1):
        dp[i + 1][j] = mod(dp[i + 1][j] + dp[i][j])
        dp[i + 1][j] = mod(dp[i + 1][j] + dp[i][j] * (n - j))
        if j + 1 <= n:
            dp[i + 1][j + 1] = mod(dp[i + 1][j + 1] + dp[i][j] * j)
print(dp[k][n])
for i in range(k):
    print(dp[i + 1][n])

if __name__ == '__main__':
    mod()