def main():
    #入力
    N, D = map(int, input().split())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    #座標の絶対値がD以下のものを数える
    count = 0
    for i in range(N):
        if (X[i]**2 + Y[i]**2)**(1/2) <= D:
            count += 1
    #出力
    print(count)

if __name__ == '__main__':
    main()