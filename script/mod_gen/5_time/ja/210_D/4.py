def main():
    H, W, C = map(int, input().split())
    A = []
    for i in range(H):
        A.append(list(map(int, input().split())))
    min_cost = 10**18
    # 縦横の2パターンでループ
    for i in range(2):
        # 1行ずつ読み込む
        for j in range(H):
            # 1行を読み込んで、配列に格納
            row = A[j]
            # 最小値を取得
            min_row = min(row)
            # 最小値のインデックスを取得
            min_row_idx = row.index(min_row)
            # 最小値のインデックスを削除
            del row[min_row_idx]
            # 次の最小値を取得
            next_min_row = min(row)
            # 最小値を取得
            min_col = min_row
            # 最小値のインデックスを取得
            min_col_idx = min_row_idx
            # 最小値のインデックスを削除
            del row[min_col_idx]
            # 次の最小値を取得
            next_min_col = min(row)
            # 最小値の組み合わせを調べる
            min_cost = min(min_cost, min_row + next_min_row + C, min_col + next_min_col + C)
            # 最小値を元に戻す
            row.insert(min_col_idx, min_col)
            row.insert(min_row_idx, min_row)
        # 縦横を入れ替える
        A = list(map(list, zip(*A)))
    print(min_cost)

if __name__ == '__main__':
    main()