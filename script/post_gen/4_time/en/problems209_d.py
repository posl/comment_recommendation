Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]

    # 隣接リストを作成
    # 1-indexedなので、N+1
    adj = [[] for _ in range(N+1)]
    for a, b in AB:
        adj[a].append(b)
        adj[b].append(a)

    # 根からの深さを記録する
    # 1-indexedなので、N+1
    depth = [0] * (N+1)
    depth[1] = 1

    # 根を1として、深さを記録する
    # 1-indexedなので、N+1
    def dfs(u, p):
        for v in adj[u]:
            if v == p:
                continue
            depth[v] = depth[u] + 1
            dfs(v, u)

    dfs(1, -1)

    # 各クエリに対して、深さを比較して、同じならTown、異なるならRoad
    for c, d in CD:
        if (depth[c] + depth[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(N-1)]
    cd = [list(map(int, input().split())) for _ in range(Q)]

    # 木構造にグラフを作成
    graph = [[] for _ in range(N)]
    for a, b in ab:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    # 根からの距離を求める
    dist = [-1] * N
    dist[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for i in graph[v]:
            if dist[i] == -1:
                dist[i] = dist[v] + 1
                stack.append(i)

    # 各クエリについて、距離の偶奇で判定
    for c, d in cd:
        if (dist[c-1] + dist[d-1]) % 2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    cd = [list(map(int, input().split())) for _ in range(q)]

    # graph[i] = [j, k, ...] means Town i is connected to Town j, k, ...
    graph = [[] for _ in range(n)]
    for a, b in ab:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    # dist[i] = j means Town i is j-th from Town 1
    dist = [-1] * n
    dist[0] = 0
    stack = [0]
    while stack:
        town = stack.pop()
        for next_town in graph[town]:
            if dist[next_town] == -1:
                dist[next_town] = dist[town] + 1
                stack.append(next_town)

    for c, d in cd:
        if (dist[c-1] + dist[d-1]) % 2 == 0:
            print('Town')
        else:
            print('Road')

=======
Suggestion 4

def main():
    n,q = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(n-1)]
    cd = [list(map(int, input().split())) for i in range(q)]
    g = [[] for i in range(n+1)]
    for a,b in ab:
        g[a].append(b)
        g[b].append(a)
    d = [-1]*(n+1)
    d[1] = 0
    q = [1]
    while q:
        qq = []
        for p in q:
            for np in g[p]:
                if d[np] == -1:
                    d[np] = d[p] + 1
                    qq.append(np)
        q = qq
    for c,d in cd:
        if (d - c) % 2 == 0:
            print('Town')
        else:
            print('Road')

=======
Suggestion 5

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
        
    return parent[x]

=======
Suggestion 6

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 7

def find_root(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_root(parent[x])
        return parent[x]

=======
Suggestion 8

def dfs(v,p,c):
    color[v]=c
    for i in g[v]:
        if i==p:continue
        if color[i]==c:return 1
        if color[i]==0 and dfs(i,v,-c):return 1
    return 0

n,q=map(int,input().split())
g=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
color=[0]*n
dfs(0,-1,1)
for _ in range(q):
    c,d=map(int,input().split())
    if color[c-1]==color[d-1]:print("Town")
    else:print("Road")

=======
Suggestion 9

def solve():
    # Implement solution here
    return 0
