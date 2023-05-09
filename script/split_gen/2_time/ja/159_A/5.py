def solve():
    # 標準入力から値を取得する
    n, m = map(int, input().split())
    # 処理
    answer = (n * (n - 1) // 2) + (m * (m - 1) // 2)
    # 結果出力
    print(answer)
