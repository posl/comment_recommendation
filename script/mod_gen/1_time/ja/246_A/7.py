def main():
    # 3つの座標を取得
    c1 = list(map(int, input().split()))
    c2 = list(map(int, input().split()))
    c3 = list(map(int, input().split()))
    # 座標のリストを作成
    c_list = [c1, c2, c3]
    #print(c_list)
    # x座標のリストを作成
    x_list = []
    # y座標のリストを作成
    y_list = []
    # 座標のリストからx座標とy座標のリストを作成
    for i in range(3):
        x_list.append(c_list[i][0])
        y_list.append(c_list[i][1])
    #print(x_list)
    #print(y_list)
    # x座標とy座標のリストから重複する値を削除
    x_list = list(set(x_list))
    y_list = list(set(y_list))
    #print(x_list)
    #print(y_list)
    # x座標のリストから重複する値を削除した後のリストの要素数が2の場合
    if len(x_list) == 2:
        # x座標のリストの要素数が2の場合
        # y座標のリストから重複する値を削除した後のリストの要素数が1の場合
        if len(y_list) == 1:
            # x座標のリストから重複する値を削除した後のリストの要素数が2の場合
            # y座標のリストの要素数が1の場合
            # x座標のリストの要素数が2の場合
            # 重複する値を削除した後のリストの要素数が1の場合
            # x座標のリストから重

if __name__ == '__main__':
    main()