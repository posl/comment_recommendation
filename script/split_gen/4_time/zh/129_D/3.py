def light_num(h, w, s):
    # 从左往右，从上往下
    # 左右方向
    left = [[0] * w for i in range(h)]
    right = [[0] * w for i in range(h)]
    # 上下方向
    up = [[0] * w for i in range(h)]
    down = [[0] * w for i in range(h)]
    # 左右方向
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                left[i][j] = 0
            elif j == 0:
                left[i][j] = 1
            else:
                left[i][j] = left[i][j-1] + 1
    for i in range(h):
        for j in range(w-1, -1, -1):
            if s[i][j] == '#':
                right[i][j] = 0
            elif j == w-1:
                right[i][j] = 1
            else:
                right[i][j] = right[i][j+1] + 1
    # 上下方向
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                up[i][j] = 0
            elif i == 0:
                up[i][j] = 1
            else:
                up[i][j] = up[i-1][j] + 1
    for i in range(h-1, -1, -1):
        for j in range(w):
            if s[i][j] == '#':
                down[i][j] = 0
            elif i == h-1:
                down[i][j] = 1
            else:
                down[i][j] = down[i+1][j] + 1
    # 计算最大值
    max_num = 0
    for i in range(h):
        for j in range(w):
            max_num = max(max_num, left[i][j]+right[i][j]+up[i][j]+down[i][j]-3)
    return max_num
