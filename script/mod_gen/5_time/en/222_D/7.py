def solve(n,a,b):
    mod = 998244353
    dp = [[0]*(n+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(n+1):
            dp[i+1][j] = dp[i][j]
            if a[i] <= j <= b[i]:
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= mod
    return sum(dp[-1]) % mod
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(solve(n,a,b))
