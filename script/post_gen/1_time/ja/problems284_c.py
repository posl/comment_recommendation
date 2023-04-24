Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        stack = [i]
        while stack:
            j = stack.pop()
            if visited[j]:
                continue
            visited[j] = True
            for k in G[j]:
                if visited[k]:
                    continue
                stack.append(k)
    print(ans)

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    print(connected_components(G))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    def dfs(v):
        seen[v] = True
        for next_v in graph[v]:
            if seen[next_v]:
                continue
            dfs(next_v)

    seen = [False] * N
    count = 0
    for i in range(N):
        if seen[i]:
            continue
        dfs(i)
        count += 1
    print(count)

=======
Suggestion 4

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    #N, M = 5, 3
    #N, M = 5, 0
    #N, M = 4, 6

    if M == 0:
        print(N)
        return

    # 辺の情報を格納する
    edge = [[0 for i in range(2)] for j in range(M)]
    for i in range(M):
        edge[i] = list(map(int, input().split()))

    # 辺の情報を元に、頂点の情報を格納する
    vertex = [[0 for i in range(2)] for j in range(N)]
    for i in range(M):
        vertex[edge[i][0] - 1][0] += 1
        vertex[edge[i][0] - 1][1] = edge[i][0]
        vertex[edge[i][1] - 1][0] += 1
        vertex[edge[i][1] - 1][1] = edge[i][1]

    # 頂点の情報を元に、連結成分を求める
    connected_component = []
    for i in range(N):
        if vertex[i][0] == 0:
            connected_component.append([vertex[i][1]])
        else:
            for j in range(len(connected_component)):
                if vertex[i][1] in connected_component[j]:
                    connected_component[j].append(vertex[i][1])
                    break
            else:
                connected_component.append([vertex[i][1]])

    print(len(connected_component))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    edge = [list(map(int, input().split())) for _ in range(M)]
    edge.sort()
    print(edge)

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    edge = []
    for _ in range(M):
        u, v = map(int, input().split())
        edge.append((u, v))
    if M == 0:
        print(N)
        return
    edge.sort()

    def find(x):
        if x == parent[x]:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def unite(x, y):
        x, y = find(x), find(y)
        if x == y:
            return False
        if rank[x] < rank[y]:
            x, y = y, x
        if rank[x] == rank[y]:
            rank[x] += 1
        parent[y] = x
        return True

    def same(x, y):
        return find(x) == find(y)

    parent = [i for i in range(N+1)]
    rank = [0 for i in range(N+1)]
    for u, v in edge:
        unite(u, v)
    ans = 0
    for i in range(1, N+1):
        if parent[i] == i:
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    u = [0] * (M + 1)
    v = [0] * (M + 1)
    for i in range(M):
        u[i], v[i] = map(int, input().split())
    G = [[] for i in range(N + 1)]
    for i in range(M):
        G[u[i]].append(v[i])
        G[v[i]].append(u[i])
    seen = [False] * (N + 1)
    def dfs(v):
        seen[v] = True
        for nv in G[v]:
            if seen[nv]:
                continue
            dfs(nv)
    ans = 0
    for v in range(1, N + 1):
        if seen[v]:
            continue
        dfs(v)
        ans += 1
    print(ans)

=======
Suggestion 9

def main():
    #入力
    n, m = map(int, input().split())
    #辺の数が0の時
    if m == 0:
        print(n)
        exit()
    #グラフの作成
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    #深さ優先探索
    def dfs(graph, start):
        stack = [start]
        seen = [False] * n
        seen[start] = True
        while stack:
            v = stack.pop()
            for i in graph[v]:
                if seen[i] == False:
                    stack.append(i)
                    seen[i] = True
        return seen.count(True)
    #連結成分の個数
    ans = 0
    for i in range(n):
        if dfs(graph, i) != 0:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    #print(N, M)
    #print("---------------")
    if M == 0:
        print(N)
        return
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u-1].append(v-1)
        G[v-1].append(u-1)
    #print(G)
    #print("---------------")
    visited = [False] * N
    #print(visited)
    #print("---------------")
    ans = 0
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        q = [i]
        while q:
            now = q.pop()
            visited[now] = True
            for next in G[now]:
                if visited[next]:
                    continue
                q.append(next)
    print(ans)
