def main():
    # 標準入力から、R(行), C(列)を取得
    R, C = map(int, input().split())
    # 図のグリッドにおいて上から R 行目、左から C 列目のマスが黒色の場合は black と、白色の場合は white と出力せよ。
    if (R * C) % 2 == 0:
        print("black")
    else:
        print("white")
