def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N, Q = map(int, input().split())
    G = defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    X = [0] * (N+1)
    for _ in range(Q):
        p, x = map(int, input().split())
        X[p] += x
    ans = [0] * (N+1)
    def dfs(v, p):
        ans[v] += X[v]
        for u in G[v]:
            if u == p: continue
            X[u] += X[v]
            dfs(u, v)
    dfs(1, -1)
    print(*ans[1:])
