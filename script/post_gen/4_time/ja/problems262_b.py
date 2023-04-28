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
    ans = 0
    for i in range(N):
        for j in graph[i]:
            if i < j:
                for k in graph[j]:
                    if k in graph[i]:
                        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)
    ans = 0
    for u in range(N):
        for v in G[u]:
            for w in G[v]:
                if w == u:
                    ans += 1
    print(ans // 6)

=======
Suggestion 3

def solve():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        graph[u].append(v)
        graph[v].append(u)
    ans = 0
    for v in range(n):
        for u in graph[v]:
            for w in graph[u]:
                if w == v: continue
                if v in graph[w]:
                    ans += 1
    print(ans//6)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if [i+1, j+1] in edges and [j+1, k+1] in edges and [k+1, i+1] in edges:
                    ans += 1
    print(ans)

=======
Suggestion 5

def combination(n, r):
    if n < r:
        return 0
    elif n == r:
        return 1
    elif r == 1:
        return n
    else:
        return combination(n - 1, r - 1) + combination(n - 1, r)

=======
Suggestion 6

def solve():
    # N = 3
    # M = 1
    # U = [1]
    # V = [2]
    # N = 5
    # M = 6
    # U = [1, 4, 2, 1, 3, 2]
    # V = [5, 5, 3, 4, 5, 5]
    N = 7
    M = 10
    U = [1, 5, 2, 3, 4, 1, 2, 1, 1, 2]
    V = [7, 7, 5, 6, 7, 5, 4, 3, 6, 7]

    G = [[] for _ in range(N+1)]
    for i in range(M):
        G[U[i]].append(V[i])
        G[V[i]].append(U[i])

    ans = 0
    for i in range(1, N+1):
        for j in G[i]:
            for k in G[j]:
                if k != i and k not in G[i]:
                    ans += 1
    print(ans//6)

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        U, V = map(int, input().split())
        edges.append((U, V))

    # 頂点aから見たときに頂点b,cが存在するかどうかを判定
    # 頂点bから見たときに頂点a,cが存在するかどうかを判定
    # 頂点cから見たときに頂点a,bが存在するかどうかを判定
    # という風に、頂点a,b,cの順番を入れ替えて、全ての頂点について判定する
    # これで全ての頂点について判定できる
    ans = 0
    for a in range(1, N+1):
        for b in range(a+1, N+1):
            for c in range(b+1, N+1):
                if (a, b) in edges and (b, c) in edges and (c, a) in edges:
                    ans += 1

    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(M)]

    from itertools import combinations
    ans = 0
    for a, b, c in combinations(range(1, N + 1), 3):
        for u, v in edges:
            if {a, b} == {u, v} or {b, c} == {u, v} or {c, a} == {u, v}:
                break
        else:
            ans += 1

    print(ans)

=======
Suggestion 9

def main():
    # 標準入力の受け取り
    N, M = map(int, input().split())

    # グラフの初期化
    G = [[] for i in range(N)]

    # グラフの辺の受け取り
    for i in range(M):
        u, v = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)

    # 頂点0から各頂点への最短距離を求める
    dist = [-1] * N
    dist[0] = 0
    q = [0]
    while q:
        x = q.pop(0)
        for y in G[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                q.append(y)

    # 頂点0から各頂点への最短距離が3の倍数の頂点の個数を求める
    cnt = 0
    for i in range(N):
        if dist[i] % 3 == 0:
            cnt += 1

    # 頂点0から各頂点への最短距離が3の倍数の頂点の個数から、
    # 頂点0から最短距離が3の倍数の頂点への辺の本数を引いたものが、
    # 求める答え
    ans = cnt * (cnt - 1) // 2 - M

    # 答えの出力
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    if N < 3 or N > 100 or M < 1 or M > ((N*(N - 1))//2):
        print("N or M is out of range")
        return
    if M < 3:
        print(0)
        return

    graph = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        U_i, V_i = map(int, input().split())
        graph[U_i-1][V_i-1] = 1
        graph[V_i-1][U_i-1] = 1

    cnt = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            if graph[i][j] == 0:
                continue
            for k in range(j+1, N):
                if graph[i][k] == 1 and graph[j][k] == 1:
                    cnt += 1
    print(cnt)
