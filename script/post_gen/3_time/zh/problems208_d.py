Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def floyd_warshall(n, d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        x,y,z = map(int,input().split())
        a[x-1][y-1] = z
    ans = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if a[i][k] and a[k][j]:
                    if a[i][j]:
                        a[i][j] = min(a[i][j],a[i][k]+a[k][j])
                    else:
                        a[i][j] = a[i][k]+a[k][j]
            ans += a[i][j]
    print(ans)

=======
Suggestion 4

def main():
    return

=======
Suggestion 5

def floyd_warshall(N, M, edges):
    # dist[i][j]: 从i到j的最短路径长度
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for (a, b, c) in edges:
        dist[a-1][b-1] = c
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
    A = [x - 1 for x in A]
    B = [x - 1 for x in B]

    # Floyd-Warshall algorithm
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for i in range(M):
        dist[A[i]][B[i]] = C[i]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Count the number of paths
    ans = 0
    for s in range(N):
        for t in range(N):
            for k in range(N):
                if dist[s][t] == dist[s][k] + dist[k][t]:
                    ans += dist[s][t]
                    break
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    s = []
    t = []
    k = []
    for i in range(m):
        a,b,c = map(int,input().split())
        s.append(a)
        t.append(b)
        k.append(c)
    print(n,m)
    print(s)
    print(t)
    print(k)

=======
Suggestion 8

def floyd_warshall(n, m, roads):
    inf = 10 ** 9
    dist = [[inf for i in range(n)] for j in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for road in roads:
        dist[road[0]][road[1]] = road[2]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist

n, m = map(int, input().split())
roads = [list(map(int, input().split())) for i in range(m)]
dist = floyd_warshall(n, m, roads)
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist[i][j] == dist[i][k] + dist[k][j]:
                ans += dist[i][j]
print(ans)
