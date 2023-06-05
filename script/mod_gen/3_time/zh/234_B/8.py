def main():
    # 读入数据
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    # 求最大距离
    maxd = 0
    for i in range(n):
        for j in range(i + 1, n):
            d = ((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2) ** 0.5
            if d > maxd:
                maxd = d
    # 输出结果
    print(maxd)

if __name__ == '__main__':
    main()