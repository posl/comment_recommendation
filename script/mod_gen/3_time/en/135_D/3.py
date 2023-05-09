def main():
    S = input()
    MOD = 10**9 + 7
    N = len(S)
    dp = [[0] * 13 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(10):
            for k in range(13):
                dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
        if S[i] != '?':
            for k in range(13):
                dp[i + 1][k] = dp[i + 1][(k * 10 + int(S[i])) % 13]
        for k in range(13):
            dp[i + 1][k] %= MOD
    print(dp[N][5])

if __name__ == '__main__':
    main()