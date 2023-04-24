Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    color = [-1] * N
    color[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for u, w in G[v]:
            if color[u] == -1:
                color[u] = color[v] + w
                q.append(u)
    for c in color:
        print(c % 2)

=======
Suggestion 2

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append([v - 1, w])
        G[v - 1].append([u - 1, w])
    ans = [-1] * N
    ans[0] = 0

    def dfs(v, c):
        for nv, w in G[v]:
            if ans[nv] == -1:
                ans[nv] = (c + w) % 2
                dfs(nv, ans[nv])

    dfs(0, 0)
    for a in ans:
        print(a)

=======
Suggestion 3

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    color = [None] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u, w in G[v]:
            if color[u] is None:
                color[u] = color[v] ^ (w % 2)
                stack.append(u)
    print(*color, sep='

')

=======
Suggestion 4

def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u, w in graph[v]:
            if color[u] == -1:
                color[u] = (color[v] + w) % 2
                stack.append(u)
    for c in color:
        print(c)

=======
Suggestion 5

def main():
    N = int(input())
    #N = 5
    #u = [2, 2, 1, 3]
    #v = [5, 3, 3, 4]
    #w = [2, 10, 8, 2]
    u = []
    v = []
    w = []
    for i in range(N - 1):
        u_i, v_i, w_i = map(int, input().split())
        #u_i, v_i, w_i = u[i], v[i], w[i]
        u.append(u_i)
        v.append(v_i)
        w.append(w_i)

    #print(u)
    #print(v)
    #print(w)
    #print(N)
    #print(u)
    #print(v)
    #print(w)
    #print(u[0])
    #print(v[0])
    #print(w[0])
    #print(u[1])
    #print(v[1])
    #print(w[1])
    #print(u[2])
    #print(v[2])
    #print(w[2])

    #print(u[3])
    #print(v[3])
    #print(w[3])

    #print(N)
    #print(u)
    #print(v)
    #print(w)
    #print(u[0])
    #print(v[0])
    #print(w[0])
    #print(u[1])
    #print(v[1])
    #print(w[1])
    #print(u[2])
    #print(v[2])
    #print(w[2])

    #print(u[3])
    #print(v[3])
    #print(w[3])

    #print(u[4])
    #print(v[4])
    #print(w[4])

    #print(u[5])
    #print(v[5])
    #print(w[5])

    #print(u[6])
    #print(v[6])
    #print(w[6])

    #print(u[7])
    #print(v[7])
    #print(w[7])

    #print(u[8])
    #print(v[8])
    #print(w[8])

    #print(u[9])
    #print(v[9])
    #print(w[9])

    #print(u[10])
    #print(v

=======
Suggestion 6

def dfs(u, p):
    for v, w in g[u]:
        if v == p:
            continue
        d[v] = d[u] + w
        dfs(v, u)

=======
Suggestion 7

def dfs(n, p, d, g):
    if n in g:
        for i in g[n]:
            if i[0] != p:
                d[i[0]] = d[n] + i[1]
                dfs(i[0], n, d, g)

=======
Suggestion 8

def main():
    N = int(input())
    # 木を表す隣接リスト
    tree = [[] for _ in range(N)]
    # 隣接リストを作成
    for _ in range(N-1):
        u,v,w = map(int, input().split())
        tree[u-1].append((v-1,w))
        tree[v-1].append((u-1,w))
    
    # 頂点0を根として探索
    # 頂点0からの距離を管理するリスト
    dist = [0]*N
    # 頂点0を訪問済みとする
    visited = [True] + [False]*(N-1)
    # 訪問済みの頂点のリスト
    que = [0]
    # 訪問済みの頂点のリストを順番に処理
    while que:
        # 訪問済みの頂点のリストから頂点を取り出す
        v = que.pop()
        # 頂点vに隣接する頂点を順番に処理
        for w,d in tree[v]:
            # 頂点wが訪問済みの場合は処理しない
            if visited[w]:
                continue
            # 頂点wを訪問済みとする
            visited[w] = True
            # 頂点wを訪問済みの頂点のリストに追加
            que.append(w)
            # 頂点wの距離を計算
            dist[w] = dist[v] + d
    
    # 距離が偶数なら0, 奇数なら1を出力
    for d in dist:
        print(d%2)

=======
Suggestion 9

def solve(N, edges):
    # 0: white, 1: black
    colors = [None] * N
    colors[0] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        for u, w in edges[v]:
            if colors[u] is None:
                colors[u] = (colors[v] + w % 2) % 2
                stack.append(u)
    return colors

=======
Suggestion 10

def read_int():
    return int(input())
