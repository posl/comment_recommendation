def main():
    import sys
    from collections import defaultdict
    from collections import deque
    input = sys.stdin.readline
    M = int(input())
    edges = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    pieces = list(map(int, input().split()))
    if pieces == list(range(1, 9)):
        print(0)
        return
    if M == 0:
        print(-1)
        return
    for i in range(1, 10):
        if i not in edges:
            edges[i] = []
    def bfs(s):
        dist = [-1] * 10
        dist[s] = 0
        queue = deque([s])
        while queue:
            v = queue.popleft()
            for nv in edges[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    queue.append(nv)
        return dist
    dists = [bfs(i) for i in range(1, 10)]
    def dfs(bits, v, d):
        if bits == 0:
            return d
        res = float('inf')
        for nv in edges[v]:
            if (bits >> (nv - 1)) & 1 == 0:
                continue
            res = min(res, dfs(bits ^ (1 << (nv - 1)), nv, d + dists[v][nv]))
        return res
    print(dfs((1 << 8) - 1, pieces.index(9) + 1, 0))

if __name__ == '__main__':
    main()