def main():
    #入力
    N, X = map(int, input().split())
    #処理
    #文字列を作成
    #文字列の長さはN*26
    #文字列を作る
    str = ''
    for i in range(26):
        str += chr(ord('A') + i) * N
    #文字列からX番目の文字を出力
    print(str[X-1])

if __name__ == '__main__':
    main()