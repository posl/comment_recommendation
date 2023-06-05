def solve(h, w, s):
    # 两个棋子的位置
    p = []
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                p.append([i, j])
    # 棋子间的距离
    d = abs(p[0][0]-p[1][0]) + abs(p[0][1]-p[1][1])
    # 棋子间的位置
    p1 = p[0][0] + p[0][1]
    p2 = p[1][0] + p[1][1]
    if d == 1:
        return 1
    elif d == 2:
        if p1 % 2 == 0 or p2 % 2 == 0:
            return 1
        else:
            return 2
    elif d == 3:
        if p1 % 2 == 0 or p2 % 2 == 0:
            return 2
        else:
            return 3
    elif d == 4:
        if p1 % 2 == 0 or p2 % 2 == 0:
            return 2
        else:
            return 3
    else:
        return 3

if __name__ == '__main__':
    solve()