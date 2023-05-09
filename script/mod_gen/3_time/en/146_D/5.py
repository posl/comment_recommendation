def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N-1)]
    # 隣接リストを作成
    adjacent = [[] for _ in range(N+1)]
    for a, b in edges:
        adjacent[a].append(b)
        adjacent[b].append(a)
    # 各頂点の隣接頂点の色を格納
    colors = [[] for _ in range(N+1)]
    # 頂点1を根として探索
    stack = [1]
    while stack:
        # スタックから頂点を取り出す
        v = stack.pop()
        # 頂点vの隣接頂点の色を取得
        c = colors[v]
        # 頂点vの隣接頂点を取得
        a = adjacent[v]
        # 頂点vの隣接頂点の色を格納
        colors[v] = c
        # 頂点vの隣接頂点をスタックに格納
        for i in a:
            stack.append(i)
    # 頂点1を根として探索
    stack = [1]
    while stack:
        # スタックから頂点を取り出す
        v = stack.pop()
        # 頂点vの隣接頂点の色を取得
        c = colors[v]
        # 頂点vの隣接頂点を取得
        a = adjacent[v]
        # 頂点vの隣接頂点の色を格納
        colors[v] = c
        # 頂点vの隣接頂点をスタックに格納
        for i in a:
            stack.append(i)
    # 頂点1を根として探索
    stack = [1]
    while stack:
        # スタックから頂点を取り出す
        v = stack.pop()
        # 頂点vの隣接頂点の色を取得
        c = colors[v]
        #

if __name__ == '__main__':
    main()