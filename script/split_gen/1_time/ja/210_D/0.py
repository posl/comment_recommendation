def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = float('inf')
    for _ in range(2):
        dp = [[float('inf')] * W for _ in range(H)]
        for i in range(H):
            for j in range(W):
                dp[i][j] = min(dp[i][j], A[i][j])
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + C)
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + C)
        ans = min(ans, dp[H-1][W-1])
        A = A[::-1]
    print(ans)
