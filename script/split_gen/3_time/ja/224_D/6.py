def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    M = int(input())
    G = [[] for _ in range(9)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    p = list(map(int, input().split()))
    p = [i-1 for i in p]
    p = [i for i in range(9) if i not in p] + p
    def bfs(s, d):
        dist = [-1]*9
        dist[s] = 0
        q = deque([s])
        while q:
            v = q.popleft()
            for u in G[v]:
                if dist[u] == -1:
                    dist[u] = dist[v] + 1
                    q.append(u)
        return dist[d]
    ans = 0
    for i in range(8):
        d = bfs(p[i], p[i+1])
        if d == -1:
            print(-1)
            return
        ans += d
    print(ans)
