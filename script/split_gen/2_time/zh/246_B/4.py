def solve():
    # 读取输入
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    # 由于矩形的边与x轴或y轴平行，所以可以分别求出矩形的水平边和垂直边
    # 水平边的长度为x1-x2，垂直边的长度为y1-y2
    # 由于矩形的面积不为0，所以水平边和垂直边的长度不可能同时为0
    # 所以可以根据水平边和垂直边的长度来判断矩形的另外两个点的坐标
    if x1 == x2:
        x4 = x3
    elif x1 == x3:
        x4 = x2
    else:
        x4 = x1
    if y1 == y2:
        y4 = y3
    elif y1 == y3:
        y4 = y2
    else:
        y4 = y1
    # 输出结果
    print(x4, y4)
