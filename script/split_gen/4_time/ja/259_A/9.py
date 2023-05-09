def calcHeight(n, m, x, t, d):
    # 0歳からx歳までの伸びた身長
    h = 0
    for i in range(1, x + 1):
        h = h + d
    # x歳からn歳までの身長
    for i in range(x + 1, n + 1):
        h = h + t
    # m歳の身長を求める
    if m <= x:
        for i in range(1, m):
            h = h - d
    else:
        for i in range(x + 1, m):
            h = h - t
    return h
