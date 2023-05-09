def main():
    N, K = map(int, input().split())
    # 入力を受け取る
    P = [list(map(int, input().split())) for _ in range(N)]
    # 3 日目の合計点のリストを作る
    S = [sum(p) for p in P]
    # 4 日目の試験後の順位を計算する
    # 4 日目の試験後の順位は、その生徒よりも 4 日間の合計点が高い生徒の人数に 1 を加えた値として定めます。
    R = [sum(s > t for t in S) + 1 for s in S]
    # 上位 K 位以内に入っていることがあり得るかどうか判定して出力する
    for r in R:
        print('Yes' if r <= K else 'No')
