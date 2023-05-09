def main():
    N = int(input())
    edges = []
    for _ in range(N - 1):
        a, b = map(int, input().split())
        edges.append((a, b))
    # グラフの隣接リストを作成
    graph = [[] for _ in range(N + 1)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    # 頂点1から幅優先探索を行い、各頂点の深さを求める
    depth = [-1] * (N + 1)
    depth[1] = 0
    q = [1]
    while q:
        v = q.pop()
        for w in graph[v]:
            if depth[w] != -1:
                continue
            depth[w] = depth[v] + 1
            q.append(w)
    # 深さが奇数の頂点を赤、偶数の頂点を青とする
    colors = [''] * (N + 1)
    for i in range(1, N + 1):
        colors[i] = 'R' if depth[i] % 2 == 0 else 'B'
    # 各頂点の隣接頂点の色を取得
    adjacent_colors = []
    for a, b in edges:
        if colors[a] == 'R':
            adjacent_colors.append(colors[b])
        else:
            adjacent_colors.append(colors[a])
    # 隣接頂点の色の種類数を求める
    adjacent_colors = set(adjacent_colors)
    print(len(adjacent_colors))
    for color in colors[1:]:
        print(color)
