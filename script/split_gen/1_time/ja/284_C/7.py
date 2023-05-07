def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    u = [0] * (M + 1)
    v = [0] * (M + 1)
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    G = [[] for i in range(N + 1)]
    for i in range(M):
        G[u[i]].append(v[i])
        G[v[i]].append(u[i])
    seen = [False] * (N + 1)
    def dfs(v):
        seen[v] = True
        for nv in G[v]:
            if seen[nv]:
                continue
            dfs(nv)
    ans = 0
    for v in range(1, N + 1):
        if seen[v]:
            continue
        dfs(v)
        ans += 1
    print(ans)
