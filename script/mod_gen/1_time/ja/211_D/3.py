def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N+1)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)
    MOD = 10**9 + 7
    INF = 10**18
    dist = [INF] * (N+1)
    cnt = [0] * (N+1)
    dist[1] = 0
    cnt[1] = 1
    Q = [1]
    while Q:
        v = Q.pop()
        for nv in G[v]:
            if dist[nv] == INF:
                dist[nv] = dist[v] + 1
                cnt[nv] = cnt[v]
                Q.append(nv)
            elif dist[nv] == dist[v] + 1:
                cnt[nv] += cnt[v]
                cnt[nv] %= MOD
    print(cnt[N])

if __name__ == '__main__':
    main()