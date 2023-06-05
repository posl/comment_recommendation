def dfs(x,y,step):
    global max_step
    if x==H-1 and y==W-1:
        if max_step<step:
            max_step=step
        return
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<H and 0<=ny<W and S[nx][ny]=="." and visited[nx][ny]==False:
            visited[nx][ny]=True
            dfs(nx,ny,step+1)
            visited[nx][ny]=False
H,W=map(int,input().split())
S=[list(input()) for _ in range(H)]
visited=[[False]*W for _ in range(H)]
max_step=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]
visited[0][0]=True
dfs(0,0,1)
print(max_step)

if __name__ == '__main__':
    dfs()