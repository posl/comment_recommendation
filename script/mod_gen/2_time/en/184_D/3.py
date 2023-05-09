def main():
    a, b, c = map(int, input().split())
    dp = [[[0] * 100 for _ in range(100)] for _ in range(100)]
    dp[a][b][c] = 1
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if i + j + k == 0:
                    continue
                s = i + j + k
                dp[i][j][k] *= s
                if i > 0:
                    dp[i - 1][j][k] += dp[i][j][k]
                if j > 0:
                    dp[i + 1][j - 1][k] += dp[i][j][k]
                if k > 0:
                    dp[i][j + 1][k - 1] += dp[i][j][k]
    ans = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if i + j + k == 0:
                    continue
                s = i + j + k
                ans += dp[i][j][k] / s * (s / (s - 1))
    print(ans)

if __name__ == '__main__':
    main()