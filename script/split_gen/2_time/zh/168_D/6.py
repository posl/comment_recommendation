def dfs(i):
    global flag
    if flag:
        return
    if visited[i]:
        if visited[i] == 1:
            flag = True
            return
    else:
        visited[i] = 1
        for j in edge[i]:
            dfs(j)
        visited[i] = 2
        ans.append(i)
        return
n,m = map(int,input().split())
edge = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    edge[a].append(b)
visited = [0]*(n+1)
flag = False
ans = []
for i in range(1,n+1):
    if not visited[i]:
        dfs(i)
