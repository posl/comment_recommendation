def main():
    S = int(input())
    mod = 10**9+7
    dp = [[0]*(S+1) for i in range(S+1)]
    dp[0][0] = 1
    for i in range(3, S+1):
        for j in range(S+1):
            if i+j <= S:
                dp[i][j+i] = (dp[i][j+i] + dp[i-1][j])%mod
            dp[i][j] = (dp[i][j] + dp[i-1][j])%mod
    print(dp[S][S])
