def main():
    N, M = map(int, input().split())
    #都市の組み合わせをリスト化
    city = []
    for i in range(1, N+1):
        for j in range(1, N+1):
            city.append([i, j])
    #道路の組み合わせをリスト化
    road = []
    for i in range(M):
        road.append(list(map(int, input().split())))
    #都市の組み合わせから道路の組み合わせを除外
    for i in range(len(city)):
        for j in range(len(road)):
            if city[i] == road[j]:
                city[i] = [0, 0]
    #都市の組み合わせからスタート地点とゴール地点が同じものを除外
    for i in range(len(city)):
        if city[i][0] == city[i][1]:
            city[i] = [0, 0]
    #都市の組み合わせからスタート地点とゴール地点が同じものを除外
    for i in range(len(city)):
        if city[i][0] == city[i][1]:
            city[i] = [0, 0]
    #都市の組み合わせから[0, 0]を除外
    city = [i for i in city if i != [0, 0]]
    #都市の組み合わせの数を出力
    print(len(city))

if __name__ == '__main__':
    main()