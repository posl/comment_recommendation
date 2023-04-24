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
    color = [None] * N
    color[0] = 0
    stack = [(0, 0)]
    while stack:
        v, c = stack.pop()
        for w, d in G[v]:
            if color[w] is None:
                color[w] = (c + d) % 2
                stack.append((w, color[w]))
    print(*color, sep='

')

=======
Suggestion 2

def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    color = [None] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in graph[v]:
            if color[nv] is None:
                color[nv] = color[v] ^ (w % 2)
                stack.append(nv)
    for c in color:
        print(c)

=======
Suggestion 3

def main():
    N = int(input())
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        adj[u-1].append((v-1, w))
        adj[v-1].append((u-1, w))
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        now = stack.pop()
        for nxt, w in adj[now]:
            if color[nxt] == -1:
                color[nxt] = color[now] ^ (w%2)
                stack.append(nxt)
    for c in color:
        print(c)

=======
Suggestion 4

def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        u -= 1
        v -= 1
        graph[u].append((v,w))
        graph[v].append((u,w))
    ans = [None]*N
    ans[0] = 0
    q = [(0,0)]
    while q:
        v, c = q.pop()
        for nv, w in graph[v]:
            if ans[nv] is None:
                ans[nv] = c if w%2 == 0 else 1-c
                q.append((nv,ans[nv]))
    print(*ans,sep='

')

main()

=======
Suggestion 5

def main():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    # 隣接リストを作成
    adj = [[] for _ in range(N + 1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # BFSで各頂点の色を決める
    color = [None] * (N + 1)
    color[1] = 0
    q = [1]
    while q:
        u = q.pop()
        for v, w in adj[u]:
            if color[v] is None:
                color[v] = color[u] ^ (w % 2)
                q.append(v)

    # 答えを出力
    for i in range(1, N + 1):
        print(color[i])

=======
Suggestion 6

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    
    N = int(input())
    E = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        E[u-1].append((v-1,w))
        E[v-1].append((u-1,w))
    
    ans = [-1]*N
    ans[0] = 0
    que = deque([0])
    while que:
        v = que.popleft()
        for nv,nw in E[v]:
            if ans[nv] == -1:
                ans[nv] = ans[v] + nw
                que.append(nv)
    
    for a in ans:
        print(a%2)

main()

=======
Suggestion 7

def main():
    from sys import stdin
    from collections import deque
    N = int(stdin.readline().rstrip())
    E = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, stdin.readline().rstrip().split())
        E[u].append((v, w))
        E[v].append((u, w))
    D = [0] * (N + 1)
    Q = deque()
    Q.append(1)
    while Q:
        n = Q.popleft()
        for v, w in E[n]:
            if D[v] != 0:
                continue
            D[v] = D[n] + w
            Q.append(v)
    print('
'.join(map(lambda x: str(x % 2), D[1:])))

main()

=======
Suggestion 8

def main():
    N = int(input())
    # 木の隣接リスト
    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))
    # DFS
    # 0: 白
    # 1: 黒
    # -1: 未訪問
    colors = [-1] * N
    colors[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in tree[v]:
            if colors[nv] == -1:
                colors[nv] = (colors[v] + w) % 2
                stack.append(nv)
    for c in colors:
        print(c)

=======
Suggestion 9

def main():
    import sys
    from collections import deque

    sys.setrecursionlimit(10 ** 7)

    n = int(input())
    edges = [[] for _ in range(n)]

    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edges[u - 1].append((v - 1, w))
        edges[v - 1].append((u - 1, w))

    colors = [-1] * n
    colors[0] = 0

    q = deque()
    q.append(0)

    while q:
        v = q.popleft()

        for nv, w in edges[v]:
            if colors[nv] != -1:
                continue

            if w % 2 == 0:
                colors[nv] = colors[v]
            else:
                colors[nv] = 1 - colors[v]

            q.append(nv)

    for c in colors:
        print(c)

=======
Suggestion 10

def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    #print(edges)
    #print(n)
    #print(edges)
    tree = [[] for _ in range(n)]
    for u, v, w in edges:
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))

    #print(tree)
    ans = [0] * n
    ans[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u, w in tree[v]:
            if ans[u] != 0:
                continue
            if w % 2 == 0:
                ans[u] = ans[v]
            else:
                ans[u] = 1 - ans[v]
            stack.append(u)
    print(*ans, sep='

')
