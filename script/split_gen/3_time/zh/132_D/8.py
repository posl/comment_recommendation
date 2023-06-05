def main():
    n,k = map(int, input().split())
    mod = 10**9+7
    dp = [[0]*(k+1) for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(k+1):
            if j == 0:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = (dp[i][j] + dp[i][j-1]*(n-k-i))%mod
    for i in range(1,k+1):
        print(dp[n][i])
