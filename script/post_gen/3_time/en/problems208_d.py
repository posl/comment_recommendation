Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)

    # f(s,t,k) = min cost from s to t using only cities 1, 2, ..., k
    f = [[10**18] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        f[i][i] = 0
        f[i + 1][i + 1] = 0

    for i in range(M):
        a = A[i]
        b = B[i]
        c = C[i]
        f[a][b] = min(f[a][b], c)

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                f[i][j] = min(f[i][j], f[i][k] + f[k][j])

    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                ans += f[i][j]
    print(ans)

solve()

I’m not sure if this is the best solution, but it works. The solution is based on floyd-warshall algorithm. The time complexity is O(N^3) and the space complexity is O(N^2).

I also tried to solve this problem using Dijkstra’s algorithm, but it didn’t work. Here is my solution.

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    G = [[float('inf')] * N for _ in range(N)]
    for i in range(N):
        G[i][i] = 0
    for _ in range(M):
        A, B, C = map(int, input().split())
        G[A - 1][B - 1] = C
    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ans += G[i][k] if G[i][k] < float('inf') and G[i][k] == G[i][j] else 0
    print(ans)

solve()

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    G = [[float('inf')] * N for i in range(N)]
    for i in range(N):
        G[i][i] = 0
    for i in range(M):
        A, B, C = map(int, input().split())
        G[A-1][B-1] = C

    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])

    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if G[i][k] + G[k][j] == G[i][j]:
                    ans += G[i][j]
                    break
    print(ans)

=======
Suggestion 4

def main():
    import sys
    def input(): return sys.stdin.readline().strip()
    def list2d(a, b, c): return [[c] * b for i in range(a)]
    def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
    def list4d(a, b, c, d, e): return [[[[e] * d for j in range(c)] for j in range(b)] for i in range(a)]
    def ceil(x, y=1): return int(-(-x // y))
    def INT(): return int(input())
    def MAP(): return map(int, input().split())
    def LIST(N=None): return list(MAP()) if N is None else [INT() for i in range(N)]
    def Yes(): print('Yes')
    def No(): print('No')
    def YES(): print('YES')
    def NO(): print('NO')
    sys.setrecursionlimit(10 ** 9)
    INF = 10 ** 18
    MOD = 10**9 + 7

    N, M = MAP()
    G = list2d(N, N, INF)
    for i in range(N):
        G[i][i] = 0
    for i in range(M):
        a, b, c = MAP()
        a -= 1
        b -= 1
        G[a][b] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                G[i][j] = min(G[i][j], G[i][k] + G[k][j])

    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if G[i][j] == G[i][k] + G[k][j] and G[i][j] != INF:
                    ans += G[i][j]
    print(ans)

=======
Suggestion 5

def floyd_warshall(n, m, a, b, c):
    d = [[float("inf")] * n for i in range(n)]
    for i in range(n):
        d[i][i] = 0
    for i in range(m):
        d[a[i]][b[i]] = c[i]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

=======
Suggestion 6

def floyd_warshall(n, graph):
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i, j, w in graph:
        dist[i][j] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    road = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for s in range(1, N + 1):
        for t in range(1, N + 1):
            for k in range(1, N + 1):
                if s == t:
                    ans += 0
                else:
                    min_cost = 10**6 * N
                    for a, b, c in road:
                        if a > k:
                            continue
                        if a == s and b == t:
                            min_cost = min(min_cost, c)
                        elif a == s:
                            min_cost = min(min_cost, c + 0)
                    if min_cost == 10**6 * N:
                        ans += 0
                    else:
                        ans += min_cost
    print(ans)
    return

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    INF = 10**18
    D = [[INF] * N for _ in range(N)]
    for i in range(M):
        a, b, c = map(int, input().split())
        D[a-1][b-1] = c
    for i in range(N):
        D[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if D[i][j] == D[i][k] + D[k][j]:
                    ans += D[i][j]
                    break
    print(ans)

=======
Suggestion 9

def floyd_warshall(n, graph):
    # graph = [[-1 for j in range(n)] for i in range(n)]
    for i in range(n):
        graph[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == -1 or graph[k][j] == -1:
                    continue
                if graph[i][j] == -1 or graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

=======
Suggestion 10

def dijkstra(graph, start):
    """Dijkstra's algorithm for shortest paths.
    graph is a dictionary, where each key is a vertex and each value is a list of
    (vertex, distance) tuples. start is the starting vertex.
    """
    Q = set(graph)  # remaining vertices
    dist = dict.fromkeys(graph, float('inf'))  # distance from start
    dist[start] = 0
    while Q:
        u = min(Q, key=dist.get)  # vertex with smallest distance
        Q.remove(u)
        for v, d in graph[u].items():  # all neighbors of u
            if v in Q:
                dist[v] = min(dist[v], dist[u] + d)  # relax (u,v,d)
    return dist
