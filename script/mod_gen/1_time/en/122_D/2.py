def main():
    N = int(input())
    dp = [[[0] * 4 for _ in range(4)] for _ in range(N + 1)]
    dp[0][3][3] = 1
    mod = 10 ** 9 + 7
    for i in range(N):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j == 0 and k == 1 and l == 2:
                        continue
                    if j == 0 and k == 2 and l == 1:
                        continue
                    if j == 1 and k == 0 and l == 2:
                        continue
                    if j == 1 and k == 2 and l == 0:
                        continue
                    if j == 2 and k == 0 and l == 1:
                        continue
                    if j == 2 and k == 1 and l == 0:
                        continue
                    dp[i + 1][k][l] += dp[i][j][k]
                    dp[i + 1][k][l] %= mod
    print(sum(sum(dp[N][i]) for i in range(4)) % mod)

if __name__ == '__main__':
    main()