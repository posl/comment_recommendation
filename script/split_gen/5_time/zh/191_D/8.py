def count_points(x, y, r):
    # 网格点数
    points = 0
    # 网格点坐标
    x0 = int(x)
    y0 = int(y)
    # 半径
    r2 = r * r
    # 遍历网格点
    for x in range(x0 - int(r), x0 + int(r) + 1):
        for y in range(y0 - int(r), y0 + int(r) + 1):
            # 判断网格点是否在圆内
            if (x - x0) * (x - x0) + (y - y0) * (y - y0) <= r2:
                points += 1
    return points
