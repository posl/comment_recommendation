def main():
    n = int(input())
    uvw = []
    for i in range(n-1):
        uvw.append(list(map(int,input().split())))
    print(uvw)
    # n = 3
    # uvw = [[1, 2, 10], [2, 3, 20]]
    # n = 5
    # uvw = [[1, 2, 1], [2, 3, 2], [4, 2, 5], [3, 5, 14]]
    # 木の頂点の数
    N = n
    # 木の辺の数
    M = n-1
    # 頂点の数
    V = N
    # 辺の数
    E = M
    # 頂点の最大数
    MAX_V = 100000
    # 辺の最大数
    MAX_E = 100000
    # グラフ
    G = [[0 for i in range(MAX_V)] for j in range(MAX_E)]
    # 重み
    W = [[0 for i in range(MAX_V)] for j in range(MAX_E)]
    # グラフの初期化
    def graph_init():
        for i in range(MAX_V):
            for j in range(MAX_V):
                G[i][j] = 0
    # 辺の追加
    def add_edge(a, b, w):
        G[a].append(b)
        W[a].append(w)
    # BFS
    def bfs(s):
        global d
        global p
        global color
        for i in range(MAX_V):
            d[i] = float('inf')
            p[i] = -1
        q = []
        q.append(s)
        d[s] = 0
        color[s] = 1
        while len(q) != 0:
            u = q.pop(0)
            for i in range(len(G[u])):
                v = G[u][i]
                if color[v] == 0:
                    color[v] = 1
                    d[v] = d[u] + 1
                    p[v] = u
                    q.append(v)
            color[u] = 2
    # 最短経路

if __name__ == '__main__':
    main()