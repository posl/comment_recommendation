Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
    #print(N, M)
    #print(A)
    #print(B)
    #print(C)
    INF = 1000000000000000000
    d = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        d[i][i] = 0
    for i in range(M):
        d[A[i]][B[i]] = C[i]
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    #print(d)
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if d[i][j] == d[i][k] + d[k][j]:
                    ans += d[i][j]
    print(ans)

=======
Suggestion 2

def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1

    INF = 10**18
    dp = [[INF] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0

    for i in range(M):
        dp[A[i]][B[i]] = min(dp[A[i]][B[i]], C[i])

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    ans = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if dp[i][j] == dp[i][k] + dp[k][j]:
                    ans += dp[i][j]
                    break

    print(ans)
    return

=======
Suggestion 3

def floyd_warshall(graph, n):
    dist = graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

=======
Suggestion 4

def floyd_warshall(n, edges):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for a, b, c in edges:
        dist[a][b] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    edges[i][0] -= 1
    edges[i][1] -= 1
dist = floyd_warshall(n, edges)
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist[i][k] + dist[k][j] == dist[i][j]:
                ans += dist[i][j]
print(ans)

=======
Suggestion 5

def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines

    N, M, *ABCL = map(int, read().split())
    INF = 10**15
    G = [[INF] * N for _ in range(N)]
    for a, b, c in zip(*[iter(ABCL)] * 3):
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
            if G[i][j] < INF:
                ans += G[i][j]

    print(ans)

=======
Suggestion 6

def floyd_warshall(n, edges):
    INF = 10**18
    d = [[INF]*n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for a, b, c in edges:
        d[a][b] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d

=======
Suggestion 7

def main():
    import sys
    from collections import deque
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dist = [float("inf")] * (N + 1)
            dist[i] = 0
            q = deque([i])
            while q:
                v = q.popleft()
                for nv, c in graph[v]:
                    if dist[nv] > dist[v] + c:
                        dist[nv] = dist[v] + c
                        q.append(nv)
            ans += dist[j]
    print(ans)

=======
Suggestion 8

def  main():
    n, m = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(m)]
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            d = [10**9] * n
            d[i] = 0
            d[j] = 0
            for _ in range(n):
                for a, b, c in c:
                    if d[a-1] + c < d[b-1]:
                        d[b-1] = d[a-1] + c
            ans += sum(d)
    print(ans)

=======
Suggestion 9

def  main():
    import  sys
    readline  =  sys.stdin.readline
    N, M  =   map ( int , readline().split())
    INF  =  10 **  6  *  400  +   1 
    G  =  [ [ INF  for  _  in   range (N)]  for  _  in   range (N)]
    for  _  in   range (M):
        A, B, C  =   map ( int , readline().split())
        G[A -  1 ][B -  1 ] = C
     for  k  in   range (N):
         for  i  in   range (N):
             for  j  in   range (N):
                G[i][j]  =   min (G[i][j], G[i][k] + G[k][j])
    ans  =   0 
     for  i  in   range (N):
         for  j  in   range (N):
             for  k  in   range (N):
                ans  +=   min (G[i][j], G[i][k] + G[k][j])
    print (ans)
