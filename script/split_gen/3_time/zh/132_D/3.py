def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    dp = [[0 for i in range(n+1)] for j in range(k+1)]
    dp[0][0] = 1
    for i in range(1,k+1):
        for j in range(n+1):
            dp[i][j] = dp[i-1][j]*(n-k+1+i-1)//(i)
            dp[i][j] %= mod
    for i in range(1,k+1):
        print(dp[i][n])
