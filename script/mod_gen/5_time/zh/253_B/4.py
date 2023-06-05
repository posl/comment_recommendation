def main():
    H, W = map(int, input().split())
    S = []
    for i in range(H):
        S.append(input())
    # 从左上角开始，找到两个棋子的位置
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                x1, y1 = i, j
                break
        else:
            continue
        break
    for i in reversed(range(H)):
        for j in reversed(range(W)):
            if S[i][j] == 'o':
                x2, y2 = i, j
                break
        else:
            continue
        break
    # 从左上角开始，计算到达两个棋子的最短距离
    # 从左上角开始，计算到达两个棋子的最短距离
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dist = [[-1] * W for _ in range(H)]
    dist[x1][y1] = 0
    que_x = []
    que_y = []
    que_x.append(x1)
    que_y.append(y1)
    while len(que_x) > 0:
        x = que_x.pop(0)
        y = que_y.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < H and 0 <= ny < W and S[nx][ny] != '#' and dist[nx][ny] == -1):
                que_x.append(nx)
                que_y.append(ny)
                dist[nx][ny] = dist[x][y] + 1
    print(dist[x2][y2])

if __name__ == '__main__':
    main()