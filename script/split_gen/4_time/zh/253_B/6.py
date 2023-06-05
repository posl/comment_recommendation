def main():
    h, w = map(int, input().split())
    grid = [list(input()) for _ in range(h)]
    def bfs(sy, sx):
        dist = [[-1] * w for _ in range(h)]
        dist[sy][sx] = 0
        q = [(sy, sx)]
        while q:
            y, x = q.pop(0)
            for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < h and 0 <= nx < w):
                    continue
                if grid[ny][nx] == '#':
                    continue
                if dist[ny][nx] != -1:
                    continue
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
        return dist
    res = 0
    for sy in range(h):
        for sx in range(w):
            if grid[sy][sx] == '#':
                continue
            dist = bfs(sy, sx)
            for gy in range(h):
                for gx in range(w):
                    if grid[gy][gx] == '#':
                        continue
                    res = max(res, dist[gy][gx])
    print(res)
