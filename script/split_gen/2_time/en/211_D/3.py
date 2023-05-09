def main():
    N, M = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    MOD = 10 ** 9 + 7
    from collections import deque
    Q = deque([0])
    dist = [-1] * N
    dist[0] = 0
    cnt = [0] * N
    cnt[0] = 1
    while Q:
        v = Q.popleft()
        for nv in G[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                cnt[nv] = cnt[v]
                Q.append(nv)
            elif dist[nv] == dist[v] + 1:
                cnt[nv] += cnt[v]
                cnt[nv] %= MOD
    print(cnt[N - 1])
