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
    queue = [0]
    while queue:
        v = queue.pop()
        for nv, w in G[v]:
            if color[nv] is None:
                color[nv] = color[v] ^ (w % 2)
                queue.append(nv)
    for c in color:
        print(c)

=======
Suggestion 2

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    ans = [0] * N
    def dfs(cur, par):
        for nxt, w in G[cur]:
            if nxt == par:
                continue
            if w % 2 == 0:
                ans[nxt] = ans[cur]
            else:
                ans[nxt] = 1 - ans[cur]
            dfs(nxt, cur)
    dfs(0, -1)
    print(*ans, sep = '

')

=======
Suggestion 3

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u-1].append((v-1,w))
        G[v-1].append((u-1,w))
    ans = [0]*N
    stack = [(0,0)]
    while stack:
        p,c = stack.pop()
        ans[p] = c
        for q,d in G[p]:
            if ans[q] == -1:
                stack.append((q,c^d%2))
    print('

'.join(map(str,ans)))

=======
Suggestion 4

def main():
    N = int(input())
    adj = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    color = [None] * (N + 1)
    color[1] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        for u, w in adj[v]:
            if color[u] is None:
                color[u] = color[v] ^ (w % 2)
                stack.append(u)

    print(*color[1:], sep='

')

=======
Suggestion 5

def main():
    N = int(input())
    graph = [[] for _ in range(N)]
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        graph[u - 1].append((v - 1, w))
        graph[v - 1].append((u - 1, w))
    color = [0] * N
    stack = [(0, 0)]
    while stack:
        u, c = stack.pop()
        color[u] = c
        for v, w in graph[u]:
            if color[v] == 0:
                stack.append((v, c ^ (w % 2)))
    print(*color, sep='

')

=======
Suggestion 6

def main():
    N = int(input())
    edge = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        edge[u].append((v, w))
        edge[v].append((u, w))
    color = [-1] * N
    color[0] = 0
    stack = [(0, 0)]
    while stack:
        now, c = stack.pop()
        for next, w in edge[now]:
            if color[next] == -1:
                color[next] = (c + w) % 2
                stack.append((next, color[next]))
    for c in color:
        print(c)

=======
Suggestion 7

def main():
    import sys
    sys.setrecursionlimit(10**6)
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u-1].append((v-1,w))
        G[v-1].append((u-1,w))
    ans = [0]*N
    def dfs(v,p):
        for nv,w in G[v]:
            if nv == p:
                continue
            ans[nv] = ans[v] + w%2
            dfs(nv,v)
    dfs(0,-1)
    ans = [str(a%2) for a in ans]
    print('

'.join(ans))
main()

=======
Suggestion 8

def main():
    N = int(input())
    edge = [tuple(map(int, input().split())) for _ in range(N - 1)]
    G = [[] for _ in range(N)]
    for u, v, w in edge:
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    ans = [-1] * N
    ans[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in G[v]:
            if ans[nv] == -1:
                ans[nv] = ans[v] ^ (w % 2)
                stack.append(nv)
    print(*ans, sep='

')

=======
Suggestion 9

def main():
    N = int(input())
    # 1-indexed
    G = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))
    # 1-indexed
    color = [None] * (N + 1)
    color[1] = 0
    stack = [1]
    while stack:
        x = stack.pop()
        for y, w in G[x]:
            if color[y] is not None:
                continue
            color[y] = color[x] ^ (w % 2)
            stack.append(y)
    for i in range(1, N + 1):
        print(color[i])

=======
Suggestion 10

def solve(n, uvw):
    # 深さ優先探索で、各ノードの深さを求める
    depth = [-1] * n
    depth[0] = 0
    stack = [0]
    while stack:
        i = stack.pop()
        for j, w in uvw[i]:
            if depth[j] != -1:
                continue
            depth[j] = depth[i] + w
            stack.append(j)
    
    # 各ノードの深さの奇偶を出力する
    for i in range(n):
        print(depth[i] % 2)
