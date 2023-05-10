def main():
    n = int(input())
    edges = []
    for _ in range(n-1):
        edges.append(list(map(int, input().split())))
    #print("edges:", edges)
    # 色の数を決める
    max_color = 0
    for edge in edges:
        if edge[0] > max_color:
            max_color = edge[0]
        if edge[1] > max_color:
            max_color = edge[1]
    #print("max_color:", max_color)
    # 色の数を出力
    print(max_color)
    # 辺の色を決める
    for edge in edges:
        print(edge[0])

if __name__ == '__main__':
    main()