def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 部分列の和の最大値と最小値の差の絶対値を求める
    def calc(s, e):
        # 累積和の差
        diff = S[e] - S[s]
        # 部分列の和の最大値と最小値の差の絶対値
        return max(diff, S[-1] - diff)
    # 3箇所で切る
    ans = 10 ** 9
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            # i, jを切る
            ans = min(ans, calc(0, i), calc(i, j), calc(j, N))
    print(ans)
