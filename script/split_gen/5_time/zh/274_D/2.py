def check(x, y, a):
    # 从第一个点开始
    px, py = 0, 0
    for i in range(len(a)):
        # 取得下一个点的坐标
        nx, ny = px + a[i], py
        # 如果是奇数个点，下一个点的y坐标与上一个点相同
        if i % 2 == 0:
            ny = -ny
        # 如果是偶数个点，下一个点的y坐标与上一个点相同
        else:
            ny = ny
        # 判断下一个点是否在坐标轴上
        if nx == x and ny == y:
            return True
        # 更新当前点坐标
        px, py = nx, ny
    return False
