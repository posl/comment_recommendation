def main():
    N, M = map(int, input().split())
    if M == 0:
        print(3 ** N)
        return
    AB = [list(map(int, input().split())) for _ in range(M)]
    AB = [[a - 1, b - 1] for a, b in AB]
    AB = [sorted(a) for a in AB]
    AB.sort()
    AB = [[a, b] for a, b in AB if AB.count([a, b]) == 1]
    M = len(AB)
    if M == 0:
        print(0)
        return
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)
    c = [0] * N
    def dfs(v, p):
        if c[v] != 0:
            return
        c[v] = p
        for u in G[v]:
            dfs(u, 3 - p)
    dfs(0, 1)
    for v in range(N):
        if c[v] == 0:
            print(0)
            return
    for v in range(N):
        for u in G[v]:
            if c[v] == c[u]:
                print(0)
                return
    print(3 ** (N - M))
main()
