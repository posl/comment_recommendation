def main():
    h, w, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    # 1. 从左上角开始，计算以每个点为终点的最小值
    # 2. 从右下角开始，计算以每个点为终点的最小值
    # 3. 两个最小值相加，计算以每个点为终点的最小值，取最小值
    INF = 10 ** 18
    dp1 = [[INF] * w for _ in range(h)]
    dp2 = [[INF] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if i > 0:
                dp1[i][j] = min(dp1[i][j], dp1[i - 1][j])
            if j > 0:
                dp1[i][j] = min(dp1[i][j], dp1[i][j - 1])
            dp1[i][j] = min(dp1[i][j], a[i][j] - c * (i + j))
    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if i < h - 1:
                dp2[i][j] = min(dp2[i][j], dp2[i + 1][j])
            if j < w - 1:
                dp2[i][j] = min(dp2[i][j], dp2[i][j + 1])
            dp2[i][j] = min(dp2[i][j], a[i][j] - c * (i + j))
    ans = INF
    for i in range(h):
        for j in range(w):
            ans = min(ans, dp1[i][j] + dp2[i][j] + c * (i + j) + a[i][j])
    print(ans)
