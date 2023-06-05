def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]
        S[i + 1] %= M
    from collections import Counter
    C = Counter(S)
    ans = 0
    for v in C.values():
        ans += v * (v - 1) // 2
    print(ans)
