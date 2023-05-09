def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    # 木の辺の色を塗る
    # 隣接する頂点は同じ色にはできない
    # 隣接する頂点がすべて異なる色で塗られていれば、色の数は最小
    # 隣接する頂点が同じ色で塗られている場合、隣接する頂点の色を変える
    # 隣接する頂点の色を取得する
    # すでに塗られている色を取得する
    # 隣接する頂点の色を取得する
    def get_adjacent_color(v, parent):
        adjacent_color = []
        for e in edges:
            if e[0] == v or e[1] == v:
                if e[0] == v:
                    adjacent_v = e[1]
                else:
                    adjacent_v = e[0]
                if adjacent_v != parent:
                    adjacent_color.append(color[e])
        return adjacent_color
    # 隣接する頂点の色を取得する
    # すでに塗られている色を取得する
    # 隣接する頂点の色を取得する
    def get_color(v, parent):
        for i in range(1, N+1):
            if i not in get_adjacent_color(v, parent):
                return i
    # 木の辺を塗る
    # 隣接する頂点の色を取得する
    # すでに塗られている色を取得する
    # 隣接する頂点の色を取得する
    color = [0] * (N-1)
    for i in range(N-1):
        color[i] = get_color(edges[i][0], edges[i][1])
    # 隣接する頂点の色を取得する
    # すでに塗られている
