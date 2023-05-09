def dfs(x, y):
    if x < 0 or x >= 2001 or y < 0 or y >= 2001:
        return
    if not (x, y) in grid:
        return
    if visited[(x, y)]:
        return
    visited[(x, y)] = True
    dfs(x - 1, y - 1)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    dfs(x + 1, y)
    dfs(x + 1, y + 1)
n = int(input())
grid = set()
visited = {}
for _ in range(n):
    x, y = map(int, input().split())
    grid.add((x + 1000, y + 1000))
    visited[(x + 1000, y + 1000)] = False
ans = 0
for x, y in grid:
    if not visited[(x, y)]:
        dfs(x, y)
        ans += 1
print(ans)
