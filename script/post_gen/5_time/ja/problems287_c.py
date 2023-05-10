Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m = map(int,input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    for i in range(n):
        if len(g[i]) > 2:
            print("No")
            return
    print("Yes")

=======
Suggestion 2

def dfs(v, p=-1):
    global is_tree
    seen[v] = True
    for nv in G[v]:
        if nv == p:
            continue
        if seen[nv]:
            is_tree = False
        else:
            dfs(nv, v)

N, M = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

seen = [False] * N
is_tree = True
dfs(0)
for v in range(N):
    if not seen[v]:
        is_tree = False

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]
    edge = [0] * (N + 1)
    for i in range(M):
        u, v = A[i]
        edge[u] += 1
        edge[v] += 1
    print("Yes" if all([edge[i] % 2 == 0 for i in range(1, N + 1)]) else "No")

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)
        g[v - 1].append(u - 1)

    for i in range(n):
        if len(g[i]) == 2:
            continue
        else:
            print('No')
            exit()
    print('Yes')

=======
Suggestion 5

def path():
    n,m = map(int, input().split())
    if m == 0:
        print("No")
        return
    #グラフ作成
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u,v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    #パス判定
    for i in range(n):
        if len(graph[i]) > 2:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    for i in range(n):
        if len(graph[i]) != 2:
            print("No")
            return

    print("Yes")

=======
Suggestion 7

def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if visited[next_v]:
            continue
        dfs(next_v)
    return

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (N+1)
dfs(1)
print("Yes" if all(visited) else "No")

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    path = [0] * n
    for i in range(m):
        u, v = map(int, input().split())
        path[u-1] += 1
        path[v-1] += 1
    print("Yes" if max(path) <= 2 else "No")

=======
Suggestion 9

def main():
    n, m = map(int, input().split())
    if m == 0:
        print("No")
        exit()
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    for i in range(1, n + 1):
        if len(graph[i]) == 2:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 10

def solve():
    N,M = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(M)]
    edges.sort(key=lambda x:x[0])
    if len(edges) == 0:
        print("No")
        return
    if len(edges) == 1:
        print("Yes")
        return
    if len(edges) == 2:
        if edges[0][1] == edges[1][0]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(edges) == 3:
        if edges[0][1] == edges[1][0] and edges[1][1] == edges[2][0]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(edges) == 4:
        if edges[0][1] == edges[1][0] and edges[1][1] == edges[2][0] and edges[2][1] == edges[3][0]:
            print("Yes")
            return
        else:
            print("No")
            return
    if len(edges) == 5:
        if edges[0][1] == edges[1][0] and edges[1][1] == edges[2][0] and edges[2][1] == edges[3][0] and edges[3][1] == edges[4][0]:
            print("Yes")
            return
        else:
            print("No")
            return
    print("No")
    return
