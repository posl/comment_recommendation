def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 累積和を求める
    cumsum = [0] * (N + 1)
    for i in range(N):
        cumsum[i + 1] = cumsum[i] + A[i]
    # 最小値の更新
    mincumsum = [0] * (N + 1)
    mincumsum[0] = cumsum[0]
    for i in range(N):
        mincumsum[i + 1] = min(mincumsum[i], cumsum[i + 1])
    # 最大値の更新
    maxcumsum = [0] * (N + 1)
    maxcumsum[0] = cumsum[0]
    for i in range(N):
        maxcumsum[i + 1] = max(maxcumsum[i], cumsum[i + 1])
    # 3箇所で切る
    ans = 10 ** 18
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            # B, C, D, E
            B = cumsum[i]
            C = cumsum[j] - cumsum[i]
            D = cumsum[N] - cumsum[j]
            E = cumsum[N] - cumsum[N - 1]
            # P, Q, R, S
            P = B
            Q = C
            R = D
            S = E
            # P, Q, R, S の最大値と最小値の差の絶対値の最小値を求める
            ans = min(ans, max(P, Q, R, S) - min(P, Q, R, S))
            # B, C, D, E
            B = cumsum[i]
            C = cumsum[j] - cumsum[i]
            D = cumsum[N] - cumsum[j]
            E = cumsum[N - 1] - cumsum[j - 1]
            # P, Q, R, S
            P = B
            Q = C
            R = D
            S = E
            # P, Q, R, S の最
