def main():
    N = int(input())
    MOD = 10**9 + 7
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        if (a, b, c, d) == (0, 1, 2, 3): continue
                        if (a, b, c, d) == (0, 2, 1, 3): continue
                        if (a, b, c, d) == (0, 2, 3, 1): continue
                        if (a, b, c, d) == (2, 0, 1, 3): continue
                        dp[i + 1][d][a][b] += dp[i][a][b][c]
                        dp[i + 1][d][a][b] %= MOD
    ans = 0
    for a in range(4):
        for b in range(4):
            for c in range(4):
                ans += dp[N][a][b][c]
                ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()