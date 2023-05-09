def main():
    #入力
    X, Y = map(int, input().split())
    #鶴の数
    t = 0
    #亀の数
    k = 0
    #鶴の数が2匹以上のとき
    while t < X:
        #鶴の数を1匹ずつ増やす
        t += 1
        #亀の数を計算
        k = X - t
        #足の数が合っているか確認
        if 2 * t + 4 * k == Y:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()