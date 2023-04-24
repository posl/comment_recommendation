Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    cnt = 0
    for a in range(N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                if b in graph[a] and c in graph[b] and a in graph[c]:
                    cnt += 1
    print(cnt)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    graph = [[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u][v] = 1
        graph[v][u] = 1
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if graph[i][j] == 1 and graph[j][k] == 1 and graph[k][i] == 1:
                    count += 1
    print(count)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    edge = [[0] * n for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        edge[u - 1][v - 1] = 1
        edge[v - 1][u - 1] = 1

    ans = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if edge[i][j] and edge[j][k] and edge[k][i]:
                    ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    graph = [[False for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u - 1][v - 1] = True
        graph[v - 1][u - 1] = True
    ans = 0
    for a in range(N):
        for b in range(a + 1, N):
            for c in range(b + 1, N):
                if graph[a][b] and graph[b][c] and graph[c][a]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(M)]
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            for k in range(j+1, M):
                if edges[i][0] == edges[j][0] and edges[j][0] == edges[k][0]:
                    continue
                if edges[i][0] == edges[j][0] and edges[j][0] == edges[k][1]:
                    continue
                if edges[i][0] == edges[j][1] and edges[j][1] == edges[k][0]:
                    continue
                if edges[i][0] == edges[j][1] and edges[j][1] == edges[k][1]:
                    continue
                if edges[i][1] == edges[j][0] and edges[j][0] == edges[k][0]:
                    continue
                if edges[i][1] == edges[j][0] and edges[j][0] == edges[k][1]:
                    continue
                if edges[i][1] == edges[j][1] and edges[j][1] == edges[k][0]:
                    continue
                if edges[i][1] == edges[j][1] and edges[j][1] == edges[k][1]:
                    continue
                if edges[i][0] == edges[j][0] or edges[i][0] == edges[j][1] or edges[i][0] == edges[k][0] or edges[i][0] == edges[k][1]:
                    continue
                if edges[i][1] == edges[j][0] or edges[i][1] == edges[j][1] or edges[i][1] == edges[k][0] or edges[i][1] == edges[k][1]:
                    continue
                if edges[j][0] == edges[k][0] or edges[j][0] == edges[k][1]:
                    continue
                if edges[j][1] == edges[k][0] or edges[j][1] == edges[k][1]:
                    continue
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(M)]
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            for k in range(j+1, M):
                if edge[i][0] in edge[j] and edge[j][0] in edge[k] and edge[k][0] in edge[i]:
                    ans += 1
                elif edge[i][0] in edge[j] and edge[j][1] in edge[k] and edge[k][0] in edge[i]:
                    ans += 1
                elif edge[i][1] in edge[j] and edge[j][0] in edge[k] and edge[k][0] in edge[i]:
                    ans += 1
                elif edge[i][1] in edge[j] and edge[j][1] in edge[k] and edge[k][0] in edge[i]:
                    ans += 1
                elif edge[i][0] in edge[j] and edge[j][0] in edge[k] and edge[k][1] in edge[i]:
                    ans += 1
                elif edge[i][0] in edge[j] and edge[j][1] in edge[k] and edge[k][1] in edge[i]:
                    ans += 1
                elif edge[i][1] in edge[j] and edge[j][0] in edge[k] and edge[k][1] in edge[i]:
                    ans += 1
                elif edge[i][1] in edge[j] and edge[j][1] in edge[k] and edge[k][1] in edge[i]:
                    ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    graph = [[False for j in range(N)] for i in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u - 1][v - 1] = True
        graph[v - 1][u - 1] = True

    count = 0
    for a in range(N - 2):
        for b in range(a + 1, N - 1):
            for c in range(b + 1, N):
                if graph[a][b] and graph[b][c] and graph[c][a]:
                    count += 1
    print(count)

=======
Suggestion 8

def makeGraph(N, M, edges):
    graph = [[] for i in range(N)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

=======
Suggestion 9

def get_input():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    return N, M, edges

=======
Suggestion 10

def main():
    N, M = map(int, input().split(' '))
    edges = [list(map(int, input().split(' '))) for _ in range(M)]
    graph = [[] for _ in range(N)]
    for u, v in edges:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    ans = 0
    for a in range(N):
        for b in graph[a]:
            if a >= b:
                continue
            for c in graph[b]:
                if a >= c:
                    continue
                if b in graph[c]:
                    ans += 1
    print(ans // 3)
