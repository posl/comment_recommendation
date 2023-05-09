def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    dp = [[0] * 13 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(13):
            if S[i] == '?':
                for k in range(10):
                    dp[i + 1][(j * 10 + k) % 13] += dp[i][j]
            else:
                k = int(S[i])
                dp[i + 1][(j * 10 + k) % 13] += dp[i][j]
            dp[i + 1][(j * 10 + k) % 13] %= MOD
    print(dp[N][5])
