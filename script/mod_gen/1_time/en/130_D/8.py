def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    # 2つの累積和を用意
    # 累積和1: A[i]までの累積和
    # 累積和2: A[i]までの累積和 (A[i]がK以上の場合のみ)
    S1 = [0] * (N + 1)
    S2 = [0] * (N + 1)
    for i in range(N):
        S1[i + 1] = S1[i] + A[i]
        if A[i] >= K:
            S2[i + 1] = S2[i] + 1
        else:
            S2[i + 1] = S2[i]
    # S1[i] - S1[j] >= K の場合、S2[i] - S2[j] >= 1 である
    # S2[i] - S2[j] >= 1 の場合、S1[i] - S1[j] >= K である
    # つまり、S1[i] - K >= S1[j] となる S1[j] の個数を求めればよい
    # このとき、S1[i] - K は固定値になる
    # これを二分探索で求める
    for i in range(N + 1):
        # S1[i] - K >= 0 となる最小のjを求める
        l = 0
        r = i
        while r - l > 1:
            m = (l + r) // 2
            if S1[i] - K >= S1[m]:
                l = m
            else:
                r = m
        # S1[i] - K >= S1[l] となるjの個数を求める
        ans += i - l
    print(ans)

if __name__ == '__main__':
    main()