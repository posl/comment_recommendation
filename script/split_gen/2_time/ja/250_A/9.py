def main():
    # 2次元配列を作成
    # 1次元目がH、2次元目がW
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    # 1次元目の長さがhで、2次元目の長さがwの2次元配列を作成
    # 1次元目の長さがhで、2次元目の長さがwの2次元配列を作成
    # array = [[0 for j in range(w)] for i in range(h)]
    array = [[0]*w for i in range(h)]
    # 配列に値を入れる
    for i in range(h):
        for j in range(w):
            array[i][j] = abs(r-1-i) + abs(c-1-j)
    # 配列を出力する
    # for i in range(h):
    #     print(array[i])
    print(array[r-1][c-1])
