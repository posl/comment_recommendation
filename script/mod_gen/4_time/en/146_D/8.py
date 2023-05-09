def main():
    N = int(input())
    #各頂点の隣接頂点を格納するリスト
    node = [[] for _ in range(N+1)]
    #辺の色を格納するリスト
    color = [0 for _ in range(N)]
    for i in range(N-1):
        a,b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    #頂点の隣接頂点の色を格納するリスト
    color_node = [[] for _ in range(N+1)]
    #頂点1から順に隣接頂点の色を格納するリストに格納
    for i in range(N-1):
        for j in node[i+1]:
            color_node[i+1].append(color[j-1])
    #頂点の隣接頂点の色を格納するリストを走査し、頂点の隣接頂点の色が同じものがない色を辺の色として格納する
    for i in range(N-1):
        for j in range(1,N+1):
            if j not in color_node[i+1]:
                color[i] = j
                break
    #辺の色の最大値を出力
    print(max(color))
    #辺の色を出力
    for i in color:
        print(i)

if __name__ == '__main__':
    main()