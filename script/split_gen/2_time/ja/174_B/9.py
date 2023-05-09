def main():
    #入力
    N, D = map(int, input().split())
    #print(N, D)
    #N個の点の座標をリストに格納
    list_xy = []
    for i in range(N):
        X, Y = map(int, input().split())
        list_xy.append([X, Y])
    #print(list_xy)
    #原点からの距離がD以下であるような点の個数をカウント
    count = 0
    for i in range(N):
        if (list_xy[i][0]**2 + list_xy[i][1]**2)**0.5 <= D:
            count += 1
    #出力
    print(count)
