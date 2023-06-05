def main():
    # 读入数据
    n = int(input())
    point = []
    for i in range(n):
        point.append(list(map(int, input().split())))
    # 做出所有的直线
    line = []
    for i in range(n):
        for j in range(i + 1, n):
            if point[i][0] == point[j][0]:
                # 与y轴平行
                line.append([float('inf'), point[i][0]])
            else:
                # 普通情况
                k = (point[i][1] - point[j][1]) / (point[i][0] - point[j][0])
                b = point[i][1] - k * point[i][0]
                line.append([k, b])
    # 统计斜率相同的直线的数量
    line.sort()
    ans = 0
    cnt = 0
    for i in range(len(line)):
        if i == 0 or line[i] != line[i - 1]:
            ans += cnt * (cnt - 1) // 2
            cnt = 1
        else:
            cnt += 1
    ans += cnt * (cnt - 1) // 2
    print(ans)
