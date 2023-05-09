def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A-1].append(B-1)
        G[B-1].append(A-1)
    MOD = 10**9 + 7
    dist = [-1] * N
    dist[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    if dist[N-1] == -1:
        print(0)
        return
    cnt = [0] * N
    cnt[N-1] = 1
    q = [N-1]
    while q:
        v = q.pop()
        for nv in G[v]:
            if dist[nv] != dist[v] - 1:
                continue
            cnt[nv] += cnt[v]
            cnt[nv] %= MOD
            q.append(nv)
    print(cnt[0])
