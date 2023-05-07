def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    # 1. 行と列の削除フラグを用意
    # 2. 行と列を削除
    # 3. 行と列の削除フラグによって、削除する行と列を削除
    # 4. 2. 3. を繰り返す
    # 5. マス目を出力
    # 1. 行と列の削除フラグを用意
    # 1.1. 行の削除フラグ
    row_delete = [True] * H
    # 1.2. 列の削除フラグ
    col_delete = [True] * W
    # 2. 行と列を削除
    # 2.1. 行を削除
    for i in range(H):
        if "#" not in a[i]:
            row_delete[i] = False
    # 2.2. 列を削除
    for j in range(W):
        if "#" not in [a[i][j] for i in range(H)]:
            col_delete[j] = False
    # 3. 行と列の削除フラグによって、削除する行と列を削除
    # 3.1. 行を削除
    for i in range(H):
        if not row_delete[i]:
            a[i] = ""
    # 3.2. 列を削除
    for j in range(W):
        if not col_delete[j]:
            for i in range(H):
                a[i] = a[i][:j] + a[i][j+1:]
    # 4. 2. 3. を繰り返す
    # 4.1. 行の削除フラグ
    row_delete = [True] * H
    # 4.2. 列の削除フラグ
    col_delete = [True] * W
    # 4.3. 行を

if __name__ == '__main__':
    main()