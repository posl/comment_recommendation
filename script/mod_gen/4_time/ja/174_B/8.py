def main():
    # 標準入力の取得
    n, d = map(int, input().split())
    # 点の数
    #print(n)
    # 原点からの距離
    #print(d)
    # 座標のリスト
    point_list = []
    for i in range(n):
        x, y = map(int, input().split())
        point_list.append([x, y])
    #print(point_list)
    # 原点からの距離が d 以下の点の個数
    count = 0
    for point in point_list:
        if (point[0]**2 + point[1]**2)**(1/2) <= d:
            count += 1
    print(count)

if __name__ == '__main__':
    main()