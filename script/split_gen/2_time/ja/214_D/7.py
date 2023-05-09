def main():
    N = int(input())
    #各頂点に隣接する頂点のリスト
    adjacent = [[] for _ in range(N)]
    #各頂点に隣接する辺の重みのリスト
    weight = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        adjacent[u - 1].append(v - 1)
        adjacent[v - 1].append(u - 1)
        weight[u - 1].append(w)
        weight[v - 1].append(w)
    #各頂点からの距離
    dist = [0] * N
    #各頂点からの距離を計算
    def calc_dist(v, p):
        for i, u in enumerate(adjacent[v]):
            if u == p:
                continue
            dist[u] = dist[v] + weight[v][i]
            calc_dist(u, v)
    calc_dist(0, -1)
    #各頂点の深さ
    depth = [0] * N
    #各頂点の深さを計算
    def calc_depth(v, p):
        for u in adjacent[v]:
            if u == p:
                continue
            depth[u] = depth[v] + 1
            calc_depth(u, v)
    calc_depth(0, -1)
    #各頂点に隣接する頂点のリスト
    adjacent2 = [[] for _ in range(N)]
    #各頂点に隣接する辺の重みのリスト
    weight2 = [[] for _ in range(N)]
    #各頂点に隣接する頂点のリストを作成
    for i in range(N):
        for j in range(len(adjacent[i])):
            if depth[adjacent[i][j]] > depth[i]:
                adjacent2[i].append(adjacent[i][j])
                weight2[i].append(weight[i][j])
    #print(adjacent2)
    #print(weight2)
    #各頂点に隣接する頂点のリスト
    adjacent3 = [[] for
