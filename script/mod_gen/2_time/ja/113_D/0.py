def main():
    H, W, K = map(int, input().split())
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if w == 0:
                dp[h + 1][w] = dp[h][w] + dp[h][w + 1]
            elif w == W - 1:
                dp[h + 1][w] = dp[h][w - 1] + dp[h][w]
            else:
                dp[h + 1][w] = dp[h][w - 1] + dp[h][w] + dp[h][w + 1]
    print(dp[H][K - 1] % (10 ** 9 + 7))

if __name__ == '__main__':
    main()