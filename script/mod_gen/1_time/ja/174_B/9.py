def main():
    #入力
    N,D = map(int,input().split())
    #座標が入ったリスト
    L = []
    for i in range(N):
        X,Y = map(int,input().split())
        L.append([X,Y])
    #print(L)
    #原点からの距離がD以下であるような点の個数をカウントする
    count = 0
    for i in range(N):
        if (L[i][0]**2 + L[i][1]**2)**0.5 <= D:
            count += 1
    #出力
    print(count)

if __name__ == '__main__':
    main()