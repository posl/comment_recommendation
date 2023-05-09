def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if (h + w) % 2 == 0:
                if h == 0 and w == 0:
                    dp[h][w] = 1 if A[h][w] == '+' else -1
                elif h == 0:
                    dp[h][w] = dp[h][w - 1] + 1 if A[h][w] == '+' else dp[h][w - 1] - 1
                elif w == 0:
                    dp[h][w] = dp[h - 1][w] + 1 if A[h][w] == '+' else dp[h - 1][w] - 1
                else:
                    dp[h][w] = max(dp[h - 1][w] + 1 if A[h][w] == '+' else dp[h - 1][w] - 1,
                                   dp[h][w - 1] + 1 if A[h][w] == '+' else dp[h][w - 1] - 1)
            else:
                if h == 0 and w == 0:
                    dp[h][w] = -1 if A[h][w] == '+' else 1
                elif h == 0:
                    dp[h][w] = dp[h][w - 1] - 1 if A[h][w] == '+' else dp[h][w - 1] + 1
                elif w == 0:
                    dp[h][w] = dp[h - 1][w] - 1 if A[h][w] == '+' else dp[h - 1][w] + 1
                else:
                    dp[h][w] = min(dp[h - 1][w] - 1 if A[h][w] == '+' else dp[h - 1][w] + 1,
                                   dp[h][w - 1] - 1 if A[h][w] == '+' else dp[h][w - 1] + 1)
    if dp[H - 1][W - 1] > 0:
        print('Takahashi')
    elif dp
