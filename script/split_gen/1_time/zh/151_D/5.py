def dfs(i,j):
    global maxv
    if i<0 or h<=i or j<0 or w<=j or maze[i][j]=='#':
        return
    if maxv < dist[i][j]:
        maxv = dist[i][j]
    if dist[i][j] != 0:
        return
    dist[i][j] = dist[i][j] + 1
    dfs(i+1,j)
    dfs(i-1,j)
    dfs(i,j+1)
    dfs(i,j-1)
    dist[i][j] = dist[i][j] - 1
    return
h,w = map(int,input().split())
maze = [list(input()) for i in range(h)]
dist = [[0 for i in range(w)] for i in range(h)]
maxv = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            dfs(i,j)
print(maxv)
