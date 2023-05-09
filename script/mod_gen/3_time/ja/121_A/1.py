def main():
    # H 行 W 列の白色のマス目があります。
    # あなたは h 個の行と w 個の列を選び、選んだ行または列に含まれるマス目を全て黒色で塗りつぶします。
    # 白色のマス目はいくつ残るでしょうか。
    # なお、残る白色のマス目の数は行や列の選び方によらないことが証明できます。
    H, W = map(int, input().split())
    h, w = map(int, input().split())
    print((H-h)*(W-w))

if __name__ == '__main__':
    main()