def f(h, w, s):
    # 找到两个棋子的位置
    x1, y1, x2, y2 = 0, 0, 0, 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                if x1 == 0:
                    x1, y1 = i, j
                else:
                    x2, y2 = i, j
    # 棋子移动的方向
    d = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 棋子移动的步数
    step = [[-1 for j in range(w)] for i in range(h)]
    step[x1][y1] = 0
    # 棋子移动的队列
    que = []
    que.append([x1, y1])
    while que:
        x, y = que.pop(0)
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if s[nx][ny] == '-':
                continue
            if step[nx][ny] == -1:
                step[nx][ny] = step[x][y] + 1
                que.append([nx, ny])
    return step[x2][y2] - 1
h, w = map(int, input().split())
s = [input() for i in range(h)]
print(f(h, w, s))
