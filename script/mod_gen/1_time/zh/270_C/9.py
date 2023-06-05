def dfs(u,p):
    global ans
    ans.append(u)
    for v in G[u]:
        if v!=p:
            dfs(v,u)
            ans.append(u)
n,x,y=map(int,input().split())
x-=1
y-=1
G=[[] for _ in range(n)]
for _ in range(n-1):
    u,v=map(int,input().split())
    u-=1
    v-=1
    G[u].append(v)
    G[v].append(u)
ans=[]
dfs(x,-1)
ans.append(y)
print(*[i+1 for i in ans])

if __name__ == '__main__':
    dfs()