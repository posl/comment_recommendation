def main():
    # 入力
    N, X = map(int, input().split())
    a, b = [0] * N, [0] * N
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    # x座標の初期値
    x = 0
    # N回のジャンプ
    for i in range(N):
        # a_iかb_iのどちらかを選択
        if abs(X - (x + a[i])) <= abs(X - (x + b[i])):
            x = x + a[i]
        else:
            x = x + b[i]
    # 出力
    if x == X:
        print("Yes")
    else:
        print("No")
