def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    mod = 10 ** 9 + 7
    def bfs():
        q = [0]
        dist = [-1] * N
        dist[0] = 0
        cnt = [0] * N
        cnt[0] = 1
        while q:
            v = q.pop()
            for nv in G[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    q.append(nv)
                if dist[nv] == dist[v] + 1:
                    cnt[nv] += cnt[v]
                    cnt[nv] %= mod
        return cnt[N - 1]
    print(bfs())

if __name__ == '__main__':
    main()