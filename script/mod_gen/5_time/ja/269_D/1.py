def dfs(x, y):
    if x < 0 or x >= 2000 or y < 0 or y >= 2000:
        return
    if grid[x][y] == 0:
        return
    if visited[x][y]:
        return
    visited[x][y] = True
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
N = int(input())
grid = [[0] * 2000 for _ in range(2000)]
visited = [[False] * 2000 for _ in range(2000)]
for _ in range(N):
    x, y = map(int, input().split())
    x += 1000
    y += 1000
    grid[x][y] = 1
ans = 0
for x in range(2000):
    for y in range(2000):
        if grid[x][y] == 0 or visited[x][y]:
            continue
        ans += 1
        dfs(x, y)
print(ans)

if __name__ == '__main__':
    dfs()