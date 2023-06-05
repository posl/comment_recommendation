def dfs(x,y):
    if x<0 or x>=h or y<0 or y>=w or maze[x][y]=="#":
        return
    maze[x][y]="#"
    for i in range(4):
        dfs(x+dx[i],y+dy[i])
h,w=map(int,input().split())
maze=[list(input()) for i in range(h)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]
ans=0
for i in range(h):
    for j in range(w):
        if maze[i][j]==".":
            dfs(i,j)
            ans+=1
print(ans-1)

if __name__ == '__main__':
    dfs()