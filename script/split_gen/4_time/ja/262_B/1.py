def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    ans = 0
    for u in range(N):
        for v in G[u]:
            for w in G[v]:
                if w == u:
                    ans += 1
    print(ans // 6)
