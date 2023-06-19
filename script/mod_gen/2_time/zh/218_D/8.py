def get_count_of_rectangles(points):
    # 1. 从所有点中找出位于x轴上的点
    # 2. 从所有点中找出位于y轴上的点
    # 3. 算出每个x轴上的点和y轴上的点的组合
    # 4. 算出每个组合能组成的矩形个数
    # 5. 累加每个组合的矩形个数
    # 6. 返回累加的结果
    count = 0
    points_on_x = []
    points_on_y = []
    for point in points:
        if point[1] == 0:
            points_on_x.append(point)
        if point[0] == 0:
            points_on_y.append(point)
    for point_on_x in points_on_x:
        for point_on_y in points_on_y:
            if (point_on_x[0], point_on_y[1]) in points and (point_on_y[0], point_on_x[1]) in points:
                count += 1
    return count

if __name__ == '__main__':
    get_count_of_rectangles()