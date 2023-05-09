def bfs(maze, sx, sy, gx, gy):
    # 迷路のマスを4方向に移動するベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 各マスの最短距離を保持する配列
    dist = [[float("inf")] * W for i in range(H)]
    dist[sx][sy] = 0
    # 移動するマスを管理するキュー
    queue = []
    queue.append([sx, sy])
    while len(queue) > 0:
        p = queue.pop(0)
        if p[0] == gx and p[1] == gy:
            break
        # 移動するマスの周囲を探索
        for i in range(4):
            nx = p[0] + dx[i]
            ny = p[1] + dy[i]
            # 移動できるマスか判定
            if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] != "#" and dist[nx][ny] == float("inf"):
                queue.append([nx, ny])
                dist[nx][ny] = dist[p[0]][p[1]] + 1
    return dist[gx][gy]
H, W = map(int, input().split())
maze = [list(input()) for i in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == "#":
            continue
        dist = bfs(maze, i, j, i, j)
        ans = max(ans, dist)
print(ans)

if __name__ == '__main__':
    bfs()