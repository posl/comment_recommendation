def solve():
    N, M = map(int, input().split())
    if M != N - 1:
        print('No')
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    visited = [False] * N
    def dfs(u, p):
        visited[u] = True
        for v in G[u]:
            if v == p:
                continue
            if visited[v]:
                return False
            if not dfs(v, u):
                return False
        return True
    if not dfs(0, -1):
        print('No')
        return
    if not all(visited):
        print('No')
        return
    print('Yes')
solve()
