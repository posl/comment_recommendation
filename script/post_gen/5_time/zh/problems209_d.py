Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    print("Hello World!")
    return

=======
Suggestion 2

def find(x):
    if x == par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 3

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 4

def find(x):
    global parent
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 5

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

=======
Suggestion 6

def main():
    n, q = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for _ in range(q):
        c, d = map(int, input().split())
        if c == d:
            print('Town')
        else:
            if len(graph[c]) == 1 and len(graph[d]) == 1:
                print('Road')
            else:
                print('Town')

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n-1)]
    cd = [list(map(int, input().split())) for _ in range(q)]

    # 木構造を作る
    tree = [[] for _ in range(n+1)]
    for a, b in ab:
        tree[a].append(b)
        tree[b].append(a)

    # 木の根を求める
    root = 1
    for i in range(1, n+1):
        if len(tree[i]) == 1:
            root = i
            break

    # 木の深さを求める
    depth = [0] * (n+1)
    def dfs(u, p):
        for v in tree[u]:
            if v != p:
                depth[v] = depth[u] + 1
                dfs(v, u)
    dfs(root, -1)

    # 各クエリについて、高橋と青木の位置関係を調べる
    for c, d in cd:
        # 木の深さが同じなら Town
        if depth[c] == depth[d]:
            print('Town')
        # 違うなら Road
        else:
            print('Road')

=======
Suggestion 8

def get_input():
    n, q = map(int, input().split())
    roads = []
    for i in range(n-1):
        roads.append(list(map(int, input().split())))
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    return n, q, roads, queries

=======
Suggestion 9

def main():
    n, q = [int(i) for i in input().split()]
    roads = []
    for i in range(n-1):
        a, b = [int(i) for i in input().split()]
        roads.append((a, b))
    queries = []
    for i in range(q):
        c, d = [int(i) for i in input().split()]
        queries.append((c, d))
    for query in queries:
        c, d = query
        if (c, d) in roads or (d, c) in roads:
            print("Road")
        else:
            print("Town")
