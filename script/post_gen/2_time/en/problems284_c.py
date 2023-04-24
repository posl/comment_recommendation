Synthesizing 10/10 solutions

=======
Suggestion 1

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    for _ in range(M):
        a, b = map(int, input().split())
        uf.union(a-1, b-1)
    print(uf.group_count())

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    edges = []
    for _ in range(M):
        edges.append(list(map(int, input().split())))
    edges = sorted(edges, key=lambda x: x[0])
    group = [0] * N
    group[edges[0][0] - 1] = 1
    for i in range(1, N):
        if edges[i][0] == edges[i - 1][0]:
            group[edges[i][0] - 1] = group[edges[i - 1][0] - 1]
        else:
            group[edges[i][0] - 1] = group[edges[i - 1][0] - 1] + 1
    for i in range(M):
        group[edges[i][1] - 1] = group[edges[i][0] - 1]
    print(max(group))

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (N + 1)
    count = 0
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(graph, i, visited)
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    edges = [list(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N)]
    for u, v in edges:
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    visited = [False] * N
    ans = 0
    for i in range(N):
        if visited[i]:
            continue
        ans += 1
        visited[i] = True
        stack = [i]
        while stack:
            v = stack.pop()
            for u in graph[v]:
                if visited[u]:
                    continue
                visited[u] = True
                stack.append(u)
    print(ans)

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    edges = [list(map(int, input().split())) for _ in range(M)]
    edges.sort()
    ans = 0
    for i in range(M):
        if i == 0:
            ans += 1
            continue
        if edges[i][0] != edges[i - 1][0] and edges[i][1] != edges[i - 1][1]:
            ans += 1
    print(ans + 1)

main()

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    graph = [[0 for i in range(N)] for j in range(N)]
    for i in range(M):
        u, v = map(int, input().split())
        graph[u-1][v-1] = 1
        graph[v-1][u-1] = 1
    visited = [False] * N
    count = 0
    for i in range(N):
        if not visited[i]:
            count += 1
            dfs(i, graph, visited)
    print(count)

=======
Suggestion 8

def dfs(graph, v, visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph, i, visited)
    return

=======
Suggestion 9

def find_root(x):
    if x == root[x]:
        return x
    else:
        root[x] = find_root(root[x])
        return root[x]

=======
Suggestion 10

def main():
    import sys
    from collections import defaultdict
    import numpy as np

    def dfs(G, v):
        if v in G:
            for vv in G[v]:
                if vv in G:
                    G = dfs(G, vv)
            del G[v]
        return G

    def connected_components(G):
        components = []
        while G:
            v = next(iter(G))
            G = dfs(G, v)
            components.append(v)
        return len(components)

    def input():
        return sys.stdin.readline().rstrip()

    N, M = map(int, input().split())
    G = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    print(connected_components(G))
