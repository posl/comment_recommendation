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
    stack = [0]
    while stack:
        c = stack.pop()
        for v, w in G[c]:
            if color[v] == -1:
                color[v] = (color[c] + w) % 2
                stack.append(v)

    for c in color:
        print(c)

=======
Suggestion 2

def main():
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))
    ans = [-1] * n
    ans[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv, w in g[v]:
            if ans[nv] == -1:
                if w % 2 == 0:
                    ans[nv] = ans[v]
                else:
                    ans[nv] = 1 - ans[v]
                q.append(nv)
    for a in ans:
        print(a)

main()

=======
Suggestion 3

def main():
    n = int(input())
    edge = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edge[u - 1].append((v - 1, w))
        edge[v - 1].append((u - 1, w))

    color = [-1] * n
    color[0] = 0
    que = [0]
    while que:
        q = que.pop()
        for v, w in edge[q]:
            if color[v] == -1:
                color[v] = color[q] ^ (w % 2)
                que.append(v)

    for c in color:
        print(c)

=======
Suggestion 4

def main():
    N = int(input())
    G = [[] for i in range(N)]
    for i in range(N-1):
        u, v, w = map(int, input().split())
        G[u-1].append((v-1, w))
        G[v-1].append((u-1, w))
    color = [-1] * N
    color[0] = 0
    stack = [(0, 0)]
    while stack:
        u, c = stack.pop()
        for v, w in G[u]:
            if color[v] == -1:
                color[v] = (c + w) % 2
                stack.append((v, color[v]))
    for c in color:
        print(c)

=======
Suggestion 5

def main():
    N = int(input())
    G = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u].append((v,w))
        G[v].append((u,w))
    ans = [0] * (N+1)
    def dfs(s,p):
        for t,w in G[s]:
            if t == p: continue
            ans[t] = ans[s] ^ (w%2)
            dfs(t,s)
    dfs(1,-1)
    for i in range(1,N+1):
        print(ans[i])

=======
Suggestion 6

def main():
    N = int(input())
    g = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        g[u-1].append((v-1, w))
        g[v-1].append((u-1, w))
    color = [-1]*N
    color[0] = 0
    stack = [0]
    while stack:
        p = stack.pop()
        for q, w in g[p]:
            if color[q] == -1:
                color[q] = color[p] ^ (w%2)
                stack.append(q)
    for i in range(N):
        print(color[i])

=======
Suggestion 7

def main():
    N = int(input())
    node = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        node[u-1].append([v-1,w])
        node[v-1].append([u-1,w])

    ans = [-1]*N
    ans[0] = 0
    stack = [0]
    while stack:
        now = stack.pop()
        for next in node[now]:
            if ans[next[0]] == -1:
                ans[next[0]] = (ans[now] + next[1])%2
                stack.append(next[0])
    print(*ans,sep='

')

=======
Suggestion 8

def main():
    N = int(input())
    uvw = [[int(i) for i in input().split()] for i in range(N - 1)]
    # 隣接リスト
    adj = [[] for i in range(N + 1)]
    for u, v, w in uvw:
        adj[u].append((v, w))
        adj[v].append((u, w))
    # 頂点1からの距離を記録する配列
    dist = [-1] * (N + 1)
    dist[1] = 0
    # 頂点1からの距離を計算
    stack = [1]
    while stack:
        v = stack.pop()
        for nv, w in adj[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + w
                stack.append(nv)
    # 頂点1からの距離が偶数なら0、奇数なら1
    for i in range(1, N + 1):
        print(dist[i] % 2)

=======
Suggestion 9

def main():
    N = int(input())
    uvw = [list(map(int, input().split())) for _ in range(N-1)]
    #print(N,uvw)
    # 隣接リストを作る
    g = [[] for _ in range(N)]
    for u, v, w in uvw:
        u -= 1
        v -= 1
        g[u].append((v, w))
        g[v].append((u, w))
    #print(g)
    # 0 からの距離を求める
    dist = [-1] * N
    dist[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in g[v]:
            if dist[nv] != -1:
                continue
            dist[nv] = dist[v] + w
            stack.append(nv)
    #print(dist)
    for i in range(N):
        if dist[i] % 2 == 0:
            print(0)
        else:
            print(1)

=======
Suggestion 10

def main():
    N = int(input())
    # 木の構造を保持する
    # 1-indexedで保持する
    tree = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        tree[u].append((v, w))
        tree[v].append((u, w))

    # 木をDFSで探索する
    # 1-indexedで保持する
    # 0: 白, 1: 黒
    color = [0] * (N+1)
    # 1-indexedで保持する
    # 0: 未探索, 1: 探索済み
    visited = [0] * (N+1)
    # 1-indexedで保持する
    # 0: 未探索, 1: 探索済み
    # 頂点1からの距離を保持する
    dist = [0] * (N+1)
    stack = [1]
    while stack:
        now = stack.pop()
        visited[now] = 1
        for next, w in tree[now]:
            if visited[next] == 1:
                continue
            stack.append(next)
            dist[next] = dist[now] + w
            color[next] = color[now] if w % 2 == 0 else 1 - color[now]

    for c in color[1:]:
        print(c)
