def main():
    n = int(input())
    dp = [[[0] * 4 for _ in range(4)] for _ in range(n + 1)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i == 0 and j == 2 and k == 1:
                    continue
                if i == 0 and j == 1 and k == 2:
                    continue
                if i == 2 and j == 0 and k == 1:
                    continue
                if i == 0 and j == 2 and k == 0:
                    continue
                if i == 2 and j == 0 and k == 2:
                    continue
                dp[3][i][j] += 1
    for i in range(4, n + 1):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if j == 0 and k == 2 and l == 1:
                        continue
                    if j == 0 and k == 1 and l == 2:
                        continue
                    if j == 2 and k == 0 and l == 1:
                        continue
                    if j == 0 and k == 2 and l == 0:
                        continue
                    if j == 2 and k == 0 and l == 2:
                        continue
                    dp[i][j][k] += dp[i - 1][k][l]
                    dp[i][j][k] %= 1000000007
    ans = 0
    for i in range(4):
        for j in range(4):
            ans += dp[n][i][j]
    print(ans % 1000000007)

if __name__ == '__main__':
    main()