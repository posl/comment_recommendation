Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    edges.sort(key=lambda x: x[2], reverse=True)
    parents = list(range(n+1))
    sizes = [1] * (n+1)

    def find(x):
        if parents[x] == x:
            return x
        else:
            parents[x] = find(parents[x])
            return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            if sizes[px] < sizes[py]:
                px, py = py, px
            parents[py] = px
            sizes[px] += sizes[py]

    ans = 0
    for u, v, w in edges:
        ans += w * sizes[find(u)] * sizes[find(v)]
        union(u, v)
    print(ans)

=======
Suggestion 2

def read_input():
    n = int(input())
    edges = []
    for i in range(n-1):
        u,v,w = map(int,input().split())
        edges.append((w,u,v))
    return n,edges

=======
Suggestion 3

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        edge = list(map(int, input().split()))
        edges.append(edge)
    edges.sort(key=lambda x:x[2])
    # print(edges)
    # print(edges[0][2])
    # print(edges[1][2])
    # print(edges[n-2][2])
    # print(edges[n-3][2])
    # print(edges[n-4][2])
    # print(edges[n-5][2])
    # print(edges[n-6][2])
    # print(edges[n-7][2])
    # print(edges[n-8][2])
    # print(edges[n-9][2])
    # print(edges[n-10][2])
    # print(edges[n-11][2])
    # print(edges[n-12][2])
    # print(edges[n-13][2])
    # print(edges[n-14][2])
    # print(edges[n-15][2])
    # print(edges[n-16][2])
    # print(edges[n-17][2])
    # print(edges[n-18][2])
    # print(edges[n-19][2])
    # print(edges[n-20][2])
    # print(edges[n-21][2])
    # print(edges[n-22][2])
    # print(edges[n-23][2])
    # print(edges[n-24][2])
    # print(edges[n-25][2])
    # print(edges[n-26][2])
    # print(edges[n-27][2])
    # print(edges[n-28][2])
    # print(edges[n-29][2])
    # print(edges[n-30][2])
    # print(edges[n-31][2])
    # print(edges[n-32][2])
    # print(edges[n-33][2])
    # print(edges[n-34][2])
    # print(edges[n-35][2])
    # print(edges[n-36][2])
    # print(edges[n-37][2])
    # print(edges[n-38][2])
    # print(edges[n-39][2])
    # print(edges[n-40][2])
    # print(edges[n-41][2])
    # print(edges[n-42][2])
    # print(edges[n-43][2])
    # print(edges[n-44][2])

=======
Suggestion 4

def main():
    # 读取数据
    N = int(input())
    edges = []
    for i in range(N - 1):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    # 按权重排序
    edges.sort(key=lambda e: e[2])
    # 初始化并查集
    uf = UnionFind(N)
    # 初始化ans
    ans = 0
    # 遍历所有边
    for u, v, w in edges:
        # 计算u和v的连通分量大小
        size = uf.size(u) * uf.size(v)
        # 计算答案
        ans += size * w
        # 连接u和v
        uf.unite(u, v)
    # 输出答案
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    u = [0] * (n - 1)
    v = [0] * (n - 1)
    w = [0] * (n - 1)
    for i in range(n - 1):
        u[i], v[i], w[i] = map(int, input().split())
    print(solve(n, u, v, w))

=======
Suggestion 6

def dfs(v, p, d):
    global ans
    ans += d
    for i in range(len(g[v])):
        if g[v][i][0] != p:
            dfs(g[v][i][0], v, max(d, g[v][i][1]))

n = int(input())
g = [[] for i in range(n)]
for i in range(n - 1):
    u, v, w = map(int, input().split())
    g[u - 1].append((v - 1, w))
    g[v - 1].append((u - 1, w))
ans = 0
dfs(0, -1, 0)
print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    edges = []
    for i in range(n-1):
        edges.append(list(map(int, input().split())))
    edges.sort(key=lambda x: x[2])

    cnt = [1] * n
    ans = 0
    for u, v, w in edges:
        ans += w * cnt[u-1] * cnt[v-1]
        cnt[u-1] += cnt[v-1]
    print(ans)

=======
Suggestion 8

def get_input():
    n = int(input())
    graph = {}
    for i in range(n-1):
        u, v, w = map(int, input().split())
        if u not in graph:
            graph[u] = [(v, w)]
        else:
            graph[u].append((v, w))
        if v not in graph:
            graph[v] = [(u, w)]
        else:
            graph[v].append((u, w))
    return graph

=======
Suggestion 9

def main():
    pass

=======
Suggestion 10

def main():
    N = int(input())
    edges = []
    for i in range(N-1):
        edges.append(list(map(int, input().split())))
    edges = sorted(edges, key=lambda x: x[2], reverse=True)
    # print(edges)
    # print(edges[0][2])
    # print(edges[0][0])
    # print(edges[0][1])
    # print(edges[1][2])
    # print(edges[1][0])
    # print(edges[1][1])
    # print(edges[2][2])
    # print(edges[2][0])
    # print(edges[2][1])
    # print(edges[3][2])
    # print(edges[3][0])
    # print(edges[3][1])
    # print(edges[4][2])
    # print(edges[4][0])
    # print(edges[4][1])
    # print(edges[5][2])
    # print(edges[5][0])
    # print(edges[5][1])
    # print(edges[6][2])
    # print(edges[6][0])
    # print(edges[6][1])
    # print(edges[7][2])
    # print(edges[7][0])
    # print(edges[7][1])
    # print(edges[8][2])
    # print(edges[8][0])
    # print(edges[8][1])
    # print(edges[9][2])
    # print(edges[9][0])
    # print(edges[9][1])
    # print(edges[10][2])
    # print(edges[10][0])
    # print(edges[10][1])
    # print(edges[11][2])
    # print(edges[11][0])
    # print(edges[11][1])
    # print(edges[12][2])
    # print(edges[12][0])
    # print(edges[12][1])
    # print(edges[13][2])
    # print(edges[13][0])
    # print(edges[13][1])
    # print(edges[14][2])
    # print(edges[14][0])
    # print(edges[14][1])
    # print(edges[15][2])
    # print(edges[15][0])
    # print(edges[15][1])
    # print(edges[16][2])
    # print(edges[
