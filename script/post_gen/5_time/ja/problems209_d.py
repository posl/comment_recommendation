Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(now, par):
    for nex in G[now]:
        if nex == par: continue
        dist[nex] = dist[now] + 1
        dfs(nex, now)

N, Q = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = [0] * N
dfs(0, -1)

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (dist[c] + dist[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]

    # 隣接リストを作る
    graph = [[] for _ in range(N)]
    for a, b in AB:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    # 各頂点の深さを記録する配列
    depth = [-1] * N
    # 根の頂点の深さを 0 にする
    depth[0] = 0
    # 根の頂点を記録する変数
    root = 0
    # 根の頂点から DFS を行う
    stack = [root]
    while stack:
        i = stack.pop()
        for j in graph[i]:
            if depth[j] == -1:
                depth[j] = depth[i] + 1
                stack.append(j)

    # 各頂点の親を記録する配列
    parent = [-1] * N
    # 根の頂点の親を -1 にする
    parent[root] = -1
    # 根の頂点から DFS を行う
    stack = [root]
    while stack:
        i = stack.pop()
        for j in graph[i]:
            if parent[j] == -1:
                parent[j] = i
                stack.append(j)

    # 高橋君と青木君の街の頂点番号をそれぞれ c, d とする
    for c, d in CD:
        c -= 1
        d -= 1
        # 高橋君の街から根の頂点までの経路を記録する配列
        path_c = []
        i = c
        while i != -1:
            path_c.append(i)
            i = parent[i]
        # 青木君の街から根の頂点まで

=======
Suggestion 3

def get_input():
    N, Q = map(int, input().split())
    road = []
    for i in range(N-1):
        a, b = map(int, input().split())
        road.append([a, b])
    query = []
    for i in range(Q):
        c, d = map(int, input().split())
        query.append([c, d])
    return N, Q, road, query

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N-1)]
    cd = [list(map(int, input().split())) for _ in range(Q)]

    # グラフの隣接リスト表現
    edge = [[] for _ in range(N)]
    for a, b in ab:
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)

    # 各頂点の深さ
    depth = [-1] * N
    depth[0] = 0

    # 各頂点の親
    parent = [-1] * N

    # DFS
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in edge[v]:
            if depth[nv] == -1:
                depth[nv] = depth[v] + 1
                parent[nv] = v
                stack.append(nv)

    # 1. 高橋君が青木君より先に目的地に到着する場合
    # 2. 青木君が高橋君より先に目的地に到着する場合
    # 3. 高橋君と青木君が同時に目的地に到着する場合
    # 4. 高橋君と青木君が街中で出会う場合
    # 5. 高橋君と青木君が道路上で出会う場合

    # 各頂点の深さを求める
    depth = [-1] * N
    depth[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv in edge[v]:
            if depth[nv] == -1:
                depth[nv] = depth[v] + 1
                stack.append(nv)

    # 各頂点の親を求める
    parent = [-1] * N
    stack = [0]
    while stack:

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, Q, AB, CD)
    #print(N, Q)
    #print(AB)
    #print(CD)
    #print("AB[0][0]:", AB[0][0])
    #print("AB[0][1]:", AB[0][1])
    #print("AB[1][0]:", AB[1][0])
    #print("AB[1][1]:", AB[1][1])
    #print("AB[2][0]:", AB[2][0])
    #print("AB[2][1]:", AB[2][1])
    #print("CD[0][0]:", CD[0][0])
    #print("CD[0][1]:", CD[0][1])
    #print("CD[1][0]:", CD[1][0])
    #print("CD[1][1]:", CD[1][1])
    #print("CD[2][0]:", CD[2][0])
    #print("CD[2][1]:", CD[2][1])

    #print("AB[0][0] - 1:", AB[0][0] - 1)
    #print("AB[0][1] - 1:", AB[0][1] - 1)
    #print("AB[1][0] - 1:", AB[1][0] - 1)
    #print("AB[1][1] - 1:", AB[1][1] - 1)
    #print("AB[2][0] - 1:", AB[2][0] - 1)
    #print("AB[2][1] - 1:", AB[2][1] - 1)
    #print("CD[0][0] - 1:", CD[0][0] - 1)
    #print("CD[0][1] - 1:", CD[0][1] - 1)
    #print("CD[1][0] - 1:", CD[1][0] -

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    edge = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    from collections import deque
    dist = [-1]*N
    dist[0] = 0
    que = deque([0])
    while que:
        v = que.popleft()
        for nv in edge[v]:
            if dist[nv] != -1: continue
            dist[nv] = dist[v] + 1
            que.append(nv)

    for _ in range(Q):
        c, d = map(int, input().split())
        c, d = c-1, d-1
        if dist[c]%2 == dist[d]%2:
            print("Town")
        else:
            print("Road")

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N - 1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    dist = [-1] * N
    dist[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv in G[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + 1
            q.append(nv)
    for c, d in CD:
        if (dist[c - 1] + dist[d - 1]) % 2 == 0:
            print('Town')
        else:
            print('Road')

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a-1].append(b-1)
        tree[b-1].append(a-1)
    for _ in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        dist = [-1] * n
        dist[c] = 0
        stack = [c]
        while stack:
            v = stack.pop()
            for u in tree[v]:
                if dist[u] != -1:
                    continue
                dist[u] = dist[v] + 1
                stack.append(u)
        if dist[d] % 2 == 0:
            print('Town')
        else:
            print('Road')

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N - 1)]
    cd = [list(map(int, input().split())) for _ in range(Q)]
    #print(N, Q)
    #print(ab)
    #print(cd)
    #print()

    # 隣接リスト
    edges = [[] for _ in range(N + 1)]
    for a, b in ab:
        edges[a].append(b)
        edges[b].append(a)
    #print(edges)
    #print()

    # 頂点1から各頂点への距離
    dist = [-1] * (N + 1)
    dist[1] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        for v2 in edges[v]:
            if dist[v2] != -1:
                continue
            dist[v2] = dist[v] + 1
            stack.append(v2)
    #print(dist)
    #print()

    for c, d in cd:
        # 高橋君と青木君の距離
        dist_cd = abs(dist[c] - dist[d])
        # 高橋君と青木君の距離が偶数なら街で出会う
        if dist_cd % 2 == 0:
            print('Town')
        # 高橋君と青木君の距離が奇数なら道路上で出会う
        else:
            print('Road')

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    routes = []
    for _ in range(N-1):
        a, b = map(int, input().split())
        routes.append((a, b))
    for _ in range(Q):
        c, d = map(int, input().split())
        if (c, d) in routes or (d, c) in routes:
            print('Road')
        else:
            print('Town')
