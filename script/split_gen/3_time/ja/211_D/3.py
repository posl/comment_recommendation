def main():
    N, M = map(int, input().split())
    if M == 0:
        print(0)
        return
    if N == 2:
        print(1)
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    dist = [-1]*N
    dist[0] = 0
    q = [0]
    while len(q) > 0:
        v = q.pop(0)
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    if dist[-1] == -1:
        print(0)
        return
    ans = 1
    for d in dist:
        if d == 2:
            ans *= len(G[d])
    print(ans%(10**9+7))
