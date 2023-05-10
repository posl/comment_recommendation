def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
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
    for c, d in CD:
        if (dist[c - 1] + dist[d - 1]) % 2 == 0:
            print('Town')
        else:
            print('Road')

if __name__ == '__main__':
    main()