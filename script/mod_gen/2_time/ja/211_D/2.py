def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    G = [[] for _ in range(N+1)]
    for a, b in AB:
        G[a].append(b)
        G[b].append(a)
    INF = 10**9
    dist = [INF for _ in range(N+1)]
    dist[1] = 0
    que = [1]
    while que:
        v = que.pop(0)
        for nv in G[v]:
            if dist[nv] > dist[v] + 1:
                dist[nv] = dist[v] + 1
                que.append(nv)
    if dist[N] == INF:
        print(0)
        return
    cnt = 0
    que = [N]
    while que:
        v = que.pop(0)
        for nv in G[v]:
            if dist[nv] == dist[v] - 1:
                cnt += 1
                que.append(nv)
    print(cnt)

if __name__ == '__main__':
    main()