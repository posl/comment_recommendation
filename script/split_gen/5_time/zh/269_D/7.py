def dfs(x,y):
    if x < -1000 or x > 1000 or y < -1000 or y > 1000:
        return
    if (x,y) in visited:
        return
    visited.add((x,y))
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)
N = int(input())
visited = set()
for _ in range(N):
    x,y = map(int,input().split())
    dfs(x,y)
print(len(visited))
