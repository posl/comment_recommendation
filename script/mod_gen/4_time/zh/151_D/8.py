def dfs(i,j):
    global ans
    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if ni < 0 or ni >= h or nj < 0 or nj >= w:
            continue
        if maze[ni][nj] == "#":
            continue
        if seen[ni][nj] == True:
            continue
        seen[ni][nj] = True
        dfs(ni,nj)
        seen[ni][nj] = False
    ans = max(ans,sum(seen,[]))
h,w = map(int,input().split())
maze = [list(input()) for _ in range(h)]
seen = [[False]*w for _ in range(h)]
ans = 0
dx = [1,0,-1,0]
dy = [0,1,0,-1]
for i in range(h):
    for j in range(w):
        if maze[i][j] == "#":
            continue
        seen[i][j] = True
        dfs(i,j)
        seen[i][j] = False
print(ans-1)

if __name__ == '__main__':
    dfs()