def main():
    A, B, C = map(int, input().split())
    dp = [[[0 for _ in range(100)] for _ in range(100)] for _ in range(100)]
    for i in range(99):
        for j in range(99):
            for k in range(99):
                dp[i][j][k] = (dp[i][j][k] + dp[i+1][j][k] + dp[i][j+1][k] + dp[i][j][k+1] + 3) * (i+j+k) / (i+j+k+3)
    print(dp[A][B][C])

if __name__ == '__main__':
    main()