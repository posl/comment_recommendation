def dfs(v):
    visited[v] = True
    for i in G[v]:
        if not visited[i]:
            dfs(i)
N,M = map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
visited = [False]*N
ans = 0
for i in range(N):
    if not visited[i]:
        dfs(i)
        ans += 1
print(ans-1)
