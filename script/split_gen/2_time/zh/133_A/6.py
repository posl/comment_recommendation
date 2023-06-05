def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    dp = [[0]*(n+1) for _ in range(k+1)]
    dp[0][0] = 1
    for i in range(k):
        for j in range(n+1):
            dp[i+1][j] = (dp[i+1][j-1] + dp[i][j]) % mod
            if j >= i+1:
                dp[i+1][j] -= dp[i][j-i-1]
                dp[i+1][j] %= mod
    print(dp[k][n])
