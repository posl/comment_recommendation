def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i == 0 and j == 0:
                continue
            elif C[i][j] == '#':
                dp[i][j] = 0
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    print(dp[H-1][W-1] % 1000000007)

if __name__ == '__main__':
    main()