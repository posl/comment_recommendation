def dfs(x,y):
    global max_length
    #print("x,y",x,y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #print("nx,ny",nx,ny)
        if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] == "." and not seen[nx][ny]:
            seen[nx][ny] = True
            dfs(nx,ny)
            seen[nx][ny] = False
        else:
            max_length = max(max_length, sum(sum(seen,[])))
H,W = map(int,input().split())
maze = [list(input()) for _ in range(H)]
seen = [[False]*W for _ in range(H)]
max_length = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(H):
    for j in range(W):
        if maze[i][j] == ".":
            seen[i][j] = True
            dfs(i,j)
            seen[i][j] = False
print(max_length)
