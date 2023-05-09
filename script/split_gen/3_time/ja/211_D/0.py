def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    dist = [None] * N
    dist[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv in G[v]:
            if dist[nv] is None:
                dist[nv] = dist[v] + 1
                q.append(nv)
    if dist[-1] is None:
        print(0)
        return
    cnt = 0
    for v in G[-1]:
        if dist[v] == dist[-1] - 1:
            cnt += 1
    print(cnt)
