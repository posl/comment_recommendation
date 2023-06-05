def main():
    N = int(input())
    mod = 998244353
    dp = [[0 for i in range(10)] for j in range(N+1)]
    dp[1][0] = 0
    for i in range(1,10):
        dp[1][i] = 1
    for i in range(2,N+1):
        dp[i][0] = (dp[i-1][1] + dp[i-1][0])%mod
        for j in range(1,9):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1] + dp[i-1][j])%mod
        dp[i][9] = (dp[i-1][8] + dp[i-1][9])%mod
    res = 0
    for i in range(0,10):
        res = (res + dp[N][i])%mod
    print(res)
