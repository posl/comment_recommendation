def problems112_c():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        x_i, y_i, h_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        h.append(h_i)
    # 从高度最高的点开始遍历，找到第一个高度不为0的点，即为中心点
    for i in range(N):
        if h[i] != 0:
            center_x = x[i]
            center_y = y[i]
            height = h[i]
            break
    # 从中心点开始遍历，判断每个点的高度是否满足条件
    for i in range(101):
        for j in range(101):
            # 如果该点高度为0，则跳过
            if h[i] == 0:
                continue
            # 如果该点的高度不等于height-|i-center_x|-|j-center_y|，则跳过
            if h[i] != height - abs(i-center_x) - abs(j-center_y):
                continue
            # 如果该点的高度等于height-|i-center_x|-|j-center_y|，则继续判断
            if h[i] == height - abs(i-center_x) - abs(j-center_y):
                continue
    print(center_x, center_y, height)
problems112_c()
