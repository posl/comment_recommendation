def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(N+1)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if (i, j, k) == (0, 1, 2) or (i, j, k) == (0, 2, 1) or (i, j, k) == (1, 0, 2):
                    continue
                dp[3][i][j] += 1
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if (i, j, k) == (0, 1, 2) or (i, j, k) == (0, 2, 1) or (i, j, k) == (1, 0, 2):
                    continue
                for l in range(4):
                    if (j, k, l) == (0, 1, 2) or (j, k, l) == (0, 2, 1) or (j, k, l) == (1, 0, 2):
                        continue
                    dp[4][i][j] += dp[3][j][k]
                    dp[4][i][j] %= MOD
    for i in range(5, N+1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if (j, k, l) == (0, 1, 2) or (j, k, l) == (0, 2, 1) or (j, k, l) == (1, 0, 2):
                        continue
                    dp[i][j][k] += dp[i-1][j][k]
                    dp[i][j][k] %= MOD
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[N][i][j]
            ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()