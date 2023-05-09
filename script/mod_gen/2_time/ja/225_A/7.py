def main():
    #入力
    S = input()
    #文字列をリストに変換
    S = list(S)
    #重複を削除
    S = list(set(S))
    #文字列の長さを取得
    length = len(S)
    #出力
    print(length)
    #出力例 1
    #3
    #出力例 2
    #1
    #出力例 3
    #6

if __name__ == '__main__':
    main()