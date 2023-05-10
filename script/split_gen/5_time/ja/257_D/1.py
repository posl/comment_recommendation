def main():
    from collections import defaultdict
    from heapq import heappush, heappop
    import sys
    input = sys.stdin.readline
    N = int(input())
    P = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        P.append((x, y, p))
    def check(S):
        G = defaultdict(list)
        for i in range(N):
            x, y, p = P[i]
            G[i].append((i, S*p))
            for j in range(i+1, N):
                x2, y2, p2 = P[j]
                G[i].append((j, abs(x-x2)+abs(y-y2)))
                G[j].append((i, abs(x-x2)+abs(y-y2)))
        q = [(0, 0)]
        dist = [float('inf')] * N
        dist[0] = 0
        while q:
            d, v = heappop(q)
            if dist[v] < d:
                continue
            for u, c in G[v]:
                if dist[u] > dist[v] + c:
                    dist[u] = dist[v] + c
                    heappush(q, (dist[u], u))
        return dist[-1] < float('inf')
    ok = 0
    ng = 10**18
    while ng - ok > 1:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
