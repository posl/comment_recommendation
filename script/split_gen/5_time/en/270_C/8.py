def dfs(v):
    for i in range(len(edges[v])):
        if edges[v][i][0] == 0:
            edges[v][i][0] = 1
            dfs(edges[v][i][1])
            ans.append(edges[v][i][1])
            break
n,x,y = map(int,input().split())
edges = [[] for _ in range(n+1)]
for i in range(n-1):
    u,v = map(int,input().split())
    edges[u].append([0,v])
    edges[v].append([0,u])
ans = []
dfs(x)
ans.append(x)
ans.reverse()
dfs(y)
print(*ans)
