def dfs(x,y):
    visited[x][y] = 1
    for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
        nx,ny = x+dx,y+dy
        if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '.' and visited[nx][ny] == 0:
            dfs(nx,ny)
    return
H,W = map(int,input().split())
S = [list(input()) for _ in range(H)]
res = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            visited = [[0]*W for _ in range(H)]
            dfs(i,j)
            res = max(res,sum([sum(visited[i]) for i in range(H)]))
print(res)
