def main():
    N, K = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(N)]
    # 点数の合計を求める
    sum_P = [sum(p) for p in P]
    # 点数の合計を降順にソートしたときのインデックスを求める
    sorted_sum_P = sorted(range(N), key=lambda x: sum_P[x], reverse=True)
    # 点数の合計が同じものがあるかどうかをチェック
    same = False
    for i in range(N - 1):
        if sum_P[sorted_sum_P[i]] == sum_P[sorted_sum_P[i + 1]]:
            same = True
            break
    # 点数の合計が同じものがある場合は、
    # その点数の合計を取った人のうち、
    # 3 日目の点数が高い順にソートしたときのインデックスを求める
    if same:
        for i in range(N - 1):
            if sum_P[sorted_sum_P[i]] == sum_P[sorted_sum_P[i + 1]]:
                sorted_P = sorted(range(i, i + 2), key=lambda x: P[x][2], reverse=True)
                sorted_sum_P[i:i + 2] = sorted_P
    # 上位 K 位以内に入っているかどうかをチェック
    for i in range(N):
        if sorted_sum_P.index(i) < K:
            print("Yes")
        else:
            print("No")
