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
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if j in graph[i] and k in graph[i] and k in graph[j]:
                    ans += 1

    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    edges = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        edges[u-1][v-1] = 1
        edges[v-1][u-1] = 1
    ans = 0
    for a in range(N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                if edges[a][b] == 1 and edges[b][c] == 1 and edges[c][a] == 1:
                    ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    x = [0] * M
    y = [0] * M
    for i in range(M):
        x[i], y[i] = map(int, input().split())
    
    count = 0
    for a in range(1, N - 1):
        for b in range(a + 1, N):
            for c in range(b + 1, N + 1):
                if (a in x and b in y) or (a in y and b in x):
                    if (b in x and c in y) or (b in y and c in x):
                        if (c in x and a in y) or (c in y and a in x):
                            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(M)]
    ans = 0
    for a in range(1, N-1):
        for b in range(a+1, N):
            for c in range(b+1, N+1):
                if [a, b] in edges and [b, c] in edges and [c, a] in edges:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    import sys
    input = sys.stdin.readline
    N, M = map(int, input().split())
    E = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        E[u-1].append(v-1)
        E[v-1].append(u-1)
    ans = 0
    for a in range(N):
        for b in E[a]:
            if a >= b:
                continue
            for c in E[b]:
                if a >= c or b >= c:
                    continue
                if c in E[a]:
                    ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(M)]

    ans = 0
    for a in range(1, N):
        for b in range(a+1, N):
            for c in range(b+1, N+1):
                if [a, b] in ab and [b, c] in ab and [c, a] in ab:
                    ans += 1
    print(ans)

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    e = [list(map(int,input().split())) for _ in range(m)]
    e.sort()
    ans = 0
    for i in range(m):
        for j in range(i+1,m):
            if e[i][0] == e[j][0]:
                continue
            if e[i][1] == e[j][1]:
                continue
            if e[i][1] > e[j][0]:
                continue
            if e[i][1] < e[j][0] and e[j][1] > e[i][1]:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    # 0-indexed
    adj = [[0] * N for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u][v] = 1
        adj[v][u] = 1

    ans = 0
    for a in range(N):
        for b in range(a+1, N):
            if adj[a][b] == 0:
                continue
            for c in range(b+1, N):
                if adj[b][c] == 0 or adj[c][a] == 0:
                    continue
                ans += 1

    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print()

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    # 二次元配列を初期化
    # 0で初期化される
    # 0: 辺が存在しない
    # 1: 辺が存在する
    edge = [[0 for i in range(N)] for j in range(N)]
    for _ in range(M):
        U, V = map(int, input().split())
        edge[U-1][V-1] = 1
        edge[V-1][U-1] = 1
    #print(edge)
    ans = 0
    for a in range(N-2):
        for b in range(a+1, N-1):
            for c in range(b+1, N):
                if edge[a][b] == 1 and edge[b][c] == 1 and edge[c][a] == 1:
                    ans += 1
    print(ans)
