def main():
    S = input()
    MOD = 10 ** 9 + 7
    N = len(S)
    dp = [[0] * 9 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(9):
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
            if S[i] == 'c' and j == 0:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
            if S[i] == 'h' and j == 1:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
            if S[i] == 'o' and j == 2:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
            if S[i] == 'k' and j == 3:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
            if S[i] == 'u' and j == 4:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
            if S[i] == 'd' and j == 5:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
            if S[i] == 'a' and j == 6:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
            if S[i] == 'i' and j == 7:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= MOD
    print(dp[N][8])
