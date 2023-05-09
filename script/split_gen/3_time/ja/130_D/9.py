def solve():
    N, K = map(int,input().split())
    A = list(map(int,input().split()))
    # Aの累積和を求める
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 尺取り法で解く
    ans = 0
    r = 0
    for l in range(N):
        while r < N and S[r + 1] - S[l] < K:
            r += 1
        ans += N - r
    print(ans)
