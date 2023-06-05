def dfs(x, y, d):
    global ans
    ans = max(ans, d)
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '.' and not used[nx][ny]:
            used[nx][ny] = True
            dfs(nx, ny, d + 1)
            used[nx][ny] = False
h, w = map(int, input().split())
s = [input() for _ in range(h)]
dxy = ((-1, 0), (1, 0), (0, -1), (0, 1))
ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            used = [[False] * w for _ in range(h)]
            used[i][j] = True
            dfs(i, j, 0)
print(ans)

if __name__ == '__main__':
    dfs()