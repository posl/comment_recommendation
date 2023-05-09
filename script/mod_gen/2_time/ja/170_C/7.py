def main():
    # 標準入力から X, N を取得
    X, N = map(int, input().split())
    # 標準入力から N 個の整数列 p を取得
    p = list(map(int, input().split()))
    # X との差の絶対値が最小のものを求める
    # 絶対値の最小値を 0 で初期化
    min_diff = 0
    # 絶対値の最小値になる数を X で初期化
    min_diff_num = X
    # X との差の絶対値が最小のものを求める
    for i in range(100):
        # X との差の絶対値を求める
        diff = abs(X - i)
        # 絶対値の最小値になる数を更新する
        if i not in p:
            if min_diff == 0:
                min_diff = diff
                min_diff_num = i
            elif min_diff > diff:
                min_diff = diff
                min_diff_num = i
    # 絶対値の最小値になる数を出力する
    print(min_diff_num)

if __name__ == '__main__':
    main()