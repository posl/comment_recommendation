Synthesizing 10/10 solutions

=======
Suggestion 1

def dfs(v, p, c):
    color[c] += 1
    for nv in G[v]:
        if nv == p:
            continue
        dfs(nv, v, c)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

color = [0] * N
dfs(0, -1, 0)

print(max(color))
for i in range(N-1):
    print(color[i+1])

=======
Suggestion 2

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    d = {}
    for a, b in ab:
        d.setdefault(a, [])
        d[a].append(b)
        d.setdefault(b, [])
        d[b].append(a)
    c = [0] * n
    c[0] = 1
    c[1] = 2
    c[2] = 3
    c[3] = 4
    for i in range(4, n):
        c[i] = i+1
    for i in range(1, n+1):
        for j in d[i]:
            if c[i-1] == c[j-1]:
                c[j-1] += 1
    print(max(c))
    for i in c:
        print(i)

=======
Suggestion 3

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    ans = [0]*N
    ans[0] = 1
    stack = [0]
    while stack:
        v = stack.pop()
        c = 1
        for u in G[v]:
            if ans[u] != 0:
                continue
            if c == ans[v]:
                c += 1
            ans[u] = c
            c += 1
            stack.append(u)
    print(max(ans))
    for i in range(N-1):
        print(ans[i])

=======
Suggestion 4

def main():
    N = int(input())
    edges = []
    for _ in range(N-1):
        a, b = map(int, input().split())
        edges.append((a, b))
    # print(edges)

    # 頂点の色の個数を数える
    color_num = [0 for _ in range(N+1)]
    for a, b in edges:
        color_num[a] += 1
        color_num[b] += 1
    # print(color_num)

    # 頂点の色の個数の最大値を求める
    max_color_num = max(color_num)
    # print(max_color_num)

    # 頂点の色の個数の最大値になるような頂点のリストを求める
    max_color_vertexes = []
    for i in range(1, N+1):
        if color_num[i] == max_color_num:
            max_color_vertexes.append(i)
    # print(max_color_vertexes)

    # 辺の色を決める
    edge_color = {}
    color = 1
    for a, b in edges:
        if a in max_color_vertexes and b in max_color_vertexes:
            edge_color[(a, b)] = color
            edge_color[(b, a)] = color
            color += 1
    # print(edge_color)

    # 辺の色を出力する
    print(max_color_num)
    for a, b in edges:
        print(edge_color[(a, b)])

=======
Suggestion 5

def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        edges.append(list(map(int, input().split())))
    #print("edges:", edges)

    # 色の数を決める
    max_color = 0
    for edge in edges:
        if edge[0] > max_color:
            max_color = edge[0]
        if edge[1] > max_color:
            max_color = edge[1]
    #print("max_color:", max_color)

    # 色の数を出力
    print(max_color)

    # 辺の色を決める
    for edge in edges:
        print(edge[0])

=======
Suggestion 6

def dfs(v, p=-1, c=-1):
    global ans
    c += 1
    color = 0
    for u in G[v]:
        if u == p:
            continue
        color += 1
        if c == color:
            color += 1
        ans[u] = color
        dfs(u, v, color)

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)
ans = [0]*N
dfs(0)
print(max(ans))
for a in ans:
    print(a)

=======
Suggestion 7

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        G[a-1].append(b-1)
        G[b-1].append(a-1)
    ans = [0] * (N-1)
    c = 0
    for i in range(N):
        if len(G[i]) > c:
            c = len(G[i])
            s = i
    color = [0] * N
    color[s] = 1
    q = [s]
    while q:
        v = q.pop()
        c = 1
        for i in range(len(G[v])):
            u = G[v][i]
            if color[u] == 0:
                if c == color[v]:
                    c += 1
                color[u] = c
                ans[i] = c
                c += 1
                q.append(u)
    print(max(color))
    for i in range(N-1):
        print(ans[i])

=======
Suggestion 8

def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in range(n - 1)]

    # 隣接リスト作成
    g = [[] for _ in range(n)]
    for a, b in ab:
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    # 1 から BFS しつつ、色を決めていく
    ans = [0] * (n - 1)
    q = [0]
    used = set()
    while q:
        v = q.pop(0)
        c = 1
        used.add(c)
        for u in g[v]:
            if ans[u] != 0:
                used.add(ans[u])
            else:
                while c in used:
                    c += 1
                used.add(c)
                ans[u] = c
                q.append(u)
    print(len(used))
    for c in ans:
        print(c)

=======
Suggestion 9

def solve():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    graph = [[] for _ in range(n)]
    for a, b in edges:
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(v, p):
        c = 1
        for u in graph[v]:
            if u == p:
                continue
            if c == color[p]:
                c += 1
            color[u] = c
            c += 1
            dfs(u, v)
    
    color = [0] * n
    color[0] = 1
    dfs(0, -1)
    
    print(max(color))
    for a, b in edges:
        print(color[b-1])

=======
Suggestion 10

def main():
    n = int(input())
    ab = []
    for _ in range(n-1):
        ab.append(list(map(int, input().split())))
    
    edge = [[] for _ in range(n)]
    for a, b in ab:
        edge[a-1].append(b-1)
        edge[b-1].append(a-1)
    
    color = [-1] * n
    color[0] = 1
    stack = [0]
    while stack:
        now = stack.pop()
        now_color = color[now]
        for next in edge[now]:
            if color[next] != -1:
                continue
            now_color += 1
            if now_color == color[now]:
                now_color += 1
            color[next] = now_color
            stack.append(next)
    
    print(max(color))
    for i in range(n-1):
        print(color[ab[i][0]-1])
