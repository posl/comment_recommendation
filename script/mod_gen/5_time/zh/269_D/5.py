def dfs(x,y):
    if x < 0 or x >= 2000 or y < 0 or y >= 2000:
        return
    if graph[x][y] == 0:
        return
    if visited[x][y]:
        return
    visited[x][y] = True
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)
n = int(input())
graph = [[0 for _ in range(2000)] for _ in range(2000)]
visited = [[False for _ in range(2000)] for _ in range(2000)]
for _ in range(n):
    x,y = map(int,input().split())
    x += 1000
    y += 1000
    graph[x][y] = 1
ans = 0
for i in range(2000):
    for j in range(2000):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i,j)
            ans += 1
print(ans)

if __name__ == '__main__':
    dfs()