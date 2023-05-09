def main():
    # 文字列の入力
    S = input()
    # 雨の日数
    R_count = 0
    # 雨の日数の最大値
    R_max = 0
    # 文字列の文字を取り出す
    for s in S:
        # 文字が雨の日の場合
        if s == 'R':
            # 雨の日数をカウントアップ
            R_count += 1
        # 文字が雨の日ではない場合
        else:
            # 雨の日数の最大値を更新
            R_max = max(R_count, R_max)
            # 雨の日数をリセット
            R_count = 0
    # 最後の日の雨の日数の最大値を更新
    R_max = max(R_count, R_max)
    # 雨の日数の最大値を出力
    print(R_max)

if __name__ == '__main__':
    main()