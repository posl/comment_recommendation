def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                continue
            dist = [[-1] * W for _ in range(H)]
            dist[i][j] = 0
            queue = [(i, j)]
            for x, y in queue:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < H and 0 <= ny < W):
                        continue
                    if S[nx][ny] == '#':
                        continue
                    if dist[nx][ny] == -1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))
            ans = max(ans, max(max(row) for row in dist))
    print(ans)

if __name__ == '__main__':
    solve()