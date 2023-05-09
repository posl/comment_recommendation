def main():
    H, W, K = map(int, input().split())
    dp = [[0] * (W + 2) for _ in range(H + 1)]
    dp[0][1] = 1
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            for i in range(1 << (W - 1)):
                if i & (i << 1):
                    continue
                if i & (1 << (w - 1)):
                    dp[h][w - 1] += dp[h - 1][w]
                    dp[h][w - 1] %= 10**9 + 7
                elif (i >> (w - 1)) & 1:
                    dp[h][w + 1] += dp[h - 1][w]
                    dp[h][w + 1] %= 10**9 + 7
                else:
                    dp[h][w] += dp[h - 1][w]
                    dp[h][w] %= 10**9 + 7
    print(dp[H][K])

if __name__ == '__main__':
    main()