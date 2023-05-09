def main():
    N = int(input())
    MOD = 10 ** 9 + 7
    dp = [[[[0] * 4 for _ in range(4)] for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3][3] = 1
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    for m in range(4):
                        if j == 0 and k == 1 and m == 2:
                            continue
                        if j == 0 and k == 2 and m == 1:
                            continue
                        if j == 1 and k == 0 and m == 2:
                            continue
                        if j == 1 and k == 2 and m == 0:
                            continue
                        if j == 2 and k == 0 and m == 1:
                            continue
                        if j == 2 and k == 1 and m == 0:
                            continue
                        if l == 0 and k == 1 and m == 2:
                            continue
                        dp[i + 1][k][l][m] += dp[i][j][k][l]
                        dp[i + 1][k][l][m] %= MOD
    ans = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                ans += dp[N][i][j][k]
                ans %= MOD
    print(ans)

if __name__ == '__main__':
    main()