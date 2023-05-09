def main():
    N, X, Y = map(int, input().split())
    #N, X, Y = 10, 4, 8
    #N, X, Y = 3, 1, 3
    #N, X, Y = 7, 3, 7
    #N, X, Y = 5, 2, 4
    #N, X, Y = 10, 4, 8
    #辺のリスト
    edges = []
    #頂点iと頂点jの距離がkの場合の整数の組(i,j)の数を格納するリスト
    distance = [0] * (N-1)
    #print("distance:", distance)
    #辺のリストを作成
    for i in range(1, N):
        edges.append((i, i+1))
    edges.append((X, Y))
    #print("edges:", edges)
    #辺のリストから頂点iと頂点jの距離を求め、distanceに格納
    for edge in edges:
        #print("edge:", edge)
        distance[abs(edge[0] - edge[1]) - 1] += 1
    #print("distance:", distance)
    #distanceの要素を出力
    for d in distance:
        print(d)

if __name__ == '__main__':
    main()