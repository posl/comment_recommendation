Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    N, Q = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    CD = [list(map(int, input().split())) for _ in range(Q)]

    graph = [[] for _ in range(N+1)]
    for a, b in AB:
        graph[a].append(b)
        graph[b].append(a)

    dist = [-1] * (N+1)
    dist[1] = 0
    stack = [1]
    while stack:
        now = stack.pop()
        for next in graph[now]:
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                stack.append(next)

    for c, d in CD:
        if abs(dist[c] - dist[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        G[a].append(b)
        G[b].append(a)
    dist = [-1] * N
    dist[0] = 0
    stack = [0]
    while stack:
        v = stack.pop()
        for u in G[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                stack.append(u)
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if (dist[c] + dist[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')
    return

=======
Suggestion 3

def main():
    n, q = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(n - 1)]
    queries = [list(map(int, input().split())) for _ in range(q)]

    #print(roads)
    #print(queries)

    # make graph
    graph = [[] for _ in range(n + 1)]
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    #print(graph)

    # make parent list
    parents = [0 for _ in range(n + 1)]
    #print(parents)

    # make depth list
    depths = [0 for _ in range(n + 1)]
    #print(depths)

    # make visited list
    visited = [False for _ in range(n + 1)]
    #print(visited)

    # make depth first search
    def dfs(graph, parents, depths, visited, v, p, d):
        #print("v: {}, p: {}, d: {}".format(v, p, d))
        visited[v] = True
        depths[v] = d
        parents[v] = p
        for i in graph[v]:
            if not visited[i]:
                dfs(graph, parents, depths, visited, i, v, d + 1)

    # start depth first search
    dfs(graph, parents, depths, visited, 1, 0, 0)

    #print(parents)
    #print(depths)

    # make lca
    def lca(parents, depths, u, v):
        #print("u: {}, v: {}".format(u, v))
        #print("depths[u]: {}, depths[v]: {}".format(depths[u], depths[v]))
        if depths[u] > depths[v]:
            u, v = v, u
        #print("u: {}, v: {}".format(u, v))
        while depths[u] != depths[v]:
            #print("u: {}, v: {}".format(u, v))
            v = parents[v]
        #print("u: {}, v: {}".format(u, v))
        while u != v:
            #print("u: {}, v: {}".format(u, v))
            u = parents[u]
            v = parents[v]

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    tree = [set() for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        tree[a-1].add(b-1)
        tree[b-1].add(a-1)
    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        from collections import deque
        que = deque()
        que.append((c, 0))
        dist = [-1] * N
        while que:
            v, d = que.popleft()
            dist[v] = d
            for u in tree[v]:
                if dist[u] == -1:
                    que.append((u, d+1))
        if dist[d] % 2 == 0:
            print("Town")
        else:
            print("Road")

=======
Suggestion 5

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

=======
Suggestion 6

def find_root(x, parent):
    if parent[x] == x:
        return x
    else:
        parent[x] = find_root(parent[x], parent)
        return parent[x]

=======
Suggestion 7

def find_root(tree, x):
    if tree[x] == x:
        return x
    else:
        tree[x] = find_root(tree, tree[x])
        return tree[x]

=======
Suggestion 8

def find_root(x):
    global root
    if root[x] == x:
        return x
    else:
        root[x] = find_root(root[x])
        return root[x]

=======
Suggestion 9

def find_root(node, root):
    if node == root[node]:
        return node
    else:
        root[node] = find_root(root[node], root)
        return root[node]

=======
Suggestion 10

def bfs(start, goal, graph):
    queue = [(start, 0)]
    done = set()
    while queue:
        node, depth = queue.pop(0)
        if node == goal:
            return depth
        if node in done:
            continue
        done.add(node)
        for neighbor in graph[node]:
            queue.append((neighbor, depth + 1))
    return None
