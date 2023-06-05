def f(n, v, c):
    dp = [[0 for _ in range(1000)] for _ in range(1000)]
    for i in range(n):
        for j in range(1000):
            if j < c[i]:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j], dp[i][j-c[i]] + v[i])
    return dp[n][999]
n = int(input())
v = list(map(int, input().split()))
c = list(map(int, input().split()))
print(f(n, v, c))
