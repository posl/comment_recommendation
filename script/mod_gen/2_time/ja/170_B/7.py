def main():
    # 鶴と亀の数
    X, Y = map(int, input().split())
    # 鶴の数
    t = 0
    # 亀の数
    k = 0
    # 鶴の数を変化させる
    for i in range(X + 1):
        t = i
        # 亀の数を計算する
        k = X - t
        # 足の本数が合致するか判定する
        if t * 2 + k * 4 == Y:
            print("Yes")
            exit(0)
    # どちらも該当しない場合
    print("No")

if __name__ == '__main__':
    main()