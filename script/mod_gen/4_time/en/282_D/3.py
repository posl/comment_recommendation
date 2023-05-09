def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        graph[a].append(b)
        graph[b].append(a)
    from collections import deque
    def bfs(s):
        q = deque([s])
        dist = [None] * N
        dist[s] = 0
        while q:
            v = q.popleft()
            for nv in graph[v]:
                if dist[nv] is not None:
                    continue
                dist[nv] = dist[v] + 1
                q.append(nv)
        return dist
    d0 = bfs(0)
    d1 = bfs(N - 1)
    c0 = sum(1 for x in d0 if x % 2 == 0)
    c1 = N - c0
    ans = c0 * c1 - M
    print(ans)

if __name__ == '__main__':
    main()