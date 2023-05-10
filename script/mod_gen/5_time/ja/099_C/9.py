def main():
    n = int(input())
    # 6,9の何乗かで引き出す
    # 6,9の何乗かのリスト
    # 6のリスト
    six_list = []
    # 9のリスト
    nine_list = []
    # 6のリストを作成
    for i in range(1, 100):
        six_list.append(6**i)
    # 9のリストを作成
    for i in range(1, 100):
        nine_list.append(9**i)
    # 6,9のリストを作成
    six_nine_list = six_list + nine_list
    # 6,9のリストをソート
    six_nine_list.sort()
    # 6,9のリストを逆順にする
    six_nine_list.reverse()
    # 6,9のリストの長さ
    six_nine_list_len = len(six_nine_list)
    # 引き出す最小回数
    min_count = 0
    # 引き出した金額
    money = 0
    # 引き出す
    while True:
        # 引き出す金額がn以上なら終了
        if money >= n:
            break
        # 引き出す金額がn未満なら
        else:
            # 6,9のリストをループ
            for i in range(six_nine_list_len):
                # 引き出す金額がn以上なら終了
                if money >= n:
                    break
                # 引き出す金額がn未満なら
                else:
                    # 引き出す金額に6,9のリストの値を足す
                    money += six_nine_list[i]
                    # 引き出す最小回数を1増やす
                    min_count += 1
    # 引き出す最小回数を出力
    print(min_count)

if __name__ == '__main__':
    main()