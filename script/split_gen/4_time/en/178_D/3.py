def main():
    S = int(input())
    MOD = 10**9 + 7
    dp = [[0] * (S+1) for _ in range(S+1)]
    dp[0][0] = 1
    for i in range(1, S+1):
        for j in range(S+1):
            dp[i][j] = dp[i-1][j]
            if j >= i:
                dp[i][j] += dp[i][j-i]
                dp[i][j] %= MOD
    print(dp[S][S])
