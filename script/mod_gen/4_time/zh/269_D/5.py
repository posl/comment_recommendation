def dfs(x,y):
    if x<0 or x>=1000 or y<0 or y>=1000:
        return
    if not f[x][y]:
        return
    f[x][y]=0
    dfs(x-1,y-1)
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    dfs(x+1,y)
    dfs(x+1,y+1)
n=int(input())
f=[[0]*1000 for i in range(1000)]
for i in range(n):
    x,y=map(int,input().split())
    x+=500
    y+=500
    f[x][y]=1
ans=0
for i in range(1000):
    for j in range(1000):
        if f[i][j]:
            ans+=1
            dfs(i,j)
print(ans)

if __name__ == '__main__':
    dfs()