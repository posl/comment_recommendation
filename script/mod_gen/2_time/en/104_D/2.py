def main():
    S = input()
    N = len(S)
    MOD = 10**9 + 7
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    for i in range(N):
        if S[i] == "?":
            for j in range(4):
                for k in range(4):
                    for l in range(1, 4):
                        dp[i + 1][j][l] += dp[i][j][k]
                        dp[i + 1][j][l] %= MOD
                        dp[i + 1][k][l] += dp[i][j][k]
                        dp[i + 1][k][l] %= MOD
        else:
            for j in range(4):
                for k in range(4):
                    l = "ABC".index(S[i]) + 1
                    dp[i + 1][j][l] += dp[i][j][k]
                    dp[i + 1][j][l] %= MOD
                    dp[i + 1][k][l] += dp[i][j][k]
                    dp[i + 1][k][l] %= MOD
    ans = 0
    for j in range(4):
        for k in range(4):
            ans += dp[N][j][k]
            ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()