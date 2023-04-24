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
    color = [0] * N
    color[0] = 1
    stack = [(0, 0)]
    while stack:
        v, p = stack.pop()
        for nv, w in G[v]:
            if nv == p:
                continue
            color[nv] = color[v] + w % 2
            stack.append((nv, v))
    for c in color:
        print(c % 2)

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
    def dfs(u, p, c):
        ans[u] = c
        for v, w in G[u]:
            if v == p:
                continue
            dfs(v, u, c ^ (w % 2))

    dfs(0, -1, 0)
    print(*ans, sep='

')

=======
Suggestion 3

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))

    ans = [0] * N
    stack = [(0, 0)]
    while stack:
        u, p = stack.pop()
        for v, w in G[u]:
            if v == p:
                continue
            ans[v] = ans[u] ^ (w % 2)
            stack.append((v, u))

    for a in ans:
        print(a)

=======
Suggestion 4

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append((v - 1, w))
        G[v - 1].append((u - 1, w))
    # 奇数番目の頂点は黒、偶数番目の頂点は白で塗る
    # 0: 白, 1: 黒
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for to, w in G[v]:
            if color[to] != -1:
                continue
            if w % 2 == 0:
                color[to] = color[v]
            else:
                color[to] = 1 - color[v]
            stack.append(to)
    for c in color:
        print(c)

=======
Suggestion 5

def main():
    N = int(input())
    E = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        E[u].append((v, w))
        E[v].append((u, w))
    ans = [None] * (N + 1)
    stack = [(1, 0)]
    while stack:
        v, p = stack.pop()
        if ans[v] is None:
            ans[v] = p
            for nv, w in E[v]:
                stack.append((nv, p ^ (w % 2)))
    print(*ans[1:], sep='
')

=======
Suggestion 6

def main():
    N = int(input())
    E = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        E[u].append((v, w))
        E[v].append((u, w))
    C = [-1] * (N + 1)
    C[1] = 0
    Q = [1]
    while Q:
        x = Q.pop()
        for y, w in E[x]:
            if C[y] == -1:
                C[y] = C[x] ^ (w % 2)
                Q.append(y)
    for i in range(1, N + 1):
        print(C[i])

=======
Suggestion 7

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        G[u-1].append((v-1,w))
        G[v-1].append((u-1,w))
    ans = [-1]*N
    ans[0] = 0
    q = [0]
    while q:
        v = q.pop()
        for nv,nw in G[v]:
            if ans[nv] == -1:
                ans[nv] = (ans[v] + nw) % 2
                q.append(nv)
    for a in ans:
        print(a)

=======
Suggestion 8

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, w))
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for nv, w in G[v]:
            if color[nv] == -1:
                color[nv] = (color[v] + w) % 2
                stack.append(nv)
    print(*color, sep='

')

=======
Suggestion 9

def main():
    N = int(input())
    graph = [[] for i in range(N)]
    for i in range(N-1):
        u, v, w = map(int, input().split())
        graph[u-1].append([v-1, w])
        graph[v-1].append([u-1, w])
    color = [-1] * N
    color[0] = 0
    stack = [0]
    while stack:
        node = stack.pop()
        for i, w in graph[node]:
            if color[i] == -1:
                color[i] = (color[node] + w) % 2
                stack.append(i)
    for i in color:
        print(i)
main()

=======
Suggestion 10

def main():
    N = int(input())
    edge = [[] for _ in range(N+1)]
    for _ in range(N-1):
        u,v,w = map(int,input().split())
        edge[u].append([v,w])
        edge[v].append([u,w])
    dist = [-1]*(N+1)
    dist[1] = 0
    stack = [1]
    while stack:
        v = stack.pop()
        for u,w in edge[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + w
                stack.append(u)
    for i in range(1,N+1):
        print(dist[i]%2)
