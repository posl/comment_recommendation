def main():
    N, K = map(int, input().split())
    # 確率
    prob = 0
    # 1からNまでの確率を計算
    for i in range(1, N + 1):
        # サイコロの目
        dice = i
        # 確率
        p = 1 / N
        # サイコロの目がK未満の場合
        while dice < K:
            # コインを振り、表が出たら2倍になる
            dice *= 2
            # コインの確率
            p *= 0.5
        # 確率を足す
        prob += p
    # 確率を出力
    print(prob)
