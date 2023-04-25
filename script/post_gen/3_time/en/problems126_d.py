Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    tree = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))
    color = [-1] * N
    stack = [(0, 0)]
    color[0] = 0
    while stack:
        u, c = stack.pop()
        for v, w in tree[u]:
            if color[v] == -1:
                color[v] = (c + w) % 2
                stack.append((v, color[v]))
    for c in color:
        print(c)

=======
Suggestion 2

def main():
    n = int(input())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))
    ans = [None] * n
    ans[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in graph[v]:
            if ans[nv] is None:
                ans[nv] = ans[v] + w % 2
                stack.append(nv)
    print(*[a % 2 for a in ans], sep='

')

=======
Suggestion 3

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        G[u-1].append([v-1, w])
        G[v-1].append([u-1, w])
    color = [-1]*N
    color[0] = 0
    def dfs(v):
        for nv, w in G[v]:
            if color[nv] == -1:
                color[nv] = (color[v]+w)%2
                dfs(nv)
    dfs(0)
    for i in color:
        print(i)
main()

=======
Suggestion 4

def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    tree = [[] for _ in range(N)]
    for u, v, w in edges:
        tree[u - 1].append((v - 1, w))
        tree[v - 1].append((u - 1, w))
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        u = stack.pop()
        for v, w in tree[u]:
            if color[v] != -1:
                continue
            color[v] = color[u] ^ (w % 2)
            stack.append(v)
    print(*color, sep='

')

main()

=======
Suggestion 5

def main():
    import sys
    from collections import deque
    input = sys.stdin.readline
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, w))
    Q = deque([0])
    visited = [False] * N
    d = [0] * N
    while Q:
        v = Q.popleft()
        visited[v] = True
        for nv, w in G[v]:
            if visited[nv]:
                continue
            d[nv] = d[v] + w
            Q.append(nv)
    for i in range(N):
        if d[i] % 2 == 0:
            print(0)
        else:
            print(1)

=======
Suggestion 6

def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    graph = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    colors = [-1 for _ in range(N)]
    colors[0] = 0
    dfs(graph, colors, 0)
    for color in colors:
        print(color)

=======
Suggestion 7

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v, w = map(int, input().split())
        edges.append([u, v, w])
    #print(edges)

    # 隣接リスト
    adj = [[] for _ in range(n+1)]
    for edge in edges:
        adj[edge[0]].append([edge[1], edge[2]])
        adj[edge[1]].append([edge[0], edge[2]])
    #print(adj)

    # DFS
    color = [None] * (n+1)
    stack = [1]
    color[1] = 0
    while len(stack) > 0:
        u = stack.pop()
        for v, w in adj[u]:
            if color[v] is None:
                color[v] = (color[u] + w) % 2
                stack.append(v)
    #print(color)

    for i in range(1, n+1):
        print(color[i])

=======
Suggestion 8

def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        edges.append(tuple(map(int, input().split())))
    adj = [[] for _ in range(n+1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    colors = [None] * (n+1)
    colors[1] = 0
    stack = [1]
    while stack:
        u = stack.pop()
        for v, w in adj[u]:
            if colors[v] is None:
                colors[v] = (colors[u] + w) % 2
                stack.append(v)
    print('

'.join(map(str, colors[1:])))

=======
Suggestion 9

def main():
    N = int(input())
    # 1-indexed
    edge = [[] for i in range(N + 1)]
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        edge[u].append([v, w])
        edge[v].append([u, w])
    # 1-indexed
    color = [None for i in range(N + 1)]
    color[1] = 0
    stack = [1]
    while len(stack) > 0:
        u = stack.pop()
        for v, w in edge[u]:
            if color[v] is None:
                color[v] = (color[u] + w) % 2
                stack.append(v)
    for i in range(1, N + 1):
        print(color[i])

=======
Suggestion 10

def path(x):
    if x == 0:
        return 0
    else:
        return path(parent[x]) ^ color[x]

n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a-1].append([b-1,c])
    graph[b-1].append([a-1,c])
parent = [-1]*n
color = [0]*n
stack = [[0,-1,0]]
while stack:
    v,p,c = stack.pop()
    parent[v] = p
    color[v] = c
    for v2,c2 in graph[v]:
        if v2 == p:
            continue
        stack.append([v2,v,c2%2])
for i in range(n):
    print(path(i))
