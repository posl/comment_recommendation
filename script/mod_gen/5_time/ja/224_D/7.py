def main():
    # グラフの頂点数 (頂点 1, 頂点 2, ..., 頂点 9)
    V = 9
    # グラフの辺数
    M = int(input())
    # グラフの辺
    edges = []
    for i in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))
    # 頂点に置かれているコマ
    p = list(map(int, input().split()))
    # 頂点 1, 頂点 2, ..., 頂点 9 にコマが置かれているかどうかを表す配列
    # (置かれている場合は True, 置かれていない場合は False とする)
    is_placed = [False] * (V + 1)
    for i in range(8):
        is_placed[p[i]] = True
    # 頂点 1, 頂点 2, ..., 頂点 9 にコマが置かれている場合のみ隣接行列の要素を True とする
    adj = [[False] * (V + 1) for _ in range(V + 1)]
    for u, v in edges:
        if is_placed[u] and is_placed[v]:
            adj[u][v] = True
            adj[v][u] = True
    # 頂点 1, 頂点 2, ..., 頂点 9 にコマが置かれている場合のみ隣接リストを作成する
    g = [[] for _ in range(V + 1)]
    for u, v in edges:
        if is_placed[u] and is_placed[v]:
            g[u].append(v)
            g[v].append(u)
    # 頂点 1, 頂点 2, ..., 頂点 9 にコマが置かれている場合のみ、
    # 頂点 1 から頂点 9 ま

if __name__ == '__main__':
    main()