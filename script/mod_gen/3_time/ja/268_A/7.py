def main():
    #入力
    a, b, c, d, e = map(int, input().split())
    #処理
    #set関数を用いて、重複する値を取り除く
    #len関数を用いて、要素数を数える
    #出力
    print(len(set([a, b, c, d, e])))

if __name__ == '__main__':
    main()