def dfs(x,y):
    global maxv
    if x < 0 or x >= h or y < 0 or y >= w:
        return
    if maze[x][y] == '#':
        return
    if maxv < dist[x][y]:
        maxv = dist[x][y]
    if dist[x][y] != -1:
        return
    dist[x][y] = dist[px][py] + 1
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    dist[x][y] = -1
h,w = map(int,input().split())
maze = [input() for i in range(h)]
dist = [[-1]*w for i in range(h)]
maxv = 0
for i in range(h):
    for j in range(w):
        if maze[i][j] == '.':
            px = i
            py = j
            dfs(i,j)
print(maxv)

if __name__ == '__main__':
    dfs()