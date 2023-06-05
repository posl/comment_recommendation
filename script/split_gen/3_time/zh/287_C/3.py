def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    for i in range(N):
        G[i].sort()
    for i in range(N):
        if len(G[i]) == 2:
            continue
        if len(G[i]) == 0:
            print("No")
            return
        if len(G[i]) == 1:
            if len(G[G[i][0]]) == 1:
                print("No")
                return
    print("Yes")
