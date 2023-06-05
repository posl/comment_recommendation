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

def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]

n, m = map(int, input().split())
d = [[float('inf')]*n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c

floyd_warshall()
ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != j and j != k and k != i:
                ans += d[i][j] + d[j][k] + d[k][i]

print(ans)

=======
Suggestion 3

def floyd_warshall(n, m, edges):
    d = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for a, b, c in edges:
        d[a - 1][b - 1] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

=======
Suggestion 4

def floyd_warshall():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

N, M = map(int, input().split())
INF = 10**9
d = [[INF]*N for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    d[A-1][B-1] = C

floyd_warshall()

ans = 0
for s in range(N):
    for t in range(N):
        for k in range(N):
            if d[s][t] == d[s][k] + d[k][t]:
                ans += d[s][t]
print(ans)

=======
Suggestion 5

def floyd_warshall(n, d):
    # n: the number of vertices
    # d: distance matrix
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

n, m = map(int, input().split())
d = [[10**9] * n for i in range(n)]
for i in range(n):
    d[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c

floyd_warshall(n, d)

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            if d[i][j] == d[i][k] + d[k][j]:
                ans += d[i][j]
print(ans)

=======
Suggestion 6

def main():
    pass

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    A = []
    B = []
    C = []
    for i in range(m):
        a,b,c = map(int,input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    for i in range(m):
        A[i] -= 1
        B[i] -= 1
    INF = 10**9
    d = [[INF for i in range(n)] for j in range(n)]
    for i in range(n):
        d[i][i] = 0
    for i in range(m):
        d[A[i]][B[i]] = C[i]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    ans = 0
    for s in range(n):
        for t in range(n):
            for k in range(n):
                if d[s][t] == d[s][k] + d[k][t]:
                    ans += d[s][t]
    print(ans)

=======
Suggestion 8

def floyd_warshall(n, m, road):
    '''floyd_warshall'''
    inf = float('inf')
    dist = [[inf for i in range(n)] for j in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for i in range(m):
        dist[road[i][0]-1][road[i][1]-1] = road[i][2]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist

=======
Suggestion 9

def main():
    print("Hello World!")
