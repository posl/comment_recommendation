def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    print(S)
    # 棋子的位置
    pos = []
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                pos.append([i, j])
    print(pos)
    # 4个方向
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    ans = -1
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                continue
            # 从每个位置出发，计算到达棋子的最短距离
            dist = [[-1] * W for _ in range(H)]
            dist[i][j] = 0
            que_x = []
            que_y = []
            que_x.append(i)
            que_y.append(j)
            while len(que_x) > 0:
                x = que_x.pop(0)
                y = que_y.pop(0)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx and nx < H and 0 <= ny and ny < W and S[nx][ny] != '#' and dist[nx][ny] == -1:
                        que_x.append(nx)
                        que_y.append(ny)
                        dist[nx][ny] = dist[x][y] + 1
            # 从每个位置出发，计算到达另一个棋子的最短距离
            d = dist[pos[1][0]][pos[1][1]]
            if d == -1:
                continue
            if ans == -1 or ans > d + 1:
                ans = d + 1
    print(ans)
