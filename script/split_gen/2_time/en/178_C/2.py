def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[0]*10 for _ in range(N+1)]
    dp[1] = [1]*10
    for i in range(2,N+1):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]
        for j in range(1,9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[N])%MOD)
