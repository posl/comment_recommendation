def main():
    MOD = 10**9 + 7
    S = input()
    N = len(S)
    dp = [[0] * 9 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(9):
            if j == 8:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = dp[i][j] + dp[i][j+1]
    print(dp[N][0] % MOD)
