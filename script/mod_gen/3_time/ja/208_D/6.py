def main():
    import sys
    from heapq import heappush, heappop
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, M, *ABCD = map(int, read().split())
    INF = 10 ** 18
    G = [[] for _ in range(N)]
    for a, b, c in zip(*[iter(ABCD)] * 3):
        a -= 1
        b -= 1
        G[a].append((b, c))
    ans = 0
    for k in range(N):
        for s in range(N):
            dist = [INF] * N
            dist[s] = 0
            hq = [(0, s)]
            while hq:
                d, v = heappop(hq)
                if dist[v] < d:
                    continue
                for nv, w in G[v]:
                    if nv > k:
                        continue
                    if dist[nv] > d + w:
                        dist[nv] = d + w
                        heappush(hq, (dist[nv], nv))
            for t in range(N):
                if dist[t] < INF:
                    ans += dist[t]
    print(ans)

if __name__ == '__main__':
    main()