def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    M = max(W)
    # 体重の最大値を最大のXにする
    X = M
    # 体重の最大値を最小のXにする
    Y = 0
    # XとYの差が1になるまで繰り返す
    while X - Y > 1:
        # XとYの中間値をZにする
        Z = (X + Y) // 2
        # ZをXにする
        X = Z
        # 高橋君が正しく判定できる人数を初期化
        count = 0
        # 体重がZ未満の人が子供であることを判定
        for i in range(N):
            if W[i] < Z and S[i] == '0':
                count += 1
            elif W[i] >= Z and S[i] == '1':
                count += 1
        # 高橋君が正しく判定できる人数がN人未満の場合
        if count < N:
            # ZをYにする
            Y = Z
    # 高橋君が正しく判定できる人数を出力
    print(count)

if __name__ == '__main__':
    main()