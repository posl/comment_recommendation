def main():
    # 標準入力から文字列を取得
    S = input()
    # ACGT文字列の最大値を保持する変数
    max = 0
    # ACGT文字列の長さを保持する変数
    count = 0
    # ACGT文字列の最大値を保持する変数
    max = 0
    # ACGT文字列の長さを保持する変数
    count = 0
    # 文字列の長さ分ループ
    for i in range(len(S)):
        # 文字列がACGTの場合
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            # ACGT文字列の長さをインクリメント
            count += 1
        # 文字列がACGT以外の場合
        else:
            # ACGT文字列の最大値を保持する変数と比較
            if max < count:
                # ACGT文字列の最大値を保持する変数に代入
                max = count
            # ACGT文字列の長さを保持する変数を0に初期化
            count = 0
    # 最後の文字列がACGTの場合
    if max < count:
        # ACGT文字列の最大値を保持する変数に代入
        max = count
    # ACGT文字列の最大値を出力
    print(max)
