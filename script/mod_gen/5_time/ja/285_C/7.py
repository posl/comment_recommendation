def main():
    #文字列を入力
    s = input()
    #長さを取得
    n = len(s)
    #問題数を格納する変数
    cnt = 0
    #1文字の時
    if n == 1:
        cnt = ord(s) - ord("A") + 1
    #2文字の時
    elif n == 2:
        cnt = (ord(s[0]) - ord("A") + 1) * 26 + (ord(s[1]) - ord("A") + 1)
    #3文字の時
    elif n == 3:
        cnt = (ord(s[0]) - ord("A") + 1) * 26 * 26 + (ord(s[1]) - ord("A") + 1) * 26 + (ord(s[2]) - ord("A") + 1)
    #4文字の時
    elif n == 4:
        cnt = (ord(s[0]) - ord("A") + 1) * 26 * 26 * 26 + (ord(s[1]) - ord("A") + 1) * 26 * 26 + (ord(s[2]) - ord("A") + 1) * 26 + (ord(s[3]) - ord("A") + 1)
    #5文字の時
    elif n == 5:
        cnt = (ord(s[0]) - ord("A") + 1) * 26 * 26 * 26 * 26 + (ord(s[1]) - ord("A") + 1) * 26 * 26 * 26 + (ord(s[2]) - ord("A") + 1) * 26 * 26 + (ord(s[3]) - ord("A") + 1) * 26 + (ord(s[4]) - ord("A") + 1)
    #6文字の時
    elif n == 6:
        cnt = (ord(s[0]) - ord("A") + 1) * 26 * 26 * 26 * 26 * 26 + (ord(s[1]) - ord("A") + 1) * 26 * 26 * 26

if __name__ == '__main__':
    main()