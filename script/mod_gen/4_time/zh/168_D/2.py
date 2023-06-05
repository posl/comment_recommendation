def dfs(node, parent):
    global G, ans
    for i in G[node]:
        if i == parent:
            continue
        if ans[i] != 0:
            continue
        ans[i] = node
        dfs(i, node)
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)
ans = [0] * (N+1)
ans[1] = 1
dfs(1, -1)
