Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    INF = 10 ** 15
    dp = [[INF] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for i in range(M):
        dp[A[i]][B[i]] = C[i]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if dp[i][j] <= dp[i][k] + dp[k][j]:
                    ans += dp[i][j]
    print(ans)

main()

=======
Suggestion 2

def floyd_warshall(n, d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    from collections import defaultdict
    d = defaultdict(list)
    for i in range(M):
        d[A[i]].append((B[i], C[i]))
    ans = 0
    for k in range(N):
        dist = [float('inf')] * N
        dist[k] = 0
        for i in range(N):
            for j in range(N):
                for v, c in d[j]:
                    if dist[j] + c < dist[v]:
                        dist[v] = dist[j] + c
        for i in range(N):
            if dist[i] != float('inf'):
                ans += dist[i]
    print(ans)
    return

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append((b, c))
        G[b].append((a, c))
    INF = 10**10
    ans = 0
    for k in range(N):
        dist = [INF for _ in range(N)]
        dist[k] = 0
        que = [(0, k)]
        while que:
            d, v = heapq.heappop(que)
            if dist[v] < d:
                continue
            for nv, nd in G[v]:
                if dist[nv] > d + nd:
                    dist[nv] = d + nd
                    heapq.heappush(que, (dist[nv], nv))
        for i in range(N):
            if i == k:
                continue
            ans += dist[i]
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    dist = [[float("inf")] * N for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for _ in range(M):
        A, B, C = map(int, input().split())
        dist[A - 1][B - 1] = C
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if dist[i][j] == dist[i][k] + dist[k][j]:
                    ans += dist[i][k]
    print(ans)

main()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    graph = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        graph[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a-1][b-1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if graph[i][k] + graph[k][j] == graph[i][j]:
                    ans += graph[i][j]
    print(ans)

=======
Suggestion 7

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

=======
Suggestion 8

def get_input():
    N, M = map(int, input().split())
    A = [0]*M
    B = [0]*M
    C = [0]*M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
    return N, M, A, B, C

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline
    
    class UnionFind():
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n
    
        def find(self, x):
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]
    
        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)
    
            if x == y:
                return
    
            if self.parents[x] > self.parents[y]:
                x, y = y, x
    
            self.parents[x] += self.parents[y]
            self.parents[y] = x
    
        def size(self, x):
            return -self.parents[self.find(x)]
    
        def same(self, x, y):
            return self.find(x) == self.find(y)
    
        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]
    
        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]
    
        def group_count(self):
            return len(self.roots())
    
        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}
    
        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
    
    N,M = map(int,input().split())
    uf = UnionFind(N)
    for _ in range(M):
        A,B,C = map(int,input().split())
        A -= 1
        B -= 1
        if A > B:
            A,B = B,A
        uf.union(A,B)
    d = {}
    for i in range(N):
        r = uf.find(i)
        if r in d:
            d[r] += 1
        else:
            d[r] = 1
    ans = 0
    for i in d:
        ans += d[i] * (d[i]-1) // 2
    print(ans)

=======
Suggestion 10

def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
    INF = 10 ** 18
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        dist[i][i] = 0
    for i in range(1, N + 1):
        q = deque()
        q.append(i)
        while q:
            v = q.popleft()
            for nv, c in graph[v]:
                if dist[i][nv] > dist[i][v] + c:
                    dist[i][nv] = dist[i][v] + c
                    q.append(nv)
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if dist[i][j] == dist[i][k] + dist[k][j]:
                    ans += dist[i][j]
                    break
    print(ans)
