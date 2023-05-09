def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    # 連結成分の個数をカウントする
    count = 0
    # 連結成分の判定をする
    # 連結成分に属するマスは、白→黒に塗る
    for i in range(N):
        if X[i] == 0 and Y[i] == 0:
            X[i] = 1
            Y[i] = 1
            count += 1
            continue
        if X[i] == 0 or Y[i] == 0:
            X[i] = 1
            Y[i] = 1
            count += 1
            continue
        if X[i] == Y[i] or X[i] == -Y[i]:
            X[i] = 1
            Y[i] = 1
            count += 1
            continue
        if X[i] > 0 and Y[i] > 0:
            if X[i] % 2 == 0 and Y[i] % 2 == 0:
                X[i] = 1
                Y[i] = 1
                count += 1
                continue
            if X[i] % 2 == 1 and Y[i] % 2 == 1:
                X[i] = 1
                Y[i] = 1
                count += 1
                continue
        if X[i] < 0 and Y[i] < 0:
            if X[i] % 2 == 0 and Y[i] % 2 == 0:
                X[i] = 1
                Y[i] = 1
                count += 1
                continue
            if X[i] % 2 == 1 and Y[i] % 2 == 1:
                X[i] = 1
                Y[i] = 1
                count += 1
                continue
    print(count)

if __name__ == '__main__':
    main()