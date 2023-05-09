def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * (W+1) for _ in range(H+1)]
    for h in range(H):
        for w in range(W):
            if (h + w) % 2 == 0:
                dp[h+1][w+1] = max(dp[h][w+1] + (1 if A[h][w] == "+" else -1), dp[h+1][w] + (1 if A[h][w] == "+" else -1))
            else:
                dp[h+1][w+1] = min(dp[h][w+1] - (1 if A[h][w] == "+" else -1), dp[h+1][w] - (1 if A[h][w] == "+" else -1))
    if dp[H][W] > 0:
        print("Takahashi")
    elif dp[H][W] < 0:
        print("Aoki")
    else:
        print("Draw")
