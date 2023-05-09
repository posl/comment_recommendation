def main():
    A, B, C = map(int, input().split())
    dp = [[[0] * 100 for _ in range(100)] for _ in range(100)]
    dp[A][B][C] = 1
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if i + j + k == 0:
                    continue
                dp[i][j][k] *= (i + j + k)
                if i > 0:
                    dp[i - 1][j][k] += dp[i][j][k]
                if j > 0:
                    dp[i + 1][j - 1][k] += dp[i][j][k]
                if k > 0:
                    dp[i][j + 1][k - 1] += dp[i][j][k]
                dp[i][j][k] /= (i + j + k)
    ans = 0
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if i + j + k == 0:
                    continue
                ans += dp[i][j][k] * (i + j + k)
    print(ans)

if __name__ == '__main__':
    main()