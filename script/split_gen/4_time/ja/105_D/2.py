def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    # 累積和
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
    # 累積和を M で割った余りの個数を数える
    from collections import Counter
    C = Counter([s % M for s in S])
    ans = 0
    # 余りが同じ累積和の組み合わせを数える
    for c in C.values():
        ans += c * (c - 1) // 2
    print(ans)
