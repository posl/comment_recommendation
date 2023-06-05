def dfs(v):
    global ans
    global flag
    if flag == False:
        return
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            ans[i-1] = v
            dfs(i)
        else:
            if ans[v-1] != i:
                flag = False
                return
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
ans = [0] * (n+1)
flag = True
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1)
