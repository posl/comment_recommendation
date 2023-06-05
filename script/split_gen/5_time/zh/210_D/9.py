def main():
    h, w, c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    # 从左上角开始，计算到达每个点的最小值
    dp = [[float("inf")] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + c)
            if j - 1 >= 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + c)
            dp[i][j] = min(dp[i][j], a[i][j])
    # 从右下角开始，计算到达每个点的最小值
    ans = float("inf")
    for i in reversed(range(h)):
        for j in reversed(range(w)):
            if i + 1 < h:
                ans = min(ans, dp[i + 1][j] + c + a[i][j])
            if j + 1 < w:
                ans = min(ans, dp[i][j + 1] + c + a[i][j])
            ans = min(ans, a[i][j])
    print(ans)
