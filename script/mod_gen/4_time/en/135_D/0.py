def main():
    S = input()
    N = len(S)
    MOD = 10 ** 9 + 7
    dp = [[0] * 13 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        if S[i] == "?":
            for j in range(10):
                for k in range(13):
                    dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
                    dp[i + 1][(k * 10 + j) % 13] %= MOD
        else:
            j = int(S[i])
            for k in range(13):
                dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
                dp[i + 1][(k * 10 + j) % 13] %= MOD
    print(dp[N][5])

if __name__ == '__main__':
    main()