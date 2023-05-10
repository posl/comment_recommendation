def solve(n, a, b):
    dp = [[0 for i in range(3001)] for j in range(3001)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(3001):
            dp[i+1][j] = dp[i][j]
            if j >= a[i] and j <= b[i]:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= 998244353
    return dp[n][3000]
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(n, a, b))
