def dfs(x, y):
    global n, m, a
    a[x][y] = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1:
                dfs(nx, ny)
n = int(input())
m = 1000
a = [[0] * m for _ in range(n)]
for i in range(n):
    x, y = map(int, input().split())
    x += 500
    y += 500
    a[x][y] = 1
ans = 0
for i in range(m):
    for j in range(m):
        if a[i][j] == 1:
            dfs(i, j)
            ans += 1
print(ans)

if __name__ == '__main__':
    dfs()