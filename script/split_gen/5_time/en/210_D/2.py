def main():
    H, W, C = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    ans = 10**18
    for _ in range(2):
        dp = [[10**18] * (W+1) for _ in range(H+1)]
        for i in range(H):
            for j in range(W):
                dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1]) + C
                ans = min(ans, dp[i+1][j+1] + A[i][j])
        A = A[::-1]
    print(ans)
