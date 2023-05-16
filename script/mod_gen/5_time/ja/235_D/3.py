def main():
    # 標準入力から a と N を取得する
    a, N = map(int, input().split())
    # 1 から N までの数について、操作を繰り返す回数を格納する配列を作成する
    dp = [-1] * (N + 1)
    # 1 から N までの数について、操作を繰り返す回数を求める
    for i in range(1, N + 1):
        # 操作を繰り返す回数を求める
        cnt = 0
        # 操作を繰り返す
        while i > 0:
            # 操作を繰り返す回数を増やす
            cnt += 1
            # i を a で割った余りを i に代入する
            i %= a
        # 操作を繰り返す回数を配列に格納する
        dp[i] = cnt
    # N について、操作を繰り返す回数を出力する
    print(dp[N])

if __name__ == '__main__':
    main()