def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + (1 if A[i][j] == "+" else -1)) if i > 0 else 0
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + (1 if A[i][j] == "+" else -1)) if j > 0 else 0
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] - (1 if A[i][j] == "+" else -1)) if i > 0 else 0
                dp[i][j] = min(dp[i][j], dp[i][j - 1] - (1 if A[i][j] == "+" else -1)) if j > 0 else 0
    if dp[H - 1][W - 1] > 0:
        print("Takahashi")
    elif dp[H - 1][W - 1] == 0:
        print("Draw")
    else:
        print("Aoki")
