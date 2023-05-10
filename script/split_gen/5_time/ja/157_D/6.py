def dfs(x):
    visited[x] = True
    for y in graph[x]:
        if visited[y]:
            continue
        dfs(y)
n,m,k=map(int,input().split())
graph=[[] for _ in range(n)]
visited=[False]*n
for _ in range(m):
    a,b=map(int,input().split())
    a-=1
    b-=1
    graph[a].append(b)
    graph[b].append(a)
for _ in range(k):
    c,d=map(int,input().split())
    c-=1
    d-=1
    graph[c].append(d)
    graph[d].append(c)
for i in range(n):
    if visited[i]:
        continue
    dfs(i)
ans=[0]*n
for i in range(n):
    for j in graph[i]:
        if visited[j]:
            continue
        ans[i]+=1
print(*ans)
