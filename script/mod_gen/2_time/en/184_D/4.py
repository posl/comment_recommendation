def main():
    A, B, C = map(int, input().split())
    N = A + B + C
    dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
    dp[A][B][C] = 1
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            for k in range(N-1, -1, -1):
                if i == 0 and j == 0 and k == 0:
                    continue
                dp[i][j][k] = (i * dp[i+1][j][k] + j * dp[i][j+1][k] + k * dp[i][j][k+1]) / (i + j + k)
                if i > 0:
                    dp[i][j][k] += dp[i-1][j][k] / (i + j + k)
                if j > 0:
                    dp[i][j][k] += dp[i][j-1][k] / (i + j + k)
                if k > 0:
                    dp[i][j][k] += dp[i][j][k-1] / (i + j + k)
                dp[i][j][k] += 1
    print(dp[0][0][0])

if __name__ == '__main__':
    main()