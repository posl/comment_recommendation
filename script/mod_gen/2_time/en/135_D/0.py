def main():
    S = input()
    N = len(S)
    MOD = 10 ** 9 + 7
    dp = [[0] * 13 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(13):
            if S[i] == '?':
                for k in range(10):
                    dp[i + 1][(j * 10 + k) % 13] += dp[i][j]
                    dp[i + 1][(j * 10 + k) % 13] %= MOD
            else:
                dp[i + 1][(j * 10 + int(S[i])) % 13] += dp[i][j]
                dp[i + 1][(j * 10 + int(S[i])) % 13] %= MOD
    print(dp[N][5])

if __name__ == '__main__':
    main()