def main():
    # 1行目の入力
    k = int(input())
    # 文字列の初期化
    s = ''
    # Aから昇順にK個繋げる
    for i in range(k):
        s += chr(ord('A') + i)
    # 出力
    print(s)

if __name__ == '__main__':
    main()