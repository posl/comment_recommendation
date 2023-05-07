def main():
    H, W, K = map(int, input().split())
    MOD = 1000000007
    dp = [[0] * W for _ in range(H+1)]
    dp[0][0] = 1
    for h in range(H):
        for i in range(2**(W-1)):
            if '11' in bin(i):
                continue
            for j in range(W):
                if j > 0 and i & (1 << (j-1)):
                    dp[h+1][j-1] += dp[h][j]
                    dp[h+1][j-1] %= MOD
                elif j < W-1 and i & (1 << j):
                    dp[h+1][j+1] += dp[h][j]
                    dp[h+1][j+1] %= MOD
                else:
                    dp[h+1][j] += dp[h][j]
                    dp[h+1][j] %= MOD
    print(dp[H][K-1])

if __name__ == '__main__':
    main()