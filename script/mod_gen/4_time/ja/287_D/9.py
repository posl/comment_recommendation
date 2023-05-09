def main():
    s = input()
    t = input()
    # 入力された文字列の長さを取得
    s_len = len(s)
    t_len = len(t)
    # Sの先頭の x 文字と末尾の |T|-x 文字を順番を保ったまま連結することで得られる長さ |T| の文字列を S' とする。
    # S' と T がマッチするならば Yes と、そうでなければ No と出力
    for i in range(t_len + 1):
        if s[:i] + t_len - i == t:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()