def dfs(x,y):
    global ans
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<h and 0<=ny<w and s[nx][ny]=='.' and not check[nx][ny]:
            check[nx][ny]=True
            dfs(nx,ny)
            check[nx][ny]=False
            ans=max(ans,check.count(True))
h,w=map(int,input().split())
s=[input() for _ in range(h)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
ans=0
for i in range(h):
    for j in range(w):
        if s[i][j]=='.':
            check=[[False]*w for _ in range(h)]
            check[i][j]=True
            dfs(i,j)
print(ans)
