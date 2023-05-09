def main():
    # 標準入力から N, A, B を取得する
    N, A, B = map(int, input().split())
    # N 人の交通費の合計の最小値を出力する
    print(min(A*N, B))
