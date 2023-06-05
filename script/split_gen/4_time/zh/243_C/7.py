def collision():
    # 读取输入
    N = int(input())
    XY = []
    for i in range(N):
        XY.append(list(map(int, input().split())))
    S = input()
    # 转换方向
    for i in range(len(S)):
        if S[i] == 'L':
            XY[i][0] *= -1
        else:
            XY[i][1] *= -1
    # 排序
    XY.sort(key=lambda x: (x[0], x[1]))
    # 判断是否碰撞
    for i in range(1, len(XY)):
        if XY[i][0] == XY[i - 1][0] and XY[i][1] == XY[i - 1][1]:
            return 'Yes'
    return 'No'
