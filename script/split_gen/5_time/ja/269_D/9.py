def dfs(x, y):
    if x < 0 or x >= 2001 or y < 0 or y >= 2001:
        return
    if c[y][x]:
        return
    c[y][x] = True
    dfs(x - 1, y - 1)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    dfs(x + 1, y)
    dfs(x + 1, y + 1)
n = int(input())
c = [[False] * 2001 for _ in range(2001)]
for _ in range(n):
    x, y = map(int, input().split())
    x += 1000
    y += 1000
    c[y][x] = True
ans = 0
for y in range(2001):
    for x in range(2001):
        if not c[y][x]:
            continue
        if c[y - 1][x - 1] or c[y - 1][x] or c[y][x - 1] or c[y][x + 1] or c[y + 1][x] or c[y + 1][x + 1]:
            continue
        ans += 1
        dfs(x, y)
print(ans)
