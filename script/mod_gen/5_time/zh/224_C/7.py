def solve():
    # 读入数据
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    # 计算所有点对的斜率
    slopes = {}
    for i in range(N):
        for j in range(i+1, N):
            slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
            if slope not in slopes:
                slopes[slope] = []
            slopes[slope].append((i, j))
    # 统计斜率相同的点对个数
    ans = 0
    for slope in slopes:
        n = len(slopes[slope])
        ans += n * (n - 1) // 2
    print(ans)
solve()
