def main():
    X = int(input())
    # 500円硬貨の枚数
    n_500 = X // 500
    # 500円硬貨を使った時の嬉しさ
    a_500 = n_500 * 1000
    # 500円硬貨を使った時の残り
    X = X - n_500 * 500
    # 5円硬貨の枚数
    n_5 = X // 5
    # 5円硬貨を使った時の嬉しさ
    a_5 = n_5 * 5
    # 嬉しさの合計
    a = a_500 + a_5
    print(a)
