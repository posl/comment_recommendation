def main():
    # 標準入力の取得
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # 処理
    # 入力値のうち、x番目の値を取得
    target = a[x-1]
    # 結果の初期化
    result = 1
    # 取得した値がx番目の値と同じでない限り処理を繰り返す
    while target != x:
        # 結果に+1する
        result += 1
        # 取得した値を更新する
        target = a[target-1]
    # 結果の出力
    print(result)
    return

if __name__ == '__main__':
    main()