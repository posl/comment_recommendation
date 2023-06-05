def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # しゃくとり法
    res = 0
    r = 0
    for l in range(N):
        while r < N + 1 and S[r] - S[l] < K:
            r += 1
        res += N - r + 1
    print(res)
solve()
