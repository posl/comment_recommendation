def dfs(x, y):
    global ans
    ans = max(ans, dist[x][y])
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < h and 0 <= ny < w): continue
        if a[nx][ny] == "#": continue
        if dist[nx][ny] != -1: continue
        dist[nx][ny] = dist[x][y] + 1
        dfs(nx, ny)
        dist[nx][ny] = -1
h, w = map(int, input().split())
a = [input() for _ in range(h)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == "#": continue
        dist = [[-1] * w for _ in range(h)]
        dist[i][j] = 0
        dfs(i, j)
print(ans)

if __name__ == '__main__':
    dfs()