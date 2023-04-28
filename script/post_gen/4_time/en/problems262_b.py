Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    G = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        G[u-1][v-1] = 1
        G[v-1][u-1] = 1
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if G[i][j] == 0:
                continue
            for k in range(j+1, N):
                if G[i][k] == 0:
                    continue
                if G[j][k] == 0:
                    continue
                count += 1
    print(count)

=======
Suggestion 2

def check(a, b, c, edges):
    if (a, b) in edges and (b, c) in edges and (c, a) in edges:
        return True
    return False

N, M = map(int, input().split())
edges = []
for i in range(M):
    edges.append(tuple(map(int, input().split())))

count = 0
for a in range(1, N + 1):
    for b in range(a + 1, N + 1):
        for c in range(b + 1, N + 1):
            if check(a, b, c, edges):
                count += 1

print(count)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    ans = 0
    for i in range(M):
        for j in range(M):
            if i == j:
                continue
            if edges[i][1] in edges[j] and edges[i][0] in edges[j]:
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, m = [int(x) for x in input().split()]
    matrix = [[0 for x in range(n)] for y in range(n)]
    for i in range(m):
        a, b = [int(x) for x in input().split()]
        matrix[a-1][b-1] = 1
        matrix[b-1][a-1] = 1
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[k][i] == 1:
                    count += 1
    print(count)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    edges.sort()
    count = 0
    for i in range(M):
        for j in range(i+1, M):
            if edges[i][1] == edges[j][0]:
                for k in range(j+1, M):
                    if edges[j][1] == edges[k][0] and edges[k][1] == edges[i][0]:
                        count += 1
    print(count)

=======
Suggestion 6

def get_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    return n, m, edges

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())

    edges = []
    for i in range(M):
        u, v = map(int, input().split())
        edges.append([u, v])

    ans = 0
    for i in range(M):
        u, v = edges[i]
        for j in range(M):
            if i == j:
                continue
            if u in edges[j] and v in edges[j]:
                ans += 1
    print(ans//6)

=======
Suggestion 8

def is_triangle(a,b,c):
    if a + b > c and b + c > a and c + a > b:
        return True
    else:
        return False

=======
Suggestion 9

def countTriangles(graph, N):
    count = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if graph[i][j] == 1:
                for k in range(j+1, N+1):
                    if graph[j][k] == 1 and graph[k][i] == 1:
                        count += 1
    return count

N, M = map(int, input().split())

graph = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

print(countTriangles(graph, N))

=======
Suggestion 10

def count(a, b, c):
    return (a < b and b < c) or (a > b and b > c)

n, m = map(int, input().split())

graph = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1
    graph[b - 1][a - 1] = 1

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            ans += count(graph[i][j], graph[j][k], graph[k][i])

print(ans)
