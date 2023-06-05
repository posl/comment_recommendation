def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    # 友達関係を表すグラフを作成する
    G = [[] for _ in range(N)]
    for a, b in AB:
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    # ブロック関係を表すグラフを作成する
    B = [[] for _ in range(N)]
    for c, d in CD:
        B[c - 1].append(d - 1)
        B[d - 1].append(c - 1)
    # 幅優先探索を行う
    # 頂点sから各頂点への最短距離を求める
    def bfs(s, G):
        dist = [-1] * N
        que = []
        dist[s] = 0
        que.append(s)
        while que:
            v = que.pop(0)
            for nv in G[v]:
                if dist[nv] == -1:
                    dist[nv] = dist[v] + 1
                    que.append(nv)
        return dist
    # 頂点0を始点とした時の最短距離を求める
    dist = bfs(0, G)
    # 頂点0から各頂点への最短距離が2以下であれば、
    # 友達候補となる頂点である
    ans = [0] * N
    for i in range(N):
        if dist[i] <= 2:
            ans[i] = 1
    # 頂点0から各頂点への最短距離が2以下である頂点を
    # 頂点とするグラフを作成する
    G2 = [[] for _ in range(N)]
    for i in range(N):

if __name__ == '__main__':
    main()