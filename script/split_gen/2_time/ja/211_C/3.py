def main():
    S = input()
    MOD = 10**9 + 7
    N = len(S)
    dp = [[0] * 9 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(9):
            if S[i] == "chokudai"[j]:
                dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j] += dp[i][j]
            dp[i + 1][j] %= MOD
    print(dp[N][8])
