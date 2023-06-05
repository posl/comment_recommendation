def dfs(i,j):
    global maxv
    if i<0 or i>=h or j<0 or j>=w or maze[i][j] == '#':
        return
    if maxv < dist[i][j]:
        maxv = dist[i][j]
    if dist[i][j] != -1:
        return
    dist[i][j] = dist[i][j]+1
    dfs(i+1,j)
    dfs(i-1,j)
    dfs(i,j+1)
    dfs(i,j-1)
    dist[i][j] = dist[i][j]-1
h,w = map(int,input().split())
maze = [list(input()) for i in range(h)]
dist = [[-1]*w for i in range(h)]
maxv = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            dfs(i,j)
print(maxv)

if __name__ == '__main__':
    dfs()