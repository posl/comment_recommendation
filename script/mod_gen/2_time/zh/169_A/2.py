def dfs(v):
    global flag
    visited[v] = True
    for next_v in G[v]:
        if visited[next_v]:
            continue
        dfs(next_v)
    if flag:
        return
    if v == 1:
        flag = True
        return
    for next_v in G[v]:
        if flag:
            return
        if visited[next_v]:
            continue
        visited[next_v] = True
        ans[next_v] = v
        dfs(next_v)
        visited[next_v] = False
        ans[next_v] = 0
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)
flag = False
visited = [False] * (N+1)
ans = [0] * (N+1)
dfs(2)
