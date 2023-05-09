def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                if S[i] == '?':
                    for l in range(3):
                        dp[i + 1][j][k] += dp[i][j][k]
                        dp[i + 1][j][k] %= MOD
                        dp[i + 1][l][j] += dp[i][j][k]
                        dp[i + 1][l][j] %= MOD
                else:
                    dp[i + 1][j][k] += dp[i][j][k]
                    dp[i + 1][j][k] %= MOD
                    dp[i + 1][int(S[i])][j] += dp[i][j][k]
                    dp[i + 1][int(S[i])][j] %= MOD
    print(dp[N][3][3])
main()

if __name__ == '__main__':
    main()