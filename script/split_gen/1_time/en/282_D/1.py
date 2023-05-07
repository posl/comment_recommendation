def main():
    N, M = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].add(v)
        G[v].add(u)
    ans = 0
    for u in range(N):
        for v in range(u + 1, N):
            if v in G[u]:
                continue
            if len(G[u] & G[v]) == 0:
                ans += 1
    print(ans)
