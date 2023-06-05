def dfs(v,p):
    for u in g[v]:
        if u==p:continue
        print(u,end=' ')
        dfs(u,v)
        print(v,end=' ')
n=int(input())
g=[[]for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
print(1,end=' ')
dfs(0,-1)
print()

if __name__ == '__main__':
    dfs()