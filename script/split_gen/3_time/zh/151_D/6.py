def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    # 从每个点开始，寻找到其他每个点的最短距离
    from collections import deque
    def bfs(sy, sx):
        dist = [[-1] * W for _ in range(H)]
        dist[sy][sx] = 0
        q = deque([(sy, sx)])
        while q:
            y, x = q.popleft()
            for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                ny, nx = y + dy, x + dx
                if not (0 <= ny < H and 0 <= nx < W): continue
                if S[ny][nx] == '#': continue
                if dist[ny][nx] != -1: continue
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
        return dist
    dists = [bfs(sy, sx) for sy in range(H) for sx in range(W)]
    ans = 0
    for i in range(H * W):
        for j in range(i + 1, H * W):
            if dists[i // W][i % W][j // W][j % W] == -1: continue
            ans = max(ans, dists[i // W][i % W][j // W][j % W])
    print(ans)
solve()
