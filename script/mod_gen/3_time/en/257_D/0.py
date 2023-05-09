def main():
    N = int(input())
    X = []
    Y = []
    P = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        X.append(x)
        Y.append(y)
        P.append(p)
    # x,y座標の最大値と最小値を求める
    x_min = min(X)
    x_max = max(X)
    y_min = min(Y)
    y_max = max(Y)
    # 総当たりで各座標にたどり着けるか調べる
    # たどり着けない場合は、距離を計算して、その距離がPの何倍かを求める
    # その倍数の最大値を求める
    # その最大値が答え
    ans = 0
    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max + 1):
            max_distance = 0
            for i in range(N):
                distance = abs(x - X[i]) + abs(y - Y[i])
                if max_distance < distance:
                    max_distance = distance
            if ans < max_distance / P[i]:
                ans = max_distance / P[i]
    print(int(ans))

if __name__ == '__main__':
    main()