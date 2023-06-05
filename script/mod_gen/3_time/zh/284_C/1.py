def dfs(i):
    visited[i]=True
    for j in range(n):
        if visited[j]==False and G[i][j]:
            dfs(j)
n,m=map(int,input().split())
G=[[False]*n for i in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    u-=1
    v-=1
    G[u][v]=G[v][u]=True
visited=[False]*n
ans=0
for i in range(n):
    if visited[i]==False:
        dfs(i)
        ans+=1
print(ans)

if __name__ == '__main__':
    dfs()