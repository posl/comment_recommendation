def main():
    N = int(input())
    E = [[int(x) for x in input().split()] for _ in range(N-1)]
    G = [[] for _ in range(N+1)]
    for a,b in E:
        G[a].append(b)
        G[b].append(a)
    C = [0] * (N+1)
    def dfs(v, p):
        c = 1
        for u in G[v]:
            if u == p: continue
            if c == C[v]: c += 1
            C[u] = c
            c += 1
            dfs(u, v)
    dfs(1, 0)
    print(max(C))
    for a,b in E:
        if C[a] < C[b]: a,b = b,a
        print(C[a])

if __name__ == '__main__':
    main()