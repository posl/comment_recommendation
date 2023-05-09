def main():
    N = int(input())
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3] = 1
    MOD = 10 ** 9 + 7
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if (j, k, l) == (0, 1, 2) or (j, k, l) == (0, 2, 1) or (j, k, l) == (1, 0, 2) or (j, k, l) == (2, 0, 1):
                        continue
                    if (j, k, l) == (1, 2, 0) or (j, k, l) == (2, 1, 0):
                        dp[i + 1][k][l] += dp[i][j][k]
                    else:
                        dp[i + 1][k][l] += dp[i][j][k]
                        dp[i + 1][k][l] += dp[i][j][k]
    ans = 0
    for j in range(4):
        for k in range(4):
            ans += dp[N][j][k]
    print(ans % MOD)

if __name__ == '__main__':
    main()