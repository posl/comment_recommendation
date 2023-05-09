def main():
    # 標準入力から入力値を取得する
    d, n = map(int, input().split())
    # 100 でちょうど d 回割り切れる整数のリストを作成する
    num_list = [100 ** d * i for i in range(1, 101)]
    # num_list の n 番目の要素を出力する
    print(num_list[n - 1])

if __name__ == '__main__':
    main()