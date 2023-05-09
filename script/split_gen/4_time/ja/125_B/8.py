def main():
    # 標準入力受付
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    # 価値の合計
    X = 0
    # 支払いコストの合計
    Y = 0
    # X-Yの最大値
    max = 0
    # 宝石の数だけループ
    for i in range(N):
        # 価値の合計に宝石の価値を加算
        X += V[i]
        # 支払いコストの合計に宝石の支払いコストを加算
        Y += C[i]
        # X-Yの最大値を更新
        if max < X-Y:
            max = X-Y
    # X-Yの最大値を出力
    print(max)
