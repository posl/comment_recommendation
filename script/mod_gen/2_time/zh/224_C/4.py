def solve():
    # 读取输入
    N = int(input())
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))
    # 计算所有的点对之间的斜率
    # 用字典存储，key为斜率，value为斜率相同的点对的个数
    slopes = {}
    for i in range(N):
        for j in range(i + 1, N):
            slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
            if slope not in slopes:
                slopes[slope] = 1
            else:
                slopes[slope] += 1
    # 计算答案
    # 三个点可以组成三角形的条件是，这三个点两两之间的斜率不相同
    # 所以答案就是：(N-1) + (N-2) + ... + (N-k)，其中k是满足条件的斜率的个数
    ans = 0
    for slope in slopes:
        ans += slopes[slope] * (N - slopes[slope])
    # 输出答案
    print(ans // 2)

if __name__ == '__main__':
    solve()