def dfs(v, p):
    for u in G[v]:
        if u == p:
            continue
        ans.append(u)
        dfs(u, v)
        ans.append(v)
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
ans = [0]
dfs(0, -1)
print(*[i+1 for i in ans])
