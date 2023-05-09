Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n,m=list(map(int,input().split()))
    u=[]
    v=[]
    for _ in range(m):
        ui,vi=list(map(int,input().split()))
        u.append(ui)
        v.append(vi)
    return n,m,u,v

=======
Suggestion 2

def get_input():
    N, M = map(int, input().split())
    U = []
    V = []
    for i in range(M):
        u, v = map(int, input().split())
        U.append(u)
        V.append(v)
    return N, M, U, V

=======
Suggestion 3

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    if not graph.has_key(start):
        return []

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

=======
Suggestion 4

def solve():
    N, M = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        G[u].add(v)
        G[v].add(u)

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if j not in G[i]:
                continue
            for k in range(j + 1, N):
                if k not in G[i]:
                    continue
                if k not in G[j]:
                    continue
                ans += 1

    print(ans)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        edges.append(list(map(int, input().split())))
    count = 0
    for i in range(M):
        a = edges[i][0]
        b = edges[i][1]
        for j in range(i + 1, M):
            c = edges[j][0]
            d = edges[j][1]
            if b == c:
                if [a, d] in edges:
                    count += 1
            elif b == d:
                if [a, c] in edges:
                    count += 1
            elif a == c:
                if [b, d] in edges:
                    count += 1
            elif a == d:
                if [b, c] in edges:
                    count += 1
    print(count)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    edge = []
    for i in range(m):
        edge.append(list(map(int, input().split())))
    ans = 0
    for i in range(m):
        for j in range(i+1, m):
            if edge[i][0] in edge[j] and edge[i][1] in edge[j]:
                ans += 1
    print(ans)

=======
Suggestion 7

def get_input():
    N, M = map(int, input().split())
    edges = []
    for i in range(M):
        U, V = map(int, input().split())
        edges.append((U, V))
    return N, M, edges

=======
Suggestion 8

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            paths += find_all_paths(graph, node, end, path)
    return paths
N,M = map(int,raw_input().split())
graph = {}
for i in range(M):
    u,v = map(int,raw_input().split())
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]
cnt = 0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        paths = find_all_paths(graph, i, j)
        for path in paths:
            if len(path) == 3:
                cnt += 1
print cnt

=======
Suggestion 9

def get_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    return n, m, edges

=======
Suggestion 10

def find_num_of_triangles(n, edges):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if edges[i][j] == 1:
                for k in range(j+1, n):
                    if edges[i][k] == 1 and edges[j][k] == 1:
                        count += 1
    return count
