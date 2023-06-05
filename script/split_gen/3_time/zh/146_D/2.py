def dfs(v, p, c):
    global ans
    k = 1
    for u in G[v]:
        if u == p:
            continue
        if k == c:
            k += 1
        ans[u] = k
        k += 1
        dfs(u, v, ans[u])
N = int(input())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
ans = [0] * N
dfs(0, -1, -1)
print(max(ans))
for i in range(N - 1):
    print(ans[i])
