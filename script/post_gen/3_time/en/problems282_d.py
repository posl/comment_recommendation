Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    u = [0] * M
    v = [0] * M
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    #print(N, M, u, v)
    edge = [[] for _ in range(N)]
    for i in range(M):
        edge[u[i]-1].append(v[i]-1)
        edge[v[i]-1].append(u[i]-1)
    #print(edge)
    ans = 0
    for i in range(N):
        for j in range(len(edge[i])):
            for k in range(j+1, len(edge[i])):
                if edge[i][j] in edge[edge[i][k]]:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    color = [-1] * n
    color[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for i in g[v]:
            if color[i] == -1:
                color[i] = 1 - color[v]
                stack.append(i)

    c1 = sum(color)
    c2 = n - c1

    print(c1 * c2 - m)

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)
    colors = [0] * n
    colors[0] = 1
    q = [0]
    while q:
        cur = q.pop()
        for nxt in g[cur]:
            if colors[nxt] == 0:
                colors[nxt] = -colors[cur]
                q.append(nxt)
            elif colors[nxt] == colors[cur]:
                print(0)
                exit()
    cnt = sum(c == 1 for c in colors)
    print(cnt * (n - cnt) - m)

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    
    color = [-1 for _ in range(N)]
    def dfs(x, c):
        color[x] = c
        for y in graph[x]:
            if color[y] == c:
                return False
            if color[y] == -1 and not dfs(y, 1 - c):
                return False
        return True
    
    ans = 0
    for i in range(N):
        if color[i] == -1:
            if dfs(i, 0):
                ans += color.count(0) * color.count(1)
            else:
                ans += N * (N - 1) // 2
                break
    print(ans - M)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        G[u].append(v)
        G[v].append(u)

    from collections import deque
    def bfs(s):
        q = deque([s])
        color = [-1]*N
        color[s] = 0
        while q:
            u = q.popleft()
            for v in G[u]:
                if color[v] == -1:
                    color[v] = color[u]^1
                    q.append(v)
        return color

    color = bfs(0)
    cnt = [0]*2
    for c in color:
        cnt[c] += 1

    ans = cnt[0]*cnt[1] - M
    print(ans)

=======
Suggestion 6

def solve():
    N,M = map(int,input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u,v = map(int,input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    color = [None] * N
    def dfs(v,c):
        if color[v] is not None:
            return color[v] == c
        color[v] = c
        for v2 in graph[v]:
            if not dfs(v2,1-c):
                return False
        return True
    ans = 0
    for v in range(N):
        if color[v] is None:
            if dfs(v,0):
                b = color.count(0)
                ans += b * (b-1) // 2
                b = color.count(1)
                ans += b * (b-1) // 2
            else:
                ans += N * (N-1) // 2
                break
    print(ans)
solve()

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    nodes = [[] for i in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        nodes[u].append(v)
        nodes[v].append(u)

    colors = [0] * (n + 1)
    ans = 0
    for i in range(1, n + 1):
        if colors[i] != 0:
            continue
        colors[i] = 1
        stack = [i]
        while stack:
            node = stack.pop()
            for next_node in nodes[node]:
                if colors[next_node] == 0:
                    colors[next_node] = -colors[node]
                    stack.append(next_node)
                elif colors[next_node] == colors[node]:
                    ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append([u, v])
    print(N, M, edges)

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    edges.sort(key=lambda x: x[1])
    edges.sort(key=lambda x: x[0])
    #print(edges)
    #print(n, m)
    #print(edges)
    #print(edges[0])
    #print(edges[1])
    #print(edges[2])
    #print(edges[3])
    #print(edges[4])
    #print(edges[5])
    #print(edges[6])
    #print(edges[7])
    #print(edges[8])
    #print(edges[9])
    #print(edges[10])
    #print(edges[11])
    #print(edges[12])
    #print(edges[13])
    #print(edges[14])
    #print(edges[15])
    #print(edges[16])
    #print(edges[17])
    #print(edges[18])
    #print(edges[19])
    #print(edges[20])
    #print(edges[21])
    #print(edges[22])
    #print(edges[23])
    #print(edges[24])
    #print(edges[25])
    #print(edges[26])
    #print(edges[27])
    #print(edges[28])
    #print(edges[29])
    #print(edges[30])
    #print(edges[31])
    #print(edges[32])
    #print(edges[33])
    #print(edges[34])
    #print(edges[35])
    #print(edges[36])
    #print(edges[37])
    #print(edges[38])
    #print(edges[39])
    #print(edges[40])
    #print(edges[41])
    #print(edges[42])
    #print(edges[43])
    #print(edges[44])
    #print(edges[45])
    #print(edges[46])
    #print(edges[47])
    #print(edges[48])
    #print(edges[49])
    #print(edges[50])
    #print(edges[51])
    #print(edges[52])
    #print(edges[53])
    #print(edges[54])
    #print(edges[55])
    #print(edges[56])
    #print(edges[57])
    #print(edges[58])
    #print(edges[59])
    #print(edges[

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    # 0-indexed
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    # 0: not visited, 1: white, 2: black
    color = [0] * N

    def dfs(v, c):
        color[v] = c
        for nv in graph[v]:
            if color[nv] == 0:
                if not dfs(nv, 3-c):
                    return False
            elif color[nv] == c:
                return False
        return True

    ans = 0
    for i in range(N):
        if color[i] == 0:
            if dfs(i, 1):
                ans += color.count(1) * color.count(2)
            else:
                ans = -1
                break

    print(ans)
