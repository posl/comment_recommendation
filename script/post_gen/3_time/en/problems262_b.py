Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    ans = 0
    for a in range(N - 2):
        for b in range(a + 1, N - 1):
            for c in range(b + 1, N):
                if b in graph[a] and c in graph[b] and a in graph[c]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    ans = 0
    for i in range(m):
        for j in range(i + 1, m):
            for k in range(j + 1, m):
                if edges[i][0] == edges[j][0] or edges[i][0] == edges[j][1] or edges[i][1] == edges[j][0] or edges[i][1] == edges[j][1]:
                    continue
                if edges[j][0] == edges[k][0] or edges[j][0] == edges[k][1] or edges[j][1] == edges[k][0] or edges[j][1] == edges[k][1]:
                    continue
                if edges[i][0] == edges[k][0] or edges[i][0] == edges[k][1] or edges[i][1] == edges[k][0] or edges[i][1] == edges[k][1]:
                    continue
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            for k in range(j+1, M):
                if edges[i][0] in edges[j] and edges[j][0] in edges[k] and edges[k][0] in edges[i]:
                    ans += 1
                elif edges[i][1] in edges[j] and edges[j][1] in edges[k] and edges[k][1] in edges[i]:
                    ans += 1
                elif edges[i][0] in edges[j] and edges[j][1] in edges[k] and edges[k][0] in edges[i]:
                    ans += 1
                elif edges[i][1] in edges[j] and edges[j][0] in edges[k] and edges[k][1] in edges[i]:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    g = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].add(b-1)
        g[b-1].add(a-1)
    ans = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if j in g[i] and k in g[i] and k in g[j]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]
    count = 0
    for a in range(1, N-1):
        for b in range(a+1, N):
            for c in range(b+1, N+1):
                if [a, b] in edges and [b, c] in edges and [c, a] in edges:
                    count += 1
    print(count)

main()

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        U, V = map(int, input().split())
        edges.append((U, V))

    count = 0
    for a in range(1, N+1):
        for b in range(a+1, N+1):
            for c in range(b+1, N+1):
                if (a, b) in edges and (b, c) in edges and (c, a) in edges:
                    count += 1

    print(count)

=======
Suggestion 7

def solve():
    n, m = map(int, input().split())
    g = {i:[] for i in range(1, n + 1)}
    for i in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    ans = 0
    for a in range(1, n - 1):
        for b in g[a]:
            if a < b:
                for c in g[b]:
                    if b < c and a in g[c]:
                        ans += 1
    print(ans // 3)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    E = [tuple(map(int, input().split())) for _ in range(M)]
    E = set(E)
    ans = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            for k in range(j+1, N+1):
                if (i, j) in E and (j, k) in E and (k, i) in E:
                    ans += 1
    print(ans)

=======
Suggestion 9

def main():
    #Read the input
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    #Create a list of sets of connected vertices for each vertex
    neighbors = [set() for _ in range(N)]
    for u, v in edges:
        neighbors[u-1].add(v-1)
        neighbors[v-1].add(u-1)

    #Loop through each possible tuple of vertices
    count = 0
    for a in range(N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                #Check if the vertices are connected
                if b in neighbors[a] and c in neighbors[b] and a in neighbors[c]:
                    count += 1
    print(count)

=======
Suggestion 10

def count_triangles(edges):
    # count the number of triangles in a graph
    # edges is a list of tuples (a, b) representing edges
    count = 0
    for a, b in edges:
        for c, d in edges:
            if a == c and d != b:
                for e, f in edges:
                    if b == e and f == d:
                        count += 1

    return count
