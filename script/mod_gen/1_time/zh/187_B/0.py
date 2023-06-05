def solve():
    # 读入数据
    N = int(input())
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    # 斜率的范围是[-1, 1]，即-1 <= (y2 - y1) / (x2 - x1) <= 1
    # 两边同时乘以(x2 - x1)，则-1 * (x2 - x1) <= y2 - y1 <= 1 * (x2 - x1)
    # 移项得-1 * (x2 - x1) - y2 + y1 <= 0 <= 1 * (x2 - x1) - y2 + y1
    # 所以对于每个点，只要找到与其连线的斜率在[-1, 1]的点的数目即可
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if -1 * (x2 - x1) - y2 + y1 <= 0 <= 1 * (x2 - x1) - y2 + y1:
                count += 1
    print(count)

if __name__ == '__main__':
    solve()