def solve():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    max_cnt = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            # スタート地点を決める
            start = (i, j)
            # ゴール地点を決める
            for k in range(H):
                for l in range(W):
                    if S[k][l] == '#':
                        continue
                    goal = (k, l)
                    # BFSで最短距離を求める
                    dist = [[-1] * W for _ in range(H)]
                    dist[start[0]][start[1]] = 0
                    queue = [start]
                    while queue:
                        x, y = queue.pop(0)
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx = x + dx
                            ny = y + dy
                            if not (0 <= nx < H and 0 <= ny < W):
                                continue
                            if S[nx][ny] == '#':
                                continue
                            if dist[nx][ny] != -1:
                                continue
                            dist[nx][ny] = dist[x][y] + 1
                            queue.append((nx, ny))
                    max_cnt = max(max_cnt, dist[goal[0]][goal[1]])
    print(max_cnt)
