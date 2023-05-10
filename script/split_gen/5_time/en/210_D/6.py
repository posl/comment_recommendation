def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 10 ** 20
    dp = [[10 ** 20] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i > 0:
                ans = min(ans, dp[i - 1][j] + c + a[i][j])
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + c, a[i][j])
            if j > 0:
                ans = min(ans, dp[i][j - 1] + c + a[i][j])
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + c, a[i][j])
    dp = [[10 ** 20] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i > 0:
                ans = min(ans, dp[i - 1][j] + c + a[i][j])
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + c, a[i][j])
            if j < w - 1:
                ans = min(ans, dp[i][j + 1] + c + a[i][j])
                dp[i][j] = min(dp[i][j], dp[i][j + 1] + c, a[i][j])
    print(ans)
