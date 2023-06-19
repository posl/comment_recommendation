def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 从每个点出发，求到其他所有点的最短距离
    INF = 1000000007
    d = [[INF] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            d[i][j] = 0
            q = [(i, j)]
            while q:
                x, y = q.pop(0)
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.' and d[nx][ny] == INF:
                        d[nx][ny] = d[x][y] + 1
                        q.append((nx, ny))
    res = 0
    for i in range(H):
        for j in range(W):
            if d[i][j] == INF:
                continue
            res = max(res, d[i][j])
    return res
print(solve())
