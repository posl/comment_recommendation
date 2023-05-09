def main():
    # 文字列を入力
    s = input()
    # 文字列の長さを取得
    len_s = len(s)
    # 文字列の長さが3かどうかを判定
    if len_s == 3:
        # 文字列を出力
        print('ARC')
    else:
        # 文字列を出力
        print('ABC')

if __name__ == '__main__':
    main()