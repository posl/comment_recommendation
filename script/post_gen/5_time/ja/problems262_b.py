Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b = map(int, input().split())
        edges.append((a, b))

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                a = i + 1
                b = j + 1
                c = k + 1
                if (a, b) in edges and (b, c) in edges and (c, a) in edges:
                    ans += 1

    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    edges.sort()
    ans = 0
    for i in range(m):
        for j in range(i+1, m):
            if edges[i][1] == edges[j][0]:
                for k in range(j+1, m):
                    if edges[i][0] == edges[k][0] and edges[j][1] == edges[k][1]:
                        ans += 1
    print(ans)

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    ans = 0
    for i in range(N):
        for j in G[i]:
            for k in G[j]:
                if k in G[i]:
                    ans += 1
    print(ans//6)

=======
Suggestion 4

def main():
    N,M = map(int,input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if j in G[i]:
                for k in range(j+1,N):
                    if k in G[j] and i in G[k]:
                        ans += 1
    print(ans)

=======
Suggestion 5

def solve():
    n,m = map(int,input().split())
    edge = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    ans = 0
    for i in range(n):
        for j in edge[i]:
            for k in edge[j]:
                if k in edge[i]:
                    ans += 1
    print(ans//6)

=======
Suggestion 6

def main():
    n,m = map(int,input().split())
    edge = []
    for i in range(m):
        edge.append(list(map(int,input().split())))
    ans = 0
    for i in range(m):
        for j in range(i+1,m):
            if edge[i][0] in edge[j] and edge[i][1] in edge[j]:
                ans += 1
    print(ans)
main()

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    data = []
    for i in range(M):
        data.append(list(map(int, input().split())))
    #print(N, M, data)

    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            #print(i, j, data[i], data[j])
            if data[i][0] in data[j] and data[i][1] in data[j]:
                ans += 1
            if data[i][0] in data[j] and data[i][1] in data[j]:
                ans += 1
            if data[i][0] in data[j] and data[i][1] in data[j]:
                ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N = 0
    M = 0
    U = []
    V = []
    ans = 0

    # 標準入力から N, M, U, V を取得する
    N, M = map(int, input().split())
    for i in range(M):
        u, v = map(int, input().split())
        U.append(u)
        V.append(v)

    # 頂点 a, b, c を全探索する
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            for c in range(1, N + 1):
                # a < b < c かつ、頂点 a と頂点 b を結ぶ辺が存在する。
                # 頂点 b と頂点 c を結ぶ辺が存在する。
                # 頂点 c と頂点 a を結ぶ辺が存在する。
                if a < b < c and (a in U and b in U) and (b in V and c in V) and (c in U and a in V):
                    ans += 1

    # 答えを出力する
    print(ans)

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    uv = [list(map(int, input().split())) for _ in range(M)]
    
    #print(N,M)
    #print(uv)

    # まずは隣接リストを作る
    adj = [[False for _ in range(N)] for _ in range(N)]
    for u, v in uv:
        adj[u - 1][v - 1] = True
        adj[v - 1][u - 1] = True
    #print(adj)

    # 頂点を選ぶ
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if not adj[i][j]:
                continue
            for k in range(j + 1, N):
                if adj[i][k] and adj[j][k]:
                    ans += 1
    print(ans)

=======
Suggestion 10

def solve():
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    N, M = 5, 6
    A = [1, 5, 4, 5, 2, 3, 1, 4, 3, 5, 2, 5]
    # N, M = 3, 1
    # A = [1, 2]
    # N, M = 7, 10
    # A = [1, 7, 5, 7, 2, 5, 3, 6, 4, 7, 1, 5, 2, 4, 1, 3, 1, 6, 2, 7]
    # N, M = 10, 20
    # A = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 2, 3, 2, 4, 2, 5, 2, 6, 3, 4, 3, 5, 3, 6, 4, 5, 4, 6, 5, 6]

    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # N, M = 3, 1
    # A = [1, 2]
    # N, M = 7, 10
    # A = [1, 7, 5, 7, 2, 5, 3, 6, 4, 7, 1, 5, 2, 4, 1, 3, 1, 6, 2, 7]
    # N, M = 10, 20
    # A = [1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 2, 3, 2, 4, 2, 5, 2, 6, 3, 4, 3, 5, 3, 6, 4
