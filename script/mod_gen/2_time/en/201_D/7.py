def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    dp = [[0] * (W + 1) for _ in range(H + 1)]
    for h in range(H - 1, -1, -1):
        for w in range(W - 1, -1, -1):
            if (h + w) % 2 == 0:
                if a[h][w] == '+':
                    dp[h][w] = max(dp[h][w], dp[h + 1][w] + 1)
                    dp[h][w] = max(dp[h][w], dp[h][w + 1] + 1)
                else:
                    dp[h][w] = max(dp[h][w], dp[h + 1][w] - 1)
                    dp[h][w] = max(dp[h][w], dp[h][w + 1] - 1)
            else:
                if a[h][w] == '+':
                    dp[h][w] = min(dp[h][w], dp[h + 1][w] - 1)
                    dp[h][w] = min(dp[h][w], dp[h][w + 1] - 1)
                else:
                    dp[h][w] = min(dp[h][w], dp[h + 1][w] + 1)
                    dp[h][w] = min(dp[h][w], dp[h][w + 1] + 1)
    if dp[0][0] == 0:
        print('Draw')
    elif dp[0][0] > 0:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()