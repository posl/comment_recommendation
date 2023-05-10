def solve(h, w, c_h, c_w, d_h, d_w, s):
    INF = 10 ** 9
    dist = [[INF] * w for _ in range(h)]
    dist[c_h - 1][c_w - 1] = 0
    q = [(c_h - 1, c_w - 1)]
    while q:
        i, j = q.pop(0)
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if not (0 <= ni < h and 0 <= nj < w):
                continue
            if s[ni][nj] == "#":
                continue
            if dist[ni][nj] <= dist[i][j]:
                continue
            dist[ni][nj] = dist[i][j]
            q.append((ni, nj))
        for di in range(-2, 3):
            for dj in range(-2, 3):
                ni, nj = i + di, j + dj
                if not (0 <= ni < h and 0 <= nj < w):
                    continue
                if s[ni][nj] == "#":
                    continue
                if dist[ni][nj] <= dist[i][j] + 1:
                    continue
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
    return dist[d_h - 1][d_w - 1] if dist[d_h - 1][d_w - 1] < INF else -1
h, w = map(int, input().split())
c_h, c_w = map(int, input().split())
d_h, d_w = map(int, input().split())
s = [input() for _ in range(h)]
print(solve(h, w, c_h, c_w, d_h, d_w, s))
