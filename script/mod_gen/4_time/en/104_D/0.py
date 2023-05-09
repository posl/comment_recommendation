def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    dp = [[0] * 4 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(4):
            if S[i] == "?":
                dp[i + 1][j] += dp[i][j] * 3
                dp[i + 1][j] %= MOD
                if j < 3:
                    dp[i + 1][j + 1] += dp[i][j]
                    dp[i + 1][j + 1] %= MOD
            else:
                if j < 3 and S[i] == "ABC"[j]:
                    dp[i + 1][j + 1] += dp[i][j]
                    dp[i + 1][j + 1] %= MOD
    print(dp[N][3])

if __name__ == '__main__':
    main()