def dfs(x,y):
    if (x,y) in visited:
        return
    visited.add((x,y))
    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0),(1,-1),(-1,1)]:
        if (x+dx,y+dy) in black:
            dfs(x+dx,y+dy)
n = int(input())
black = set()
for _ in range(n):
    x,y = map(int,input().split())
    black.add((x,y))
visited = set()
ans = 0
for x,y in black:
    if (x,y) in visited:
        continue
    ans += 1
    dfs(x,y)
print(ans)
