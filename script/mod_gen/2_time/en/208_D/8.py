def main():
    import sys
    from heapq import heappush, heappop
    N, M = map(int, sys.stdin.readline().split())
    AB = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
    C = [int(sys.stdin.readline()) for _ in range(M)]
    AB = [(a-1, b-1, c) for a, b, c in zip(*[iter(AB)]*2)]
    AB = [AB[i] + (i,) for i in range(M)]
    AB.sort(key=lambda x: x[2])
    ans = 0
    for i in range(M):
        a, b, c, _ = AB[i]
        dist = [[float('inf') for _ in range(N)] for _ in range(N)]
        for j in range(N):
            dist[j][j] = 0
        for j in range(i):
            a2, b2, c2, _ = AB[j]
            dist[a2][b2] = c2
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    dist[k][l] = min(dist[k][l], dist[k][j] + dist[j][l])
        for j in range(N):
            for k in range(N):
                if dist[j][k] != float('inf'):
                    ans += dist[j][k]
    print(ans)

if __name__ == '__main__':
    main()