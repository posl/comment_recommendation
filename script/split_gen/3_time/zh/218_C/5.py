def rotate90(data):
    # 逆时针旋转90度
    n = len(data)
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j] = data[j][n - i - 1]
    return res
