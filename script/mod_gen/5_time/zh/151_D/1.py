def bfs(S, start, goal):
    INF = 10 ** 9
    H, W = len(S), len(S[0])
    dist = [[INF] * W for _ in range(H)]
    dist[start[0]][start[1]] = 0
    que = []
    que.append(start)
    while que:
        y, x = que.pop(0)
        for dy, dx in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= H or nx < 0 or nx >= W:
                continue
            if S[ny][nx] == '#':
                continue
            if dist[ny][nx] != INF:
                continue
            dist[ny][nx] = dist[y][x] + 1
            que.append((ny, nx))
    return dist[goal[0]][goal[1]]
H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue
        ans = max(ans, bfs(S, (i, j), (i, j)))
print(ans)

if __name__ == '__main__':
    bfs()