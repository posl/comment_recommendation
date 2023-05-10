def main():
    N = int(input())
    edges = []
    for _ in range(N-1):
        a, b = map(int, input().split())
        edges.append((a, b))
    # print(edges)
    # 頂点の色の個数を数える
    color_num = [0 for _ in range(N+1)]
    for a, b in edges:
        color_num[a] += 1
        color_num[b] += 1
    # print(color_num)
    # 頂点の色の個数の最大値を求める
    max_color_num = max(color_num)
    # print(max_color_num)
    # 頂点の色の個数の最大値になるような頂点のリストを求める
    max_color_vertexes = []
    for i in range(1, N+1):
        if color_num[i] == max_color_num:
            max_color_vertexes.append(i)
    # print(max_color_vertexes)
    # 辺の色を決める
    edge_color = {}
    color = 1
    for a, b in edges:
        if a in max_color_vertexes and b in max_color_vertexes:
            edge_color[(a, b)] = color
            edge_color[(b, a)] = color
            color += 1
    # print(edge_color)
    # 辺の色を出力する
    print(max_color_num)
    for a, b in edges:
        print(edge_color[(a, b)])
