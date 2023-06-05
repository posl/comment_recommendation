def solve():
    N, M = map(int, input().split())
    a = [0] * M
    b = [0] * M
    for i in range(M):
        a[i], b[i] = map(int, input().split())
        a[i] -= 1
        b[i] -= 1
    G = [[] for _ in range(N)]
    for i in range(M):
        G[a[i]].append(b[i])
        G[b[i]].append(a[i])
    V = [False] * N
    def dfs(v):
        V[v] = True
        for i in range(len(G[v])):
            if V[G[v][i]] == False:
                dfs(G[v][i])
    ans = 0
    for i in range(N):
        if V[i] == False:
            dfs(i)
            ans += 1
    print(ans - 1)
