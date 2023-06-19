def get_max_light_num(h, w, s):
    # 从上往下，从左往右，第一个遇到的#号的位置
    top = [[0] * w for _ in range(h)]
    left = [[0] * w for _ in range(h)]
    # 从下往上，从右往左，第一个遇到的#号的位置
    bottom = [[0] * w for _ in range(h)]
    right = [[0] * w for _ in range(h)]
    # 从上往下，从左往右，第一个遇到的#号的位置
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                top[i][j] = i
                left[i][j] = j
            elif i > 0:
                top[i][j] = top[i-1][j]
                left[i][j] = left[i][j-1] if j > 0 else 0
    # 从下往上，从右往左，第一个遇到的#号的位置
    for i in range(h-1, -1, -1):
        for j in range(w-1, -1, -1):
            if s[i][j] == '#':
                bottom[i][j] = i
                right[i][j] = j
            elif i < h - 1:
                bottom[i][j] = bottom[i+1][j]
                right[i][j] = right[i][j+1] if j < w - 1 else w - 1
    # 计算灯光的照射范围
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            ans = max(ans, bottom[i][j] - top[i][j] + right[i][j] - left[i][j] + 1)
    return ans
