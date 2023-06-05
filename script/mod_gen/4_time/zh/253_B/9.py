def solve():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    INF = 10 ** 18
    ans = INF
    for i in range(H):
        for j in range(W):
            if S[i][j] == 'o':
                continue
            dist = [[INF] * W for _ in range(H)]
            dist[i][j] = 0
            q = [(i, j)]
            while q:
                y, x = q.pop(0)
                for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    ny = y + dy
                    nx = x + dx
                    if ny < 0 or ny >= H or nx < 0 or nx >= W:
                        continue
                    if S[ny][nx] == '-':
                        continue
                    if dist[ny][nx] != INF:
                        continue
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))
            for i2 in range(H):
                for j2 in range(W):
                    if S[i2][j2] == 'o':
                        ans = min(ans, dist[i2][j2] - 1)
    print(ans)

if __name__ == '__main__':
    solve()