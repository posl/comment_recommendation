def main():
    H, W, K = map(int, input().split())
    dp = [[0 for i in range(W)] for j in range(H+1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            for k in range(2**(W-1)):
                if ("11" in bin(k)):
                    continue
                if (j > 0 and (k & (1 << (j-1)))):
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j-1] %= 1000000007
                elif (j < W-1 and (k & (1 << j))):
                    dp[i+1][j+1] += dp[i][j]
                    dp[i+1][j+1] %= 1000000007
                else:
                    dp[i+1][j] += dp[i][j]
                    dp[i+1][j] %= 1000000007
    print(dp[H][K-1])

if __name__ == '__main__':
    main()