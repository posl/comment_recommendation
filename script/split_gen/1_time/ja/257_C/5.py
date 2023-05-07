def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))
    # Sの0と1の数をカウント
    S0 = S.count('0')
    S1 = S.count('1')
    # Wをソート
    W.sort()
    # Wの累積和を計算
    Wsum = [0] * (N + 1)
    for i in range(N):
        Wsum[i + 1] = Wsum[i] + W[i]
    # 二分探索
    def is_ok(x):
        # x未満の人の体重の和
        w0 = Wsum[S0]
        # x以上の人の体重の和
        w1 = Wsum[-1] - Wsum[N - S1]
        # 残りの人の体重の和
        w2 = Wsum[N] - w0 - w1
        # 二つの体重の和の差がx未満ならTrue
        return abs(w2 - w0) < x
    # 二分探索
    def binary_search():
        # 求める範囲を[l, r]とする
        l = 0
        r = 10 ** 9
        while r - l > 1:
            x = (l + r) // 2
            if is_ok(x):
                l = x
            else:
                r = x
        return l
    # 二分探索
    ans = binary_search()
    print(ans)
