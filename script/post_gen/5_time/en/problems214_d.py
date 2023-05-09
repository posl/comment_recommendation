Synthesizing 10/10 solutions

=======
Suggestion 1

def readinput():
    n=int(input())
    edges=[]
    for _ in range(n-1):
        u,v,w=list(map(int,input().split()))
        edges.append((u,v,w))
    return n,edges

=======
Suggestion 2

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    uf = UnionFind(n)
    ans = 0
    for w, u, v in edges:
        ans += w * uf.size(u) * uf.size(v)
        uf.union(u, v)
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
    edges.sort()
    ans = 0
    uf = UnionFind(N)
    for w, u, v in edges:
        ans += uf.size(u) * uf.size(v) * w
        uf.unite(u, v)
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    u = []
    v = []
    w = []
    for i in range(n-1):
        u_i, v_i, w_i = map(int, input().split())
        u.append(u_i)
        v.append(v_i)
        w.append(w_i)

    print(u)
    print(v)
    print(w)

=======
Suggestion 5

def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        edges.append((u,v,w))
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    ans = 0
    for u, v, w in edges:
        ans += uf.size(u) * uf.size(v) * w
        uf.union(u, v)
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    edge = []
    for i in range(n-1):
        u, v, w = map(int, input().split())
        edge.append([u, v, w])
    edge.sort(key=lambda x:x[2])
    #print(edge)
    #print(edge[0])
    #print(edge[0][2])
    #print(edge[0][0])
    #print(edge[0][1])
    #print(edge[1])
    #print(edge[1][2])
    #print(edge[1][0])
    #print(edge[1][1])
    #print(edge[2])
    #print(edge[2][2])
    #print(edge[2][0])
    #print(edge[2][1])
    #print(edge[3])
    #print(edge[3][2])
    #print(edge[3][0])
    #print(edge[3][1])
    #print(edge[4])
    #print(edge[4][2])
    #print(edge[4][0])
    #print(edge[4][1])
    #print(edge[5])
    #print(edge[5][2])
    #print(edge[5][0])
    #print(edge[5][1])
    #print(edge[6])
    #print(edge[6][2])
    #print(edge[6][0])
    #print(edge[6][1])
    #print(edge[7])
    #print(edge[7][2])
    #print(edge[7][0])
    #print(edge[7][1])
    #print(edge[8])
    #print(edge[8][2])
    #print(edge[8][0])
    #print(edge[8][1])
    #print(edge[9])
    #print(edge[9][2])
    #print(edge[9][0])
    #print(edge[9][1])
    #print(edge[10])
    #print(edge[10][2])
    #print(edge[10][0])
    #print(edge[10][1])
    #print(edge[11])
    #print(edge[11][2])
    #print(edge[11][0])
    #print(edge[11][1])
    #print(edge[12])
    #print(edge[12][2])
    #print(edge[12][0])
    #print(edge[12][

=======
Suggestion 7

def main():
    n = int(input())
    edges = []
    for i in range(n - 1):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    edges.sort(key = lambda x: x[2])
    uf = UnionFind(n)
    ans = 0
    for a, b, c in edges:
        ans += uf.size(a) * uf.size(b) * c
        uf.union(a, b)
    print(ans)

=======
Suggestion 8

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

=======
Suggestion 9

def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n - 1)]
    edges.sort(key=lambda x: x[2])

    parents = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    def find(x):
        if parents[x] == x:
            return x
        else:
            parents[x] = find(parents[x])
            return parents[x]

    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            parents[x] = y
        else:
            parents[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1

    def same(x, y):
        return find(x) == find(y)

    def weight(x, y):
        return edges[x][2] + edges[y][2]

    def kruskal():
        res = 0
        for i in range(n - 1):
            if not same(edges[i][0] - 1, edges[i][1] - 1):
                unite(edges[i][0] - 1, edges[i][1] - 1)
                res += weight(i, i)
        return res

    print(kruskal())

=======
Suggestion 10

def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x:x[2])
    nodes = [x for x in range(N)]
    def root(x):
        if nodes[x] == x:
            return x
        else:
            nodes[x] = root(nodes[x])
            return nodes[x]
    def unite(x, y):
        nodes[root(x)] = root(y)
    def same(x, y):
        return root(x) == root(y)
    def weight(x, y):
        if same(x, y):
            return 0
        else:
            unite(x, y)
            return edges.pop()[2]
    ans = 0
    for i in range(N-1):
        for j in range(i+1, N):
            ans += weight(i, j)
    print(ans)
